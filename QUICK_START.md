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

## 💡 步驟 6：沒有 API Key？免費方案在這裡！

### 🆓 免費 LLM 平台（推薦）

#### Groq（完全免費，速度快）
```
1. 前往 https://console.groq.com
2. 註冊帳號（免費）
3. 創建 API Key
4. 運行: openclaw configure
5. 選擇 Groq 作為模型提供者

✅ 優點：免費額度充足，支援 Llama 3、Mixtral
```

#### Moonshot（適合中文）
```
1. 前往 https://platform.moonshot.cn
2. 手機註冊（送免費額度）
3. 創建 API Key
4. 運行: openclaw configure

✅ 優點：中文表現好，適合台灣/香港/大陸用戶
```

#### Together AI（新用戶送 $5）
```
1. 前往 https://api.together.xyz
2. 註冊帳號
3. 獲得 $5 免費額度
4. 配置到 OpenClaw
```

---

## 🛠️ 步驟 7：安裝推薦的免費 Skills

### 必裝清單（完全免費）

```bash
# 🌤️ 天氣查詢（免費 API）
openclaw skills install weather

# 📝 提醒事項（連接 Apple Reminders）
openclaw skills install reminders

# 📓 Apple 筆記（macOS 用戶）
openclaw skills install apple-notes

# 🎬 影片截圖
openclaw skills install video-frames

# 📄 PDF 編輯
openclaw skills install nano-pdf
```

### 查看已安裝 Skills
```
openclaw skills list
```

---

## 📱 步驟 8：與手機連結

### Telegram（推薦）
```
📲 設定步驟：

1. 下載 Telegram App
2. 搜尋 @BotFather
3. 輸入 /newbot 創建機器人
4. 取得 Bot Token（像這樣：123456789:ABCdefGHI...）
5. 在電腦運行：
   openclaw channels telegram setup
6. 貼上 Bot Token
7. 完成！在手機 Telegram 搜尋你的機器人名稱

✅ 現在你可以在手機上隨時隨地聊天！
```

### Discord
```
📲 設定步驟：

1. 前往 https://discord.com/developers/applications
2. 點擊 "New Application"
3. 到 "Bot" 頁面，點擊 "Add Bot"
4. 取得 Bot Token
5. 在電腦運行：
   openclaw channels discord setup
6. 貼上 Token
7. 生成邀請連結，將 Bot 加入你的伺服器

✅ 現在可以在 Discord 上使用！
```

---

## 🎉 步驟 9：開始使用！

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

🛠️ 查看 Skills
   openclaw skills list
```

### 第一次使用
```
1. 在 Terminal 輸入：openclaw dashboard
2. 瀏覽器自動打開控制面板
3. 開始和你的 AI 助手對話！💬

💡 提示：你可以問「今天天氣怎麼樣？」
       如果你裝了 weather skill！
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
