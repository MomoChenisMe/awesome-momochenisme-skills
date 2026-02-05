# Awesome MomoChenIsMe Skills

專為 Claude Code 設計的技能集合，提升生產力與內容創作效率。

## 技能總覽

| 技能 | 說明 |
|------|------|
| **Sync Scribe** | 筆記與待辦事項管理 |
| **MomoChenIsMe Writing Style** | 部落格寫作風格指南 |

---

## Sync Scribe

簡化的筆記與待辦事項管理技能。

### 功能特色

- 🎯 **自動分類**：自動判斷輸入是待辦事項（Todo）還是記事（Note）
- ✅ **待辦管理**：新增、完成與刪除待辦事項
- 📝 **分類記事**：自動將想法歸類至「工作」、「生活」或「未分類」
- 🔍 **搜尋篩選**：依關鍵字或分類尋找項目

### 使用方式

#### 斜線指令 (Commands)

| 指令 | 說明 |
|------|------|
| `/add-todo <任務內容>` | 新增一個待辦事項 |
| `/complete-todo <關鍵字>` | 標記該事項為已完成 |
| `/list-todos [篩選條件]` | 列出所有待辦事項 |
| `/delete-todo <關鍵字>` | 刪除待辦事項 |
| `/add-note <記事內容>` | 新增一則筆記（自動分類） |
| `/list-notes [分類\|關鍵字]` | 列出筆記 |
| `/delete-note <關鍵字>` | 刪除筆記 |

#### 自然語言 (Skill)

直接對 Claude 說：
- 「幫我記得買咖啡」 → 自動加入待辦
- 「記一下：這杯咖啡很好喝」 → 自動加入筆記
- 「買咖啡完成了」 → 自動標記完成

### 資料儲存

- `TODOS.md`：存放待辦事項
- `NOTES.md`：存放分類記事

檔案儲存於工作目錄根目錄。

---

## MomoChenIsMe Writing Style

模仿 MomoChenIsMe 部落格作者的獨特寫作風格，撰寫各類文章的技能。

### 功能特色

- 🗣️ **親切口語化**：使用對話式語氣，像朋友聊天一樣
- 😄 **幽默自嘲**：適度加入輕鬆幽默元素，常用「XD」
- 🎯 **實踐導向**：強調「如何做」而非空談理論
- 🌏 **語言風格**：繁體中文為主，保留英文技術術語

### 適用文章類型

- **技術教學**：循序漸進的步驟說明，配合截圖與程式碼區塊
- **產品推廣**：工具介紹搭配誠實的優缺點分析
- **個人心得**：經驗分享與學到的教訓
- **年度回顧**：時間線式的回顧與展望

### 使用方式

自然語言觸發，例如：
- 「用 MomoChenIsMe 的風格寫一篇關於 Docker 的教學」
- 「幫我用 MomoChenIsMe 風格介紹這個工具」
- 「以 MomoChenIsMe 的口吻寫年度回顧」

### 風格特色

| 元素 | 用途 |
|------|------|
| 💡 | 重要提示、補充說明、限制條件 |
| ✨ | 強調特別重要或令人興奮的內容 |
| XD | 幽默、自嘲或輕鬆語氣 |
| 「」 | 專有名詞、重點概念 |
| **粗體** | 強調關鍵字詞 |

---

## 安裝方式

```bash
# 本地開發測試
claude --plugin-dir ./
```

## 檔案結構

```
awesome-momo-skills/
├── README.md
├── README_zh.md
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── add-todo.md
│   ├── complete-todo.md
│   ├── list-todos.md
│   ├── delete-todo.md
│   ├── add-note.md
│   ├── list-notes.md
│   └── delete-note.md
└── skills/
    ├── sync-scribe/
    │   └── SKILL.md
    └── momo-writing-style/
        ├── SKILL.md
        └── references/
            └── style-examples.md
```

## 授權

MIT License
