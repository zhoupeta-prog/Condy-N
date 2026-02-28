# 🚀 OpenClaw 快速上手指南（文字版）

> 💡 零圖片也能懂！用 emoji 和符號帶你 3 分鐘完成安裝

---

## 📥 步驟 1：下載

### 前往 Releases 頁面
```
🔗 https://github.com/zhoupeta-prog/Condy-N/releases
```

### 找到這個檔案 👇
```
┌─────────────────────────────────────┐
│  ⬇️  OpenClaw-Installer-macOS.zip  │  ← 🔴 點這個！
│       5.7 MB                        │
└─────────────────────────────────────┘
```

💾 **檔案會下載到「下載」資料夾**

---

## 📂 步驟 2：解壓縮

### 雙擊 ZIP 檔
```
📦 OpenClaw-Installer-macOS.zip
        ↓
📁 OpenClaw-Installer-macOS/
```

### 打開資料夾會看到 👇
```
📁 OpenClaw-Installer-macOS/
├── 🚀 啟動安裝器.command     ← 🔴 步驟 3 點這個！
├── ⚙️  OpenClaw-Installer
└── 📖 使用說明.txt
```

---

## ⚠️ 步驟 3：首次運行（重要！）

### 你會看到這個警告
```
┌─────────────────────────────────────────┐
│  ⚠️  無法打開「啟動安裝器.command」      │
│                                         │
│  因為它來自未識別的開發者。              │
│                                         │
│         ┌─────────┐                     │
│         │   好    │  ← ❌ 不要按這個    │
│         └─────────┘                     │
└─────────────────────────────────────────┘
```

### ✅ 正確做法
```
步驟：
1️⃣  按住 Control 鍵不放
2️⃣  點擊「啟動安裝器.command」
3️⃣  選擇「打開」
4️⃣  點擊「仍要打開」

🎉 成功！Terminal 視窗會打開
```

---

## 🦞 步驟 4：自動安裝

### 你會看到這個畫面
```
🦞 ═══════════════════════════════════════
   OpenClaw 懶人包安裝器
   讓安裝變得簡單，讓 AI 觸手可及
═══════════════════════════════════════

📊 系統環境檢測
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ 項目         ┃ 狀態        ┃ 版本    ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━┩
│ 作業系統     │ ✅          │ macOS   │
│ Node.js      │ ❌ 未安裝   │ 將安裝  │  ← 正常！
│ npm          │ ❌ 未安裝   │ 將安裝  │  ← 正常！
│ OpenClaw     │ ⏳ 待安裝   │ 即將    │  ← 正常！
└──────────────┴─────────────┴─────────┘

📦 正在安裝 Node.js...
⏳ 請稍候，這可能需要 2-3 分鐘

✅ Node.js 安裝完成！
✅ OpenClaw 安裝完成！
```

💡 **完全自動！不需要輸入任何指令！**

---

## ⚙️ 步驟 5：配置 OpenClaw

### 安裝完成後會問你
```
⚙️ ═══════════════════════════════════════
   現在開始配置 OpenClaw
═══════════════════════════════════════

接下來會引導你完成：
• API 金鑰設定（Moonshot/OpenAI 等）
• Gateway 服務配置
• 聊天頻道連接（選擇性）

是否開始配置嚮導？ [Y/n]
```

### 輸入 Y 繼續
```
Y ↵

📝 請輸入你的 API Key: 
[輸入後按 Enter]

✅ 配置完成！
```

---

## 🎉 步驟 6：完成！開始使用

### 常用指令
```
🚀 開啟控制面板（推薦新手）
   openclaw dashboard
   
   會自動打開瀏覽器：
   🌐 http://127.0.0.1:18789/

⚡ 啟動 Gateway 服務
   openclaw gateway start

❓ 查看所有指令
   openclaw --help
```

### 第一次使用
```
1. 在 Terminal 輸入：openclaw dashboard
2. 瀏覽器自動打開控制面板
3. 開始和你的 AI 助手對話！💬
```

---

## ❓ 常見問題

### Q: 安裝到一半卡住？
```
✅ 檢查網路連線
✅ 耐心等待（Node.js 安裝約需 2-3 分鐘）
✅ 不要關閉 Terminal 視窗
```

### Q: 忘記 API Key 怎麼辦？
```
🔄 重新運行配置：
   openclaw configure
   
或編輯設定檔：
   openclaw config set openai.key "你的key"
```

### Q: 如何連接 Telegram/Discord？
```
📱 Telegram:
   openclaw channels telegram setup

💬 Discord:
   openclaw channels discord setup

📖 詳細教學：
   https://docs.openclaw.ai/channels
```

---

## 🆘 需要幫助？

| 問題類型 | 聯絡方式 |
|---------|---------|
| 安裝問題 | 開 [GitHub Issue](https://github.com/zhoupeta-prog/Condy-N/issues) |
| 使用問題 | 查閱 [OpenClaw 官方文件](https://docs.openclaw.ai) |
| 功能建議 | 在 GitHub 留言或私訊我 |

---

## 🎯 快速回顧

```
📥 下載 ZIP → 📂 解壓縮 → ⚠️ Control+點擊打開 
    → 🦞 自動安裝 → ⚙️ 配置 → 🎉 完成！
    
⏱️ 總時間：約 5-10 分鐘
🧠 難度：⭐☆☆☆☆（超簡單）
```

---

**製作：Condy N.** 🐙  
*讓技術觸手可及*
