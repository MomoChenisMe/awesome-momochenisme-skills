# Awesome MomoChenIsMe Skills

專為 Claude Code 設計的技能集合，提升生產力、內容創作與開發工作流程效率。

## 技能總覽

| 技能 | 說明 |
|------|------|
| **Sync Scribe** | 筆記與待辦事項管理 |
| **MomoChenIsMe Writing Style** | 部落格寫作風格指南（繁體中文）|
| **Conventional Commit** | 遵循 Conventional Commits v1.0.0 規範的 Git commit 訊息撰寫 |
| **UI/UX Pro Max** | 全方位 UI/UX 設計智慧工具 |
| **Skill Creator** | Claude Code 技能開發指南 |
| **Plugin Creator** | Claude Code 插件開發指南 |
| **Claude Code CLI Guide** | Claude Code CLI 完整使用參考 |
| **OpenSpec Workflow** | 以規格驅動的開發工作流程方法論與決策框架 |
| **Gemini CLI Guide** | Gemini CLI 完整使用參考 |

---

## Sync Scribe

簡化的筆記與待辦事項管理技能。

### 功能特色

- **自動分類**：自動判斷輸入是待辦事項（Todo）還是記事（Note）
- **待辦管理**：新增、完成與刪除待辦事項
- **分類記事**：自動將想法歸類至「工作」、「生活」或「未分類」
- **搜尋篩選**：依關鍵字或分類尋找項目

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

- **親切口語化**：使用對話式語氣，像朋友聊天一樣
- **幽默自嘲**：適度加入輕鬆幽默元素，常用「XD」
- **實踐導向**：強調「如何做」而非空談理論
- **語言風格**：繁體中文為主，保留英文技術術語

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
| **粗體** | 強調關鍵字詞 |
| `Code` | 技術術語與命令 |
| > 引用 | 重要提示 |

---

## Conventional Commit

遵循 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) 規範撰寫 Git commit 訊息。

### 功能特色

- **完整規範**：涵蓋全部 16 條規則（使用 RFC 2119 關鍵字）
- **類型系統**：10 種標準類型（feat, fix, build, chore, ci, docs, style, refactor, perf, test）及 SemVer 對應
- **BREAKING CHANGE**：支援雙重機制（`!` 後綴與 footer）
- **Footer 格式**：Git trailer 慣例與常見 tokens
- **撰寫指南**：祈使語氣、72 字元限制、「說明 why 而非 what」原則
- **豐富範例**：13+ 個範例，涵蓋所有類型與情境

### Commit 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 標準類型

| 類型 | 用途 | SemVer |
| --- | --- | --- |
| `feat` | 新功能 | MINOR |
| `fix` | 錯誤修復 | PATCH |
| `build` | 建置系統 / 外部依賴 | — |
| `chore` | 維護任務 | — |
| `ci` | CI 設定 | — |
| `docs` | 僅文件變更 | — |
| `style` | 程式碼格式化（非 CSS） | — |
| `refactor` | 程式碼重構 | — |
| `perf` | 效能改善 | — |
| `test` | 測試 | — |

### 參考文件

- [specification.md](skills/conventional-commit/references/specification.md) - 完整 v1.0.0 規範、BNF 語法、SemVer 對應與 FAQ

---

## UI/UX Pro Max

> 來源：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

AI 驅動的全方位 UI/UX 設計智慧工具。

### 功能特色

- **67 種設計風格**：從極簡到粗獷主義，涵蓋所有主流設計美學
- **96 種調色盤**：產業專屬與氛圍導向的色彩系統
- **產業專屬規則**：針對不同產業量身打造的設計模式
- **無障礙合規**：整合 WCAG 指南
- **響應式設計**：行動優先與自適應佈局模式

### 使用方式

自然語言觸發，例如：

- 「設計一個 SaaS 產品的 dashboard」
- 「用現代極簡風格做一個 landing page」
- 「為健身追蹤器設計一個手機 app UI」

---

## Skill Creator

> 來源：[anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

Claude Code 技能開發的完整指南。

### 功能特色

- **技能結構**：SKILL.md 架構、frontmatter 與內文撰寫指南
- **資源打包**：Scripts、references 與 assets 的組織方式
- **漸進式載入**：三層載入系統，有效管理 context
- **最佳實踐**：精簡寫作、適當的自由度設定

### 核心概念

- **SKILL.md**：必要檔案，包含 YAML frontmatter（name、description）與 Markdown 內文
- **scripts/**：可執行程式碼，用於確定性、重複性任務
- **references/**：按需載入 context 的文件
- **assets/**：用於輸出的檔案（模板、圖片、字型）

### 工作流程

1. 透過具體範例理解技能需求
2. 規劃可重用內容（scripts、references、assets）
3. 使用 `scripts/init_skill.py` 初始化
4. 編輯 SKILL.md 並實作資源
5. 使用 `scripts/package_skill.py` 打包
6. 根據實際使用情況迭代改進

---

## Plugin Creator

Claude Code 插件開發指南 - 可分發的套件，打包技能、hooks 與 MCP servers。

### 功能特色

- **插件結構**：目錄配置與 manifest 設定
- **組件類型**：Commands、skills、hooks、MCP servers、LSP servers
- **初始化腳本**：快速建立插件骨架
- **測試指南**：本地插件載入與除錯

### 何時使用 Plugin vs 獨立檔案

| 使用情境 | 建議方式 |
|----------|----------|
| 僅限單一專案 | 放在 `.claude/` 目錄 |
| 跨專案共用 | 建立 Plugin |
| 分發給其他人 | 建立 Plugin |

### 快速開始

```bash
# 建立新插件
python skills/plugin-creator/scripts/init_plugin.py my-plugin

# 測試本地插件
claude --plugin-dir ./my-plugin
```

### 插件結構

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # Manifest（必要）
├── commands/            # 使用者可呼叫的技能
├── skills/              # Agent 技能
├── hooks/               # Hook 設定
└── README.md
```

---

## Claude Code CLI Guide

Claude Code CLI 命令與 flags 的完整參考。

### 基本命令

| 命令 | 說明 |
|------|------|
| `claude` | 啟動互動式 REPL |
| `claude "query"` | 帶初始提示啟動 REPL |
| `claude -p "query"` | 單次查詢模式（pipe/SDK 模式）|
| `claude -c` | 繼續最近的對話 |
| `claude -r <id>` | 恢復特定 session |
| `claude config` | 設定管理 |
| `claude mcp` | MCP server 設定 |
| `claude update` | 更新至最新版本 |

### 常用 Flags

| Flag | 說明 |
|------|------|
| `-p, --print` | 單次查詢模式 |
| `-c, --continue` | 繼續最近對話 |
| `--model <name>` | 指定模型（opus/sonnet/haiku）|
| `--output-format <fmt>` | 輸出格式（text/json/stream-json）|
| `--max-turns <n>` | 限制 agent 回合數 |
| `--verbose` | 詳細日誌 |

### 參考文件

- [commands.md](skills/claude-code-cli-guide/references/commands.md) - 所有命令說明
- [flags.md](skills/claude-code-cli-guide/references/flags.md) - 依類別分類的 flags
- [examples.md](skills/claude-code-cli-guide/references/examples.md) - 常見使用範例

---

## Gemini CLI Guide

Gemini CLI 命令與設定的完整參考。

### 基本命令

| 命令 | 說明 |
|------|------|
| `gemini` | 啟動互動式 REPL |
| `gemini "query"` | 帶初始提示啟動 REPL |
| `gemini -p "query"` | 單次查詢模式（pipe 模式）|

### 斜線指令

| 指令 | 說明 |
|------|------|
| `/help` | 顯示所有可用指令 |
| `/chat` | 開始新對話 |
| `/resume` | 恢復先前的對話 |
| `/save` | 儲存目前對話 |
| `/memory` | 顯示記憶狀態 |

### 常用 Flags

| Flag | 說明 |
|------|------|
| `-p, --prompt` | 單次查詢模式 |
| `-m, --model` | 指定模型 |
| `-s, --sandbox` | 啟用沙箱模式 |
| `--approval-mode` | 設定核准模式（default/auto_edit/plan/yolo）|
| `--output-format` | 輸出格式（text/json/stream-json）|
| `-d, --debug` | 啟用除錯模式 |

### 參考文件

- [commands.md](skills/gemini-cli-guide/references/commands.md) - 所有命令說明
- [flags.md](skills/gemini-cli-guide/references/flags.md) - 依類別分類的 flags
- [configuration.md](skills/gemini-cli-guide/references/configuration.md) - 設定與 MCP 配置
- [examples.md](skills/gemini-cli-guide/references/examples.md) - 常見使用範例

---

## OpenSpec Workflow

以規格為核心的協作開發工作流程框架，在寫程式之前先對齊需求。

### 功能特色

- **工作流程選擇**：決策樹引導選擇 Quick Feature、Exploratory 或 Parallel Changes 工作流程
- **Artifact 生成策略**：依複雜度選擇一次產出或逐步產出
- **變更生命週期**：提案 → 差異規格 → 設計 → 任務 → 實作 → 驗證 → 歸檔
- **驗證三維度**：完整性、正確性、一致性
- **更新 vs 重新開始**：何時微調既有變更、何時另起爐灶

### 使用方式

自然語言觸發，例如：

- 「我想用 OpenSpec 規劃一個新功能」
- 「這個需求該用快速流程還是探索流程？」
- 「幫我寫這個變更的 proposal」

---

## 其他推薦技能

精選社群中好用的 Claude Code 技能。

- [查看完整清單](RECOMMENDED_SKILLS_zh.md)

---

## 安裝方式

```bash
# 本地開發測試
claude --plugin-dir ./
```

## 檔案結構

```
awesome-momochenisme-skills/
├── README.md
├── README_zh.md
├── RECOMMENDED_SKILLS.md
├── RECOMMENDED_SKILLS_zh.md
├── .gitignore
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
    ├── momochenisme-writing-style/
    │   ├── SKILL.md
    │   └── references/
    ├── conventional-commit/
    │   ├── SKILL.md
    │   └── references/
    ├── ui-ux-pro-max/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── data/
    ├── openspec-workflow/
    │   ├── SKILL.md
    │   └── references/
    ├── skill-creator/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── references/
    ├── plugin-creator/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── references/
    ├── claude-code-cli-guide/
    │   ├── SKILL.md
    │   └── references/
    └── gemini-cli-guide/
        ├── SKILL.md
        └── references/
```

## 授權

MIT License
