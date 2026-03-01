#!/bin/bash
# OpenClaw 懶人包安裝器 - 一鍵安裝腳本
# 作者：Condy N. 🐙
# 使用方法: curl -fsSL https://raw.githubusercontent.com/zhoupeta-prog/Condy-N/main/install-openclaw-easy.sh | bash

set -e

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# VoiceOver 提示音函數
vo_alert() {
    # 嘗試播放提示音（靜音失敗也沒關係）
    afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true
}

vo_success() {
    afplay /System/Library/Sounds/Hero.aiff 2>/dev/null || true
}

vo_error() {
    afplay /System/Library/Sounds/Basso.aiff 2>/dev/null || true
}

# 打印標題
print_banner() {
    echo ""
    echo -e "${CYAN}🦞 =========================================${NC}"
    echo -e "${CYAN}   OpenClaw 懶人包安裝器${NC}"
    echo -e "${CYAN}   讓安裝變得簡單，讓 AI 觸手可及${NC}"
    echo -e "${CYAN} =========================================${NC}"
    echo ""
}

# 檢查 Python
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ 未檢測到 Python，請先安裝 Python 3.8+${NC}"
        echo -e "${YELLOW}💡 macOS: brew install python3${NC}"
        echo -e "${YELLOW}💡 Ubuntu/Debian: sudo apt install python3${NC}"
        exit 1
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✅ Python 已安裝: $PYTHON_VERSION${NC}"
}

# 下載並運行安裝器
download_and_run() {
    INSTALLER_URL="https://raw.githubusercontent.com/zhoupeta-prog/Condy-N/main/openclaw_easy_installer.py"
    TEMP_DIR=$(mktemp -d)
    INSTALLER_PATH="$TEMP_DIR/openclaw_easy_installer.py"
    
    echo -e "${BLUE}📥 下載安裝器...${NC}"
    
    if command -v curl &> /dev/null; then
        curl -fsSL "$INSTALLER_URL" -o "$INSTALLER_PATH" 2>/dev/null || {
            echo -e "${YELLOW}⚠️ 無法下載最新版本，使用內建版本...${NC}"
            # 內建精簡版本
            cat > "$INSTALLER_PATH" << 'PYTHON_SCRIPT'
#!/usr/bin/env python3
# 精簡版安裝器
import os, sys, subprocess, platform, shutil

def run_cmd(cmd, timeout=60):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return result.returncode == 0, result.stdout, result.stderr

def main():
    print("🦞 OpenClaw 快速安裝")
    print("=" * 40)
    
    # 檢查 Node
    node_ok, node_ver, _ = run_cmd("node --version")
    if node_ok:
        print(f"✅ Node.js: {node_ver.strip()}")
    else:
        print("📦 正在安裝 Node.js...")
        if platform.system() == "Darwin":
            if shutil.which("brew"):
                run_cmd("brew install node@22", 120)
            else:
                print("請先安裝 Homebrew: https://brew.sh")
                return
        else:
            run_cmd("curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt-get install -y nodejs", 180)
    
    # 安裝 OpenClaw
    print("🦞 安裝 OpenClaw...")
    success, _, err = run_cmd("curl -fsSL https://openclaw.ai/install.sh | bash", 120)
    if success:
        print("✅ OpenClaw 安裝完成！")
        print("\n🚀 接下來請運行: openclaw configure")
        print("📱 或開啟控制台: openclaw dashboard")
    else:
        print(f"❌ 安裝失敗: {err}")

if __name__ == "__main__":
    main()
PYTHON_SCRIPT
        }
    else
        echo -e "${RED}❌ 需要 curl 來下載安裝器${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ 安裝器已下載${NC}"
    echo ""
    
    # 運行安裝器
    chmod +x "$INSTALLER_PATH"
    $PYTHON_CMD "$INSTALLER_PATH"
    
    # 清理
    rm -rf "$TEMP_DIR"
}

# 主程序
main() {
    print_banner
    
    # VoiceOver 開場提示
    echo ""
    echo -e "${CYAN}♿ VoiceOver 使用者: 按 Command + F5 啟用語音導航${NC}"
    echo -e "${CYAN}   安裝過程會自動朗讀每個步驟${NC}"
    echo ""
    sleep 2
    
    check_python
    echo ""
    download_and_run
    
    # 完成提示
    vo_success
}

main "$@"
