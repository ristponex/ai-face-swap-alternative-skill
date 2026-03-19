# 🔄 AI 顔交換の代替ツール — 無料・オープンソース

**無料ローカル顔交換 (InsightFace) + AI 画質向上 (Real-ESRGAN) + クラウド AI 生成 (Atlas Cloud)**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)](https://docs.astral.sh/uv/)
[![Atlas Cloud](https://img.shields.io/badge/Atlas%20Cloud-API-orange)](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

---

## ✨ このツールの特徴

- 🆓 **100% 無料のローカル顔交換** — API キー不要、クラウド不要、コストゼロ
- 🔒 **プライバシー保護** — すべての処理はローカルで完結、画像はアップロードされません
- ⚡ **ワンコマンド** — `uv run` で実行、依存関係は自動インストール
- 🎭 **高品質** — InsightFace (inswapper_128) + Real-ESRGAN による強化
- ☁️ **オプションのクラウド機能** — API 顔交換 + AI ポートレート生成
- 🤖 **AI エージェント対応** — Claude Code、Cursor、Windsurf などと連携
- 💰 **節約** — FaceApp ($4.99/月)、Reface ($12.99/月)、DeepSwap ($9.99/月) の無料代替

---

## 📦 インストール

### 1. スキルの追加

```bash
npx skills add ristponex/ai-face-swap-alternative-skill
```

### 2. 前提条件

- **Python 3.10 - 3.12** (3.13 は一部の依存関係で未サポート)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python パッケージマネージャー

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. クラウド設定（任意）

```bash
cp .env.example .env
# .env を編集して API キーを追加
```

API キーの取得: [atlascloud.ai](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill)

---

## 🆓 無料ローカルツール

### 顔交換 (`scripts/face-swap.py`)

**InsightFace** (inswapper_128) を使用して2枚の画像間で顔を交換します。完全ローカル動作。

```bash
uv run scripts/face-swap.py --source 顔.jpg --target 写真.jpg -o 出力.jpg
```

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--source` | 顔の元画像 | 必須 |
| `--target` | 顔を置換する対象画像 | 必須 |
| `-o, --output` | 出力ファイルパス | `./output/<target>_swapped.png` |
| `--face-index` | 集合写真で何番目の顔を交換するか（0始まり） | `0` |

### 顔の高画質化 (`scripts/face-enhance.py`)

**Real-ESRGAN** (NCNN バックエンド) で顔や画像の品質を向上させます。

```bash
uv run scripts/face-enhance.py 入力.jpg -o 出力/
```

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `input` | 入力画像またはフォルダ | 必須 |
| `-o, --output` | 出力ディレクトリ | `./output/` |
| `--mode` | `enhance` (ディテール向上) / `upscale` (4倍拡大) | `enhance` |
| `--sharpness` | シャープネス係数 (1.0 = 変更なし) | `1.3` |
| `--contrast` | コントラスト係数 (1.0 = 変更なし) | `1.1` |
| `--gpu` | GPU ID (-1 で CPU のみ) | `0` |

---

## ☁️ クラウド機能（任意）

[Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=ai-face-swap-alternative-skill) の API キーが必要です。

### クラウド顔交換

```bash
uv run scripts/cloud-generate.py swap ソース.jpg ターゲット.jpg -o 出力/
```

### AI ポートレート生成

```bash
uv run scripts/cloud-generate.py generate "プロフェッショナルなヘッドショット" \
  --model black-forest-labs/flux-2-pro
```

---

## 💰 有料アプリとの価格比較

| アプリ | 料金 | 機能 |
|--------|------|------|
| **このツール（ローカル）** | **無料** | 顔交換 + 画質向上、無制限 |
| FaceApp | $4.99/月 | 顔交換、フィルター |
| Reface | $12.99/月 | 顔交換、GIF |
| DeepSwap | $9.99/月 | 顔交換、動画 |
| FaceMagic | $5.99/月 | 顔交換 |

---

## 🌐 関連オープンソースツール

| ツール | Stars | 特徴 | リンク |
|--------|-------|------|--------|
| **Deep-Live-Cam** | 80k+ | リアルタイムウェブカメラ顔交換 | [GitHub](https://github.com/hacksider/Deep-Live-Cam) |
| **InsightFace** | 28k+ | コア顔分析ライブラリ | [GitHub](https://github.com/deepinsight/insightface) |
| **FaceFusion** | 27k+ | roop 後継、Web GUI | [GitHub](https://github.com/facefusion/facefusion) |
| **Rope** | 5.3k+ | GUI 顔交換ツール | [GitHub](https://github.com/Hillobar/Rope) |
| **VisoMaster** | 1.8k+ | 最新 SOTA、VR180 対応 | [GitHub](https://github.com/visomaster/VisoMaster) |

---

## ❓ FAQ

**GPU は必要ですか？** いいえ。ローカル顔交換は CPU 上の ONNX Runtime で動作します。`--gpu -1` で CPU モードを強制できます。

**オフラインで使えますか？** はい。初回実行時にモデルをダウンロード後（約 270MB）、オフラインで動作します。

**対応画像形式は？** JPG、JPEG、PNG、WebP、BMP、TIFF。出力はデフォルトで PNG です。

**集合写真で特定の顔だけ交換できますか？** はい。`--face-index` で交換する顔を指定できます。

---

## 📄 ライセンス

[MIT](LICENSE)

---

このツールが役に立ったら、Star をお願いします！

[![Star History](https://img.shields.io/github/stars/ristponex/ai-face-swap-alternative-skill?style=social)](https://github.com/ristponex/ai-face-swap-alternative-skill)
