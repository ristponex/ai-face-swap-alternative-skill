---
name: ai-face-swap-alternative
description: "Free AI face swap + cloud AI generation. Local tools: face swap between images using InsightFace (100% free, offline, no API key), face enhance using Real-ESRGAN. Cloud tools: API face swap and AI portrait generation via Atlas Cloud (optional, requires API key). Use when user asks to swap faces, replace faces, face merge, or enhance face quality."
---

# AI Face Swap Alternative — Free & Open Source

**2 free local tools** + **cloud AI features** (optional, via Atlas Cloud API).

Local tools run 100% on your machine — no API keys, no cloud, no cost.

## Prerequisites

- Python 3.10 - 3.12 installed (3.13 not yet supported by some dependencies)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

## Available Tools

| Tool | Script | What It Does | API Key? |
|------|--------|-------------|----------|
| **Face Swap** | `scripts/face-swap.py` | Swap faces between images (InsightFace) | No (FREE) |
| **Face Enhance** | `scripts/face-enhance.py` | Enhance face quality (Real-ESRGAN) | No (FREE) |
| **Cloud Swap** | `scripts/cloud-generate.py swap` | Cloud face swap via API | Yes |
| **Cloud Generate** | `scripts/cloud-generate.py generate` | AI portrait generation | Yes |

## Usage

### Free Local Face Swap (no API key needed)
```bash
uv run scripts/face-swap.py source_face.jpg target_image.jpg -o output.jpg
```

### Free Local Face Enhancement
```bash
uv run scripts/face-enhance.py input.jpg -o enhanced.jpg
```

### Cloud Face Swap (requires API key)
```bash
uv run scripts/cloud-generate.py swap source.jpg target.jpg
```

### Cloud AI Portrait Generation (requires API key)
```bash
uv run scripts/cloud-generate.py generate "professional headshot of a person" --model black-forest-labs/flux-2-pro
```
