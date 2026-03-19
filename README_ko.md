# 🔄 AI 얼굴 교체 대안 — 무료 오픈소스

**무료 로컬 얼굴 교체 (InsightFace) + AI 화질 향상 (Real-ESRGAN) + 클라우드 AI 생성 (Atlas Cloud)**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)](https://docs.astral.sh/uv/)
[![Atlas Cloud](https://img.shields.io/badge/Atlas%20Cloud-API-orange)](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

---

## ✨ 이 도구를 선택하는 이유

- 🆓 **100% 무료 로컬 얼굴 교체** — API 키 불필요, 클라우드 불필요, 비용 제로
- 🔒 **프라이버시 보호** — 모든 처리가 로컬에서 이루어지며, 이미지가 업로드되지 않습니다
- ⚡ **원 커맨드** — `uv run`으로 실행, 의존성 자동 설치
- 🎭 **고품질** — InsightFace (inswapper_128) + Real-ESRGAN 향상
- ☁️ **선택적 클라우드 기능** — API 얼굴 교체 + AI 초상화 생성
- 🤖 **AI 에이전트 지원** — Claude Code, Cursor, Windsurf 등과 연동
- 💰 **절약** — FaceApp ($4.99/월), Reface ($12.99/월), DeepSwap ($9.99/월)의 무료 대안

---

## 📦 설치

### 1. 스킬 추가

```bash
npx skills add ristponex/ai-face-swap-alternative-skill
```

### 2. 사전 요구 사항

- **Python 3.10 - 3.12** (3.13은 일부 의존성에서 미지원)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python 패키지 관리자

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. 클라우드 설정 (선택)

```bash
cp .env.example .env
# .env를 편집하여 API 키를 추가
```

API 키 발급: [atlascloud.ai](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

---

## 🆓 무료 로컬 도구

### 얼굴 교체 (`scripts/face-swap.py`)

**InsightFace** (inswapper_128)를 사용하여 두 이미지 간 얼굴을 교체합니다. 완전한 로컬 동작.

```bash
uv run scripts/face-swap.py --source 얼굴.jpg --target 사진.jpg -o 출력.jpg
```

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--source` | 얼굴을 가져올 원본 이미지 | 필수 |
| `--target` | 얼굴을 교체할 대상 이미지 | 필수 |
| `-o, --output` | 출력 파일 경로 | `./output/<target>_swapped.png` |
| `--face-index` | 단체 사진에서 교체할 얼굴 번호 (0부터 시작) | `0` |

### 얼굴 화질 향상 (`scripts/face-enhance.py`)

**Real-ESRGAN** (NCNN 백엔드)으로 얼굴 및 이미지 품질을 향상시킵니다.

```bash
uv run scripts/face-enhance.py 입력.jpg -o 출력/
```

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `input` | 입력 이미지 또는 폴더 | 필수 |
| `-o, --output` | 출력 디렉토리 | `./output/` |
| `--mode` | `enhance` (디테일 향상) / `upscale` (4배 확대) | `enhance` |
| `--sharpness` | 선명도 계수 (1.0 = 변경 없음) | `1.3` |
| `--contrast` | 대비 계수 (1.0 = 변경 없음) | `1.1` |
| `--gpu` | GPU ID (-1이면 CPU 전용) | `0` |

---

## ☁️ 클라우드 기능 (선택)

[Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) API 키가 필요합니다.

### 클라우드 얼굴 교체

```bash
uv run scripts/cloud-generate.py swap 소스.jpg 타겟.jpg -o 출력/
```

### AI 초상화 생성

```bash
uv run scripts/cloud-generate.py generate "전문적인 프로필 사진, 스튜디오 조명" \
  --model black-forest-labs/flux-2-pro
```

---

## 💰 유료 앱과 가격 비교

| 앱 | 가격 | 기능 |
|----|------|------|
| **이 도구 (로컬)** | **무료** | 얼굴 교체 + 화질 향상, 무제한 |
| FaceApp | $4.99/월 | 얼굴 교체, 필터 |
| Reface | $12.99/월 | 얼굴 교체, GIF |
| DeepSwap | $9.99/월 | 얼굴 교체, 동영상 |
| FaceMagic | $5.99/월 | 얼굴 교체 |

---

## 🌐 관련 오픈소스 도구

| 도구 | Stars | 특징 | 링크 |
|------|-------|------|------|
| **Deep-Live-Cam** | 80k+ | 실시간 웹캠 얼굴 교체 | [GitHub](https://github.com/hacksider/Deep-Live-Cam) |
| **InsightFace** | 28k+ | 핵심 얼굴 분석 라이브러리 | [GitHub](https://github.com/deepinsight/insightface) |
| **FaceFusion** | 27k+ | roop 후속작, Web GUI | [GitHub](https://github.com/facefusion/facefusion) |
| **Rope** | 5.3k+ | GUI 얼굴 교체 도구 | [GitHub](https://github.com/Hillobar/Rope) |
| **VisoMaster** | 1.8k+ | 최신 SOTA, VR180 지원 | [GitHub](https://github.com/visomaster/VisoMaster) |

---

## ❓ FAQ

**GPU가 필요한가요?** 아니요. 로컬 얼굴 교체는 ONNX Runtime을 통해 CPU에서 동작합니다. `--gpu -1`로 CPU 모드를 강제할 수 있습니다.

**오프라인에서 사용 가능한가요?** 네. 첫 실행 시 모델 다운로드 후 (약 270MB), 오프라인에서 동작합니다.

**지원하는 이미지 형식은?** JPG, JPEG, PNG, WebP, BMP, TIFF. 출력은 기본적으로 PNG입니다.

**단체 사진에서 특정 얼굴만 교체할 수 있나요?** 네. `--face-index`로 교체할 얼굴을 지정할 수 있습니다.

---

## 📄 라이선스

[MIT](LICENSE)

---

이 도구가 도움이 되셨다면 Star를 눌러주세요!

[![Star History](https://img.shields.io/github/stars/ristponex/ai-face-swap-alternative-skill?style=social)](https://github.com/ristponex/ai-face-swap-alternative-skill)
