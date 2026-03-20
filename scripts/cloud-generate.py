#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests>=2.31",
#   "pillow>=10.0",
# ]
# ///

"""
云端 AI 换脸 & 图像生成 — 通过 Atlas Cloud API
支持 API 换脸 (atlascloud/image-face-swap) 和 AI 肖像生成
本地换脸请用 face-swap.py（免费、离线、无 API Key）
"""

import argparse
import os
import sys
import time
import json
import base64
import requests
from pathlib import Path


API_BASE = "https://api.atlascloud.ai/api/v1/model"


def get_api_key():
    """获取 API Key"""
    key = os.environ.get("ATLAS_CLOUD_API_KEY") or os.environ.get("ATLASCLOUD_API_KEY")
    if not key:
        for env_file in [".env", os.path.expanduser("~/.env")]:
            if os.path.exists(env_file):
                with open(env_file) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith(("ATLAS_CLOUD_API_KEY=", "ATLASCLOUD_API_KEY=")):
                            key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            if key:
                break
    if not key:
        print("Error: Atlas Cloud API Key not found")
        print()
        print("For FREE local face swap (no API key needed), use:")
        print("  uv run scripts/face-swap.py source.jpg target.jpg -o output.jpg")
        print()
        print("For cloud features, get your API key:")
        print("  https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill")
        sys.exit(1)
    return key


def image_to_data_url(path):
    """将图片转为 data URL"""
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    ext = Path(path).suffix.lstrip(".").lower()
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}.get(ext, f"image/{ext}")
    return f"data:{mime};base64,{data}"


def submit_request(endpoint, payload, api_key):
    """提交请求"""
    url = f"{API_BASE}/{endpoint}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    if resp.status_code != 200:
        print(f"API error ({resp.status_code}): {resp.text[:500]}")
        sys.exit(1)
    data = resp.json()
    if data.get("code") and data.get("code") != 200:
        print(f"API error: {data.get('message', 'Unknown error')}")
        sys.exit(1)
    request_id = data.get("data", {}).get("id") or data.get("request_id")
    if not request_id:
        print(f"Unexpected response: {json.dumps(data, indent=2)}")
        sys.exit(1)
    return request_id


def poll_result(request_id, api_key, max_wait=120):
    """轮询结果"""
    url = f"{API_BASE}/result/{request_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            resp = requests.get(url, headers=headers, timeout=30)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            time.sleep(2)
            continue
        if resp.status_code != 200:
            time.sleep(2)
            continue
        raw = resp.json()
        data = raw.get("data", raw)
        status = data.get("status", "")
        if status in ("completed", "succeeded"):
            return data.get("outputs") or data.get("output") or []
        if status == "failed":
            print(f"\nFailed: {data.get('error', 'Unknown error')}")
            sys.exit(1)
        elapsed = int(time.time() - start_time)
        print(f"\r  Waiting... {elapsed}s", end="", flush=True)
        time.sleep(2)
    print(f"\nTimeout after {max_wait}s")
    sys.exit(1)


def download_file(url, output_path):
    """下载文件"""
    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)


def cmd_swap(args):
    """云端换脸"""
    api_key = get_api_key()
    output_dir = Path(args.output) if args.output else Path("./output")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"  Source face: {args.source}")
    print(f"  Target image: {args.target}")

    payload = {
        "model": "atlascloud/image-face-swap",
        "source_image": image_to_data_url(args.source),
        "target_image": image_to_data_url(args.target),
    }

    print("\n  Submitting face swap request...")
    request_id = submit_request("generateImage", payload, api_key)
    print(f"  Request ID: {request_id}")

    outputs = poll_result(request_id, api_key)
    if not outputs:
        print("\nNo result")
        sys.exit(1)

    urls = outputs if isinstance(outputs, list) else [outputs]
    for i, url in enumerate(urls):
        if isinstance(url, dict):
            url = url.get("url") or str(url)
        filepath = str(output_dir / f"swapped_{int(time.time())}_{i}.png")
        download_file(url, filepath)
        print(f"\n  Saved: {filepath}")

    print("\nDone!")


def cmd_generate(args):
    """云端 AI 图像生成（肖像、人脸等）"""
    api_key = get_api_key()
    output_dir = Path(args.output) if args.output else Path("./output")
    output_dir.mkdir(parents=True, exist_ok=True)

    model = args.model

    payload = {"model": model, "prompt": args.prompt}
    if args.size:
        payload["image_size"] = args.size
    if args.extra:
        payload.update(json.loads(args.extra))

    print(f"  Model: {model}")
    print(f"  Prompt: {args.prompt[:80]}...")
    print("\n  Submitting...")

    request_id = submit_request("generateImage", payload, api_key)
    outputs = poll_result(request_id, api_key)
    if not outputs:
        print("\nNo images generated")
        sys.exit(1)

    urls = outputs if isinstance(outputs, list) else [outputs]
    for i, url in enumerate(urls):
        if isinstance(url, dict):
            url = url.get("url") or str(url)
        filepath = str(output_dir / f"generated_{int(time.time())}_{i}.png")
        download_file(url, filepath)
        print(f"  Saved: {filepath}")

    print(f"\nDone! {len(urls)} image(s) saved.")


def main():
    parser = argparse.ArgumentParser(description="Cloud AI Face Swap & Portrait Generation")
    sub = parser.add_subparsers(dest="command")

    # 云端换脸
    p = sub.add_parser("swap", help="Cloud-based face swap via Atlas Cloud API")
    p.add_argument("source", help="Source face image")
    p.add_argument("target", help="Target image to swap face into")
    p.add_argument("-o", "--output", help="Output directory")

    # AI 生成
    p = sub.add_parser("generate", help="Generate AI portraits/faces")
    p.add_argument("prompt", help="Text prompt")
    p.add_argument("--model", default="google/nano-banana-2/text-to-image", help="Model ID")
    p.add_argument("--size", help="Image size")
    p.add_argument("--extra", help="Extra params as JSON")
    p.add_argument("-o", "--output", help="Output directory")

    args = parser.parse_args()
    if args.command == "swap":
        cmd_swap(args)
    elif args.command == "generate":
        cmd_generate(args)
    else:
        parser.print_help()
        print("\n  For FREE local face swap (no API key):")
        print("  uv run scripts/face-swap.py source.jpg target.jpg -o output.jpg")


if __name__ == "__main__":
    main()
