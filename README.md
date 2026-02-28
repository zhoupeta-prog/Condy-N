# 🦞 OpenClaw 懶人包安裝器

> 一鍵安裝 OpenClaw，完整中文化界面，新手友善！  
> **完全免費開源** 🎁

## ✨ 功能特色

- 🚀 **一鍵自動安裝** - 全自動檢測環境、安裝依賴、配置 OpenClaw
- 🌐 **全中文介面** - 完整中文化輸出，告別英文錯誤訊息
- ⚡ **智能環境修復** - 自動檢測並修復 Node.js、npm 等依賴
- 🔧 **互動配置嚮導** - 引導式設定 API Keys、Gateway、Channels
- 💡 **免費 LLM 推薦** - 安裝後自動推薦免費/試用 API 平台（Groq、Moonshot 等）
- 🛠️ **Skills 推薦** - 推薦必裝的免費 Skills（天氣、提醒、筆記等）
- 📱 **手機連接指南** - 詳細教學如何連結 Telegram/Discord
- 🎨 **精美 TUI 介面** - 使用 Rich 打造現代化終端界面

## 🚀 快速開始

### 🍎 macOS 用戶（最簡單）

**下載執行檔，雙擊即用**

1. 從 **[Releases 頁面](https://github.com/zhoupeta-prog/Condy-N/releases/latest)** 下載 `OpenClaw-Installer-macOS.zip`
2. 解壓縮，雙擊「**啟動安裝器.command**」
3. 按照畫面提示完成安裝

> ⚠️ 第一次運行可能需要按住 `Control` 鍵點擊，選擇「打開」

**📖 詳細教學：** [QUICK_START.md](QUICK_START.md) - 純文字步驟指南，零基礎也能懂！

**直接下載連結：**
```
https://github.com/zhoupeta-prog/Condy-N/releases/download/v0.1.0/OpenClaw-Installer-macOS.zip
```

---

### 💻 Linux / WSL2 / 其他

**方式一：一鍵腳本**

```bash
curl -fsSL https://raw.githubusercontent.com/zhoupeta-prog/Condy-N/main/install-openclaw-easy.sh | bash
```

**方式二：Python 腳本**

```bash
# 下載
curl -O https://raw.githubusercontent.com/zhoupeta-prog/Condy-N/main/openclaw_easy_installer.py

# 執行
python3 openclaw_easy_installer.py
```

## 📋 系統需求

- **macOS**: 10.15+ (Catalina 或更新)
- **Linux**: Ubuntu 18.04+, Debian 10+, CentOS 8+
- **Windows**: Windows 10/11 + WSL2
- **Python**: 3.8+ (腳本方式)
- **網路**: 可連接 openclaw.ai

## 🛠️ 安裝流程

安裝器會自動完成以下步驟：

1. ✅ 檢測系統環境（Node.js、npm、curl）
2. ✅ 自動安裝/升級 Node.js 22+
3. ✅ 下載並安裝 OpenClaw CLI
4. ✅ 運行互動式配置嚮導
5. ✅ 驗證安裝並顯示後續步驟

## 📖 使用範例

```
$ ./openclaw-installer

🦞 =========================================
   OpenClaw 懶人包安裝器
   讓安裝變得簡單，讓 AI 觸手可及
 =========================================

📊 系統環境檢測
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ 項目         ┃ 狀態        ┃ 版本/資訊   ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 作業系統     │ ✅          │ Darwin 23.x │
│ Node.js      │ ❌ 未安裝   │ 將自動安裝  │
│ npm          │ ❌ 未安裝   │ 將隨 Node … │
│ OpenClaw     │ ⏳ 待安裝   │ 即將開始    │
└──────────────┴─────────────┴─────────────┘

📦 正在安裝 Node.js...
✅ Node.js 安裝完成！
```

## 👩‍💻 關於作者

**Condy N.** - 熱愛簡化複雜事情的開發者 🐙

> 「讓技術觸手可及，讓每個人都能輕鬆使用 AI。」

- 🦞 OpenClaw 愛好者與貢獻者
- 🌏 致力於中文化開發者工具
- 💡 相信好的工具應該簡單易用

歡迎關注我的其他作品！

## 💰 贊助支持

這個工具完全免費使用！

如果你覺得有幫助，可以考慮贊助一杯咖啡 ☕：

| 方式 | 連結 |
|------|------|
| 加密貨幣 | [贊助地址] |
| 微信支付 | [QR Code] |

你的支持讓我能持續創作更多好用的工具 💜

## 📄 授權

MIT License - 詳見 [LICENSE](LICENSE) 檔案

## 🤝 貢獻

歡迎提交 Issue 和 PR！

## 🙏 致謝

- [OpenClaw](https://openclaw.ai) - 優秀的 AI 助手平台
- [Rich](https://github.com/Textualize/rich) - 漂亮的終端 UI 函式庫

---

Made with ❤️ by Condy N. 🐙
