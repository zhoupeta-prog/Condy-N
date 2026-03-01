# 📋 OpenClaw 懶人包安裝器 SOP

## 標準作業程序 - 含 macOS VoiceOver 無障礙支援

---

## 🎯 目的

確保所有使用者（含視覺障礙使用者）能順利安裝 OpenClaw。

---

## 📦 安裝包內容標準

### 必含檔案
```
OpenClaw-Installer-macOS/
├── 🚀 啟動安裝器.command       # 主啟動腳本
├── ⚙️  OpenClaw-Installer      # 圖形化安裝器（如適用）
├── 📖 使用說明.txt              # 純文字說明
├── ♿  VOICEOVER_README.txt     # VoiceOver 專用指南 ⭐
└── 📋 SOP.txt                   # 本文件
```

---

## ♿ VoiceOver 無障礙設計規範

### 1. 檔案命名原則
- ✅ 使用有意義的名稱：`啟動安裝器.command`
- ❌ 避免：`run.sh`, `install.sh`

### 2. Terminal 輸出設計
```bash
# ✅ 好的做法 - 有清晰的標記和分隔線
echo "🦞 ======================================="
echo "   OpenClaw 懶人包安裝器"
echo "   讓安裝變得簡單"
echo " ======================================="
echo ""

# ✅ 每個步驟都有朗讀提示
echo "📦 步驟 1: 檢查系統環境"
echo "✅ 系統檢查完成"
echo ""
echo "📦 步驟 2: 安裝 Node.js"
echo "⏳ 請稍候，這可能需要 2-3 分鐘"

# ✅ 完成時有提示音
afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true
echo "🎉 安裝完成！"
```

### 3. 鍵盤導航支援
| 快速鍵 | 功能 | 說明 |
|--------|------|------|
| `Tab` | 切換焦點 | 在所有可互動元素間切換 |
| `Space` | 點擊 | 啟動按鈕或選項 |
| `↑/↓` | 選擇 | 在列表中移動 |
| `Enter` | 確認 | 提交輸入或選擇 |
| `Esc` | 取消 | 關閉對話框 |

### 4. VoiceOver 快速鍵參考
```
基本導航：
  Control + Option + →      下一個項目
  Control + Option + ←      上一個項目
  Control + Option + ↑      上一行
  Control + Option + ↓      下一行

互動：
  Control + Option + Space  點擊/確認
  Control + Option + I      項目概覽
  Control + Option + L      朗讀當前行

系統：
  Command + F5              啟用/停用 VoiceOver
  Option + 連按三下 Touch ID  啟用/停用 VoiceOver（MacBook）
```

---

## 🧪 測試檢查清單

### 每次發布前必須測試

#### 1. 一般使用者測試
- [ ] 雙擊 ZIP 可正常解壓
- [ ] Control+點擊可打開 `.command` 檔案
- [ ] 安裝過程無需手動輸入指令
- [ ] 安裝完成後可正常運行 `openclaw`

#### 2. VoiceOver 測試 ⭐
- [ ] 啟用 VoiceOver (Cmd+F5)
- [ ] 可聽到所有 Terminal 輸出
- [ ] 可透過鍵盤完成整個安裝流程
- [ ] 安裝完成提示清晰可聽

#### 3. 輔助功能測試
- [ ] 字體大小適中（可縮放）
- [ ] 色彩對比度足夠
- [ ] 所有功能可用鍵盤操作

---

## 📚 文件維護

### QUICK_START.md
- 位置：`/docs/QUICK_START.md`
- 更新時機：每次 UI 變更
- 必含章節：VoiceOver 使用者指南

### VOICEOVER_README.txt
- 位置：安裝包根目錄
- 格式：純文字（無 Markdown）
- 內容：簡潔的 VoiceOver 快速指引

### SOP.txt
- 位置：安裝包根目錄
- 用途：內部開發參考
- 更新：每次發布前檢視

---

## 🔧 開發者注意事項

### 新增功能時必須檢查
1. **可聽性**：Terminal 輸出是否有意義？
2. **可導航**：是否可用 Tab/方向鍵操作？
3. **可理解**：錯誤訊息是否清楚？

### Terminal 輸出範本
```bash
# 開始步驟
echo "📦 步驟 X: [步驟名稱]"

# 進行中
echo "⏳ [操作說明]..."

# 成功
echo "✅ [步驟名稱] 完成！"

# 錯誤
echo "❌ [錯誤說明]"
echo "💡 建議: [解決方案]"

# 分隔線
echo ""
echo "─────────────────────────────"
echo ""
```

---

## 🆘 疑難排解

### VoiceOver 無法朗讀 Terminal
**問題**：VoiceOver 不朗讀 Terminal 輸出

**解決**：
1. 確保 Terminal 是活動視窗
2. 按 `Control + Option + M` 切換朗讀模式
3. 或嘗試使用 iTerm2（VoiceOver 相容性更好）

### 安裝器無法打開
**問題**：「無法打開，因為它來自未識別的開發者」

**一般使用者解決**：
```
1. 按住 Control 鍵
2. 點擊「啟動安裝器.command」
3. 選擇「打開」
4. 點擊「仍要打開」
```

**VoiceOver 使用者解決**：
```
1. 選中檔案
2. 按 Control + Option + Shift + M（打開選單）
3. 選擇「打開」
4. 按 Control + Option + Space 確認「仍要打開」
```

---

## 📞 支援聯絡

| 問題類型 | 聯絡方式 |
|---------|---------|
| 安裝問題 | GitHub Issues |
| 無障礙問題 | 標記 `accessibility` |
| 功能建議 | Discussions |

---

## 📝 版本記錄

| 版本 | 日期 | 變更 |
|-----|------|------|
| 1.0 | 2026-03-01 | 初始版本，含 VoiceOver 支援 |

---

**製作：Condy N.** 🐙  
*技術為人人服務*
