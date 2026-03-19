# 🔄 AI 换脸替代方案 — 免费开源

**免费本地换脸 (InsightFace) + AI 画质增强 (Real-ESRGAN) + 云端 AI 生成 (Atlas Cloud)**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)](https://docs.astral.sh/uv/)
[![Atlas Cloud](https://img.shields.io/badge/Atlas%20Cloud-API-orange)](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

---

## ✨ 为什么选择这个工具？

- 🆓 **100% 免费本地换脸** — 无需 API Key、无需云端、零成本
- 🔒 **隐私保护** — 所有处理在本地完成，图片不会上传
- ⚡ **一条命令** — `uv run` 即可运行，依赖自动安装
- 🎭 **高质量** — InsightFace (inswapper_128) + Real-ESRGAN 增强
- ☁️ **可选云端功能** — API 换脸 + AI 肖像生成
- 🤖 **AI Agent 就绪** — 支持 Claude Code、Cursor、Windsurf 等
- 💰 **省钱** — 替代 FaceApp ($4.99/月)、Reface ($12.99/月)、DeepSwap ($9.99/月)

---

## 📦 安装

### 1. 添加 Skill

```bash
npx skills add ristponex/ai-face-swap-alternative-skill
```

### 2. 前置条件

- **Python 3.10 - 3.12** (3.13 暂不支持)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python 包管理器

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. 云端设置（可选）

```bash
cp .env.example .env
# 编辑 .env 填入 API Key
```

在 [atlascloud.ai](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) 获取 API Key。

---

## 🆓 免费本地工具

### 换脸 (`scripts/face-swap.py`)

使用 **InsightFace** (inswapper_128) 在两张图片之间交换人脸。完全本地运行，首次下载模型后可离线使用。

```bash
uv run scripts/face-swap.py --source 人脸.jpg --target 目标.jpg -o 输出.jpg
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--source` | 提供人脸的源图片 | 必填 |
| `--target` | 被替换人脸的目标图片 | 必填 |
| `-o, --output` | 输出文件路径 | `./output/<target>_swapped.png` |
| `--face-index` | 替换目标图中第几张脸（从 0 开始） | `0` |

**合照中替换指定人脸：**

```bash
uv run scripts/face-swap.py --source 脸.jpg --target 合照.jpg --face-index 2
```

### 人脸增强 (`scripts/face-enhance.py`)

使用 **Real-ESRGAN** (NCNN 后端) 增强人脸和图片质量，适合修复老照片和模糊人脸。

```bash
uv run scripts/face-enhance.py 输入.jpg -o 增强后/
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `input` | 输入图片或文件夹 | 必填 |
| `-o, --output` | 输出目录 | `./output/` |
| `--mode` | `enhance`（增强细节，保持尺寸）或 `upscale`（4 倍放大） | `enhance` |
| `--sharpness` | 锐度系数（1.0 = 不变） | `1.3` |
| `--contrast` | 对比度系数（1.0 = 不变） | `1.1` |
| `--gpu` | GPU ID（-1 为纯 CPU） | `0` |

**批量处理文件夹：**

```bash
uv run scripts/face-enhance.py ./照片/ -o ./增强后/
```

---

## ☁️ 云端功能（可选）

需要 [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) API Key。

### 云端换脸

```bash
uv run scripts/cloud-generate.py swap 源图.jpg 目标.jpg -o 输出/
```

### AI 肖像生成

```bash
uv run scripts/cloud-generate.py generate "专业头像照，工作室灯光" \
  --model black-forest-labs/flux-2-pro
```

---

## 💰 价格对比

| 应用 | 价格 | 功能 |
|------|------|------|
| **本工具（本地）** | **免费** | 换脸 + 增强，无限使用 |
| FaceApp | $4.99/月 | 换脸、滤镜 |
| Reface | $12.99/月 | 换脸、GIF |
| DeepSwap | $9.99/月 | 换脸、视频 |
| FaceMagic | $5.99/月 | 换脸 |

---

## 🌐 相关开源工具

| 工具 | Stars | 特点 | 链接 |
|------|-------|------|------|
| **Deep-Live-Cam** | 80k+ | 实时摄像头换脸 | [GitHub](https://github.com/hacksider/Deep-Live-Cam) |
| **InsightFace** | 28k+ | 核心人脸分析库 | [GitHub](https://github.com/deepinsight/insightface) |
| **FaceFusion** | 27k+ | roop 继任者，Web GUI | [GitHub](https://github.com/facefusion/facefusion) |
| **Rope** | 5.3k+ | GUI 换脸工具 | [GitHub](https://github.com/Hillobar/Rope) |
| **VisoMaster** | 1.8k+ | 新 SOTA，VR180 支持 | [GitHub](https://github.com/visomaster/VisoMaster) |

---

## ❓ 常见问题

**需要 GPU 吗？** 不需要。本地换脸通过 ONNX Runtime 在 CPU 上运行。人脸增强可用 `--gpu -1` 强制使用 CPU。

**支持离线吗？** 支持。首次运行下载模型后（约 270MB），无需网络连接。

**支持什么图片格式？** JPG、JPEG、PNG、WebP、BMP、TIFF。默认输出 PNG。

**能否在合照中换指定的脸？** 可以。使用 `--face-index` 参数选择第几张脸。

---

## 📄 许可证

[MIT](LICENSE)

---

如果这个工具帮你省了钱，请给个 Star！

[![Star History](https://img.shields.io/github/stars/ristponex/ai-face-swap-alternative-skill?style=social)](https://github.com/ristponex/ai-face-swap-alternative-skill)
