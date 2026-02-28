#!/bin/bash
# 構建腳本 - 將 Python 腳本打包成可執行檔

set -e

echo "🦞 OpenClaw 懶人包安裝器 - 構建腳本"
echo "======================================"

# 檢查環境
echo "📋 檢查構建環境..."

if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3"
    exit 1
fi

# 創建虛擬環境
echo "📦 創建虛擬環境..."
python3 -m venv build_env
source build_env/bin/activate

# 安裝依賴
echo "📥 安裝依賴..."
pip install -q --upgrade pip
pip install -q pyinstaller rich typer

# 構建可執行檔
echo "🔨 構建可執行檔..."
pyinstaller \
    --onefile \
    --name "openclaw-installer" \
    --add-data "README.md:." \
    --clean \
    --noconfirm \
    openclaw_easy_installer.py

# 移動輸出檔案
echo "📁 整理輸出..."
mkdir -p dist
cp dist/openclaw-installer dist/openclaw-installer-$(uname -s)-$(uname -m)

echo ""
echo "✅ 構建完成！"
echo ""
echo "輸出檔案:"
echo "  - dist/openclaw-installer (單一可執行檔)"
echo ""
echo "測試運行:"
echo "  ./dist/openclaw-installer"
echo ""

# 清理
deactivate
rm -rf build_env build

echo "🎉 完成！"
