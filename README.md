# 🔄 AI Face Swap Alternative — Free & Open Source

**Free local face swap (InsightFace) + AI enhancement (Real-ESRGAN) + Cloud AI generation (Atlas Cloud)**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)](https://docs.astral.sh/uv/)
[![Atlas Cloud](https://img.shields.io/badge/Atlas%20Cloud-API-orange)](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

---

## ✨ Why This Skill?

- 🆓 **100% FREE local face swap** — no API key, no cloud, no cost
- 🔒 **Privacy first** — all processing happens on your machine, nothing gets uploaded
- ⚡ **One command** — `uv run` and go, dependencies auto-install
- 🎭 **High quality** — InsightFace (inswapper_128) + Real-ESRGAN enhancement
- ☁️ **Optional cloud features** — API face swap + AI portrait generation via Atlas Cloud
- 🤖 **AI Agent ready** — works with Claude Code, Cursor, Windsurf, and other AI coding tools
- 💰 **Save money** — free alternative to FaceApp ($4.99/mo), Reface ($12.99/mo), DeepSwap ($9.99/mo)

---

## 📦 Installation

### 1. Add the Skill

```bash
npx skills add ristponex/ai-face-swap-alternative-skill
```

This installs the skill so AI agents (Claude Code, Cursor, etc.) can use it automatically.

### 2. Prerequisites

- **Python 3.10 - 3.12** (3.13 is not yet supported by some dependencies)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python package manager (auto-manages Python versions)

If you don't have `uv` installed:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **Note:** `uv` will automatically download and manage the correct Python version if needed. You don't need to install Python separately.

### 3. Cloud Setup (Optional)

Cloud features (API face swap & AI generation) require an Atlas Cloud API key. Local tools work without any API key.

```bash
cp .env.example .env
# Edit .env and add your API key
```

Get your API key at [atlascloud.ai](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

---

## 🆓 Free Local Tools

### Face Swap (`scripts/face-swap.py`)

Swap faces between two images using **InsightFace** (inswapper_128 model). Runs 100% locally — no API key, no internet connection needed after first model download.

**Powered by:**
- [InsightFace](https://github.com/deepinsight/insightface) — State-of-the-art face analysis library
- inswapper_128 model — High-quality face swapping (auto-downloaded on first run)
- ONNX Runtime — Cross-platform inference engine

#### Basic Usage

```bash
uv run scripts/face-swap.py --source face.jpg --target photo.jpg -o output.jpg
```

#### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--source` | Source face image (the face to use) | Required |
| `--target` | Target image (the face to replace) | Required |
| `-o, --output` | Output file path | `./output/<target>_swapped.png` |
| `--face-index` | Which face in target to swap (for group photos) | `0` |

#### Examples

**Simple face swap:**

```bash
uv run scripts/face-swap.py --source celebrity.jpg --target selfie.jpg -o result.jpg
```

**Group photo — swap specific face:**

```bash
# Swap the third face (index starts at 0)
uv run scripts/face-swap.py --source face.jpg --target group.jpg --face-index 2 -o result.jpg
```

#### How It Works

1. Detects all faces in both source and target images
2. Extracts the face embedding from the source image
3. Replaces the selected face in the target image using the inswapper_128 model
4. Saves the output with the swapped face seamlessly blended

---

### Face Enhance (`scripts/face-enhance.py`)

Enhance face and image quality using **Real-ESRGAN** with NCNN backend. Great for restoring old photos, fixing blurry faces, and improving image details.

**Powered by:**
- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — Practical image restoration model
- NCNN backend — Fast inference, works on CPU and GPU

#### Basic Usage

```bash
uv run scripts/face-enhance.py input.jpg -o enhanced.jpg
```

#### Options

| Flag | Description | Default |
|------|-------------|---------|
| `input` | Input image path or folder | Required |
| `-o, --output` | Output directory | `./output/` |
| `--mode` | `enhance` (detail boost, keep size) or `upscale` (4x enlarge) | `enhance` |
| `--sharpness` | Sharpness factor (1.0 = unchanged) | `1.3` |
| `--contrast` | Contrast factor (1.0 = unchanged) | `1.1` |
| `--gpu` | GPU ID (-1 for CPU) | `0` |

#### Examples

**Enhance a single image (keep original size, boost details):**

```bash
uv run scripts/face-enhance.py old_photo.jpg -o restored/
```

**4x upscale:**

```bash
uv run scripts/face-enhance.py low_res.jpg --mode upscale -o output/
```

**Batch processing a folder:**

```bash
uv run scripts/face-enhance.py ./photos/ -o ./enhanced_photos/
```

**Fine-tune sharpness and contrast:**

```bash
uv run scripts/face-enhance.py portrait.jpg --sharpness 1.5 --contrast 1.2
```

**CPU-only processing:**

```bash
uv run scripts/face-enhance.py input.jpg --gpu -1
```

#### Enhancement Modes

| Mode | What It Does | Output Size |
|------|-------------|-------------|
| `enhance` | Upscales with Real-ESRGAN then downscales back, boosting detail and removing artifacts | Same as input |
| `upscale` | 4x super-resolution enlargement | 4x input size |

---

## ☁️ Cloud Features (Optional)

Cloud features require an [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) API key. They're useful when you want faster processing, don't have a GPU, or need AI-generated portraits.

### Cloud Face Swap

API-based face swap using the `atlascloud/image-face-swap` model. No local GPU required — processing happens in the cloud.

```bash
uv run scripts/cloud-generate.py swap source.jpg target.jpg -o output/
```

**When to use cloud swap vs local swap:**

| | Local (face-swap.py) | Cloud (cloud-generate.py swap) |
|---|---|---|
| **Cost** | Free | Pay per use |
| **Privacy** | 100% local | Images sent to API |
| **Speed** | Depends on CPU/GPU | Fast, server-side |
| **Setup** | Auto (first run downloads model) | API key needed |
| **Offline** | Works offline | Requires internet |

### AI Portrait Generation

Generate AI portraits, headshots, or any image using any model available on Atlas Cloud (Flux, Seedream, Stable Diffusion, etc.).

```bash
# Generate with Flux 2 Pro
uv run scripts/cloud-generate.py generate "professional headshot of a young woman, studio lighting" \
  --model black-forest-labs/flux-2-pro

# Generate with a specific size
uv run scripts/cloud-generate.py generate "cinematic portrait, dramatic lighting" \
  --model black-forest-labs/flux-2-pro --size 1024x1024

# Pass extra model-specific parameters
uv run scripts/cloud-generate.py generate "portrait painting, oil on canvas style" \
  --model black-forest-labs/flux-2-pro --extra '{"num_inference_steps": 30}'
```

#### Generation Options

| Flag | Description | Default |
|------|-------------|---------|
| `prompt` | Text description of the image to generate | Required |
| `--model` | Model ID on Atlas Cloud | `black-forest-labs/flux-2-pro` |
| `--size` | Image dimensions (e.g., `1024x1024`) | Model default |
| `--extra` | Additional parameters as JSON string | None |
| `-o, --output` | Output directory | `./output/` |

---

## 💰 Price Comparison vs Paid Apps

Why pay for face swap apps when you can do it for free?

| App | Price | Features |
|-----|-------|----------|
| **This Skill (local)** | **FREE** | Face swap + face enhance, unlimited use |
| FaceApp | $4.99/mo | Face swap, filters, aging |
| Reface | $12.99/mo | Face swap, GIF swap |
| DeepSwap | $9.99/mo | Face swap, video swap |
| FaceMagic | $5.99/mo | Face swap, video |

With this skill you get **unlimited** face swaps and enhancements at **zero cost**, running entirely on your own machine with full privacy.

---

## 🌐 Related Open Source Tools

This skill builds on top of the amazing open source face swap ecosystem. Here are some notable projects:

| Tool | GitHub Stars | Features | Link |
|------|-------------|----------|------|
| **Deep-Live-Cam** | 80k+ | Real-time webcam face swap, one-click deepfake | [github.com/hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) |
| **InsightFace** | 28k+ | Core face analysis library, ArcFace, inswapper | [github.com/deepinsight/insightface](https://github.com/deepinsight/insightface) |
| **FaceFusion** | 27k+ | Next-gen face swapper (roop successor), web GUI | [github.com/facefusion/facefusion](https://github.com/facefusion/facefusion) |
| **Rope** | 5.3k+ | GUI-based face swap tool, easy to use | [github.com/Hillobar/Rope](https://github.com/Hillobar/Rope) |
| **VisoMaster** | 1.8k+ | New SOTA face swap, VR180 support | [github.com/visomaster/VisoMaster](https://github.com/visomaster/VisoMaster) |

**How this skill differs:**
- Designed for **AI agents** (Claude Code, Cursor) — not just manual GUI use
- **Zero-config** — `uv run` handles all dependencies automatically
- **Combined workflow** — face swap + enhancement + cloud generation in one package
- **Lightweight** — no heavy GUI frameworks, just Python scripts

---

## 🤖 Using with AI Agents

This skill is designed to work seamlessly with AI coding agents. Once installed, your AI agent can:

- **Swap faces** between photos with a natural language request
- **Enhance** blurry or old photos automatically
- **Generate** AI portraits from text descriptions

### Claude Code

```bash
# Install the skill
npx skills add ristponex/ai-face-swap-alternative-skill

# Then just ask Claude:
# "Swap the face from selfie.jpg onto group.jpg"
# "Enhance this old family photo"
# "Generate a professional headshot"
```

### Cursor / Windsurf

After installing the skill, the AI agent picks up the `SKILL.md` file and knows how to use all available tools.

---

## ❓ FAQ

### Do I need a GPU?

**No.** Local face swap runs on CPU via ONNX Runtime. Face enhancement uses NCNN which supports both CPU and GPU. Use `--gpu -1` to force CPU-only mode.

### Does it work offline?

**Yes.** After the first run (which downloads the InsightFace model ~270MB), everything works offline. No internet connection required.

### What image formats are supported?

JPG, JPEG, PNG, WebP, BMP, and TIFF for input. Output is saved as PNG by default.

### Can I swap multiple faces in a group photo?

**Yes.** Use the `--face-index` flag to select which face to swap. Faces are indexed starting from 0. The script reports how many faces it detects in each image.

### Is Python 3.13 supported?

**Not yet.** Some dependencies (InsightFace, ONNX Runtime) don't have Python 3.13 wheels. Use Python 3.10-3.12. If you use `uv`, it will automatically manage the correct Python version.

### How is this different from Deep-Live-Cam or FaceFusion?

Those are full-featured desktop apps with GUI interfaces. This skill is designed as a **lightweight CLI tool** that integrates with AI coding agents. It's simpler to set up (`uv run` and done), easier to automate, and includes cloud AI generation features.

### Do I need to pay for anything?

**No.** Local face swap and enhancement are 100% free with no limits. Cloud features (API swap + AI generation) are optional and use [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) credits.

---

## 📁 Project Structure

```
ai-face-swap-alternative-skill/
├── scripts/
│   ├── face-swap.py           # Free local face swap (InsightFace)
│   ├── face-enhance.py        # Free local face enhance (Real-ESRGAN)
│   └── cloud-generate.py      # Cloud face swap & AI generation (Atlas Cloud)
├── SKILL.md                   # AI agent skill definition
├── .env.example               # Environment template
├── LICENSE                    # MIT License
├── README.md                 # English (this file)
├── README_zh.md              # 中文
├── README_ja.md              # 日本語
└── README_ko.md              # 한국어
```

---

## 🛠️ Technical Details

### Dependencies

**Local Face Swap (face-swap.py):**
- `insightface >= 0.7.3` — Face detection and swapping
- `onnxruntime >= 1.16.0` — Model inference
- `opencv-python-headless >= 4.8` — Image processing
- `numpy < 2` — Numerical operations
- `pillow >= 10.0` — Image I/O

**Local Face Enhance (face-enhance.py):**
- `realesrgan-ncnn-py >= 2.0.0` — Super-resolution model
- `pillow >= 10.0` — Image I/O

**Cloud Generate (cloud-generate.py):**
- `requests >= 2.31` — HTTP client
- `pillow >= 10.0` — Image I/O

All dependencies are declared inline using [PEP 723](https://peps.python.org/pep-0723/) script metadata and managed automatically by `uv`.

### Models

| Model | Size | Purpose | Source |
|-------|------|---------|--------|
| buffalo_l | ~320MB | Face detection/analysis | InsightFace (auto-download) |
| inswapper_128 | ~270MB | Face swapping | [HuggingFace](https://huggingface.co/deepinsight/inswapper) (auto-download) |
| realesrgan-x4plus | ~64MB | Image enhancement | Bundled with realesrgan-ncnn-py |

Models are automatically downloaded on first use and cached locally.

---

## 📄 License

[MIT](LICENSE) — Use it however you want.

---

## 🌟 Star This Repo

If this skill saved you from paying for expensive face swap apps, consider giving it a star! It helps others discover free alternatives.

[![Star History](https://img.shields.io/github/stars/ristponex/ai-face-swap-alternative-skill?style=social)](https://github.com/ristponex/ai-face-swap-alternative-skill)
