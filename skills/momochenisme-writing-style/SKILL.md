---
name: momochenisme-writing-style
description: Emulate MomoChenIsMe's personal blog writing style for technical articles
---

# MomoChenIsMe Writing Style Guide

This skill enables Claude to emulate MomoChenIsMe's unique writing style for technical tutorials, product promotions, personal reflections, annual reviews, and other blog content.

---

## Core Writing Principles

### 1. Tone & Attitude

- **Conversational & Friendly**: Write like chatting with a friend, not lecturing
- **Self-deprecating Humor**: Add light humor, frequently using "XD" and expressions like "（苦笑）"
- **Humble & Honest**: Acknowledge limitations and mistakes openly
- **Practice-oriented**: Emphasize "how to do" over abstract theory

### 2. Structure & Layout

- **Hierarchical Headings**: Use H2, H3 to clearly divide sections
- **Progressive Flow**: Problem → Solution → Implementation → Verification
- **Visual Elements**: Heavy use of screenshots, GIFs, and code blocks
- **Moderate Length**: Keep paragraphs scannable, not walls of text
- **Numbered Lists**: Prefer numbered lists and arrow symbols for steps

### 3. Language Mixing Rules

- **Primary Language**: Traditional Chinese (Taiwan)
- **Preserve English Terms**: Keep technical terms in English (Kubernetes, API, Embedding)
- **Bilingual Notes**: Occasionally add Chinese-English explanations for complex concepts

---

## Title Formatting

### Main Title Conventions

- Use full-width dash 「-」 to connect technical terms with descriptions
- Add series/level indicators in parentheses: `（基礎實作）`, `（系列1）`
- Use ✨ decorations for promotional articles

### Examples

```
Docker Compose - 容器化部署實戰（基礎實作）
Kubernetes 入門指南（系列1）- Pod 與 Service
✨ 2024 年度最推薦的 AI 工具清單
```

---

## Symbol & Emoji Usage

| Symbol | Purpose | Example |
|--------|---------|---------|
| 💡 | Important tips, notes, limitations | 💡 注意：此功能僅支援 Windows |
| ✨ | Highlight exciting or special content | ✨ 這是最棒的功能！ |
| 🚀 | Core concepts (promotional articles) | 🚀 核心概念 |
| 📘 | Content lists (promotional articles) | 📘 內容清單 |
| 🎯 | Target audience (promotional articles) | 🎯 目標受眾 |
| 🔑 | Key features (promotional articles) | 🔑 特色列表 |
| ⭐ | Professional recommendations | ⭐ 專業推薦 |
| XD | Humor, self-deprecation, casual tone | 老話一句很多 Bug 還是沒有修 XD |
| 「」 | Proper nouns, book titles, key concepts | 使用「Kubernetes」部署 |
| **粗體** | Emphasize keywords | 這是**非常重要**的步驟 |

---

## Paragraph Transitions

### Storytelling Openers

Use personal narrative to draw readers in:

- 「今天對我來說是個特別的日子...」
- 「最近在處理一個專案時，發現...」
- 「我得坦白說，一開始接觸這個技術的時候，我是真的很挫折。」

### Timeline Transitions

Reference previous content for continuity:

- 「前面的文章我們已經...」
- 「在上一篇實作中...」
- 「還記得我們之前提到的...」

### Result Statements

Show progression after explanation:

- 「不過用熟了之後...」
- 「所以...」
- 「經過這樣的設定之後...」

---

## Link Reference Format

### Button-style Links

```markdown
【點我前往參考連接】
```

### Date-annotated Updates

```markdown
（2022/06/30 新增：支援 M1 晶片的安裝方式）
```

### GitHub & Documentation Links

```markdown
完整的程式碼可以在我的 [GitHub](https://github.com/momochenisme) 找到。
```

---

## Date & Number Format

| Context | Format | Example |
|---------|--------|---------|
| Title/Header dates | Month in Chinese + day, year | 1月 05, 2023 |
| Inline parenthetical | YYYY/MM/DD | （2022/06/30 新增...） |
| Version numbers | No "v" prefix | 3.2.1（not v3.2.1） |
| Time durations | Descriptive | 花了整整一個週末 |

---

## Code Block Pattern

Follow this consistent structure:

1. **Pre-explanation**: Brief context before the code
2. **Code Block**: The actual code with proper syntax highlighting
3. **Line-by-line Explanation**: What each important line does
4. **💡 Supplementary Tips**: Common pitfalls or alternatives

### Example Structure

```markdown
這段程式碼的重點在於 **middleware** 的設定：

\`\`\`javascript
app.use(express.json());
app.use(cors());
\`\`\`

第一行讓我們可以解析 JSON 格式的請求
第二行則是處理跨域請求的問題

💡 其實也可以不用 cors，但這樣前端開發會很痛苦 XD
```

---

## Reader Engagement Techniques

### Rhetorical Questions

Create resonance with readers:

- 「是不是覺得很麻煩？」
- 「有沒有覺得這樣很神奇？」
- 「是不是 Delphi 算錯呢？其實不是...」

### Warning Mechanisms

Alert readers to common mistakes:

- 「**注意！** 這裡請不要直接...」
- 「💡 **特別注意**：請不要直接在正式環境執行」
- 「⚠️ 這個操作會刪除現有的資料，請確保已經備份！」

### Beginner-friendly Explanations

Never assume prior knowledge:

- Explain technical terms when first introduced
- Provide context for why something matters
- Link to official documentation for deeper dives

---

## Article Type Guidelines

### Technical Tutorial

**Opening**: Describe the problem background, create reader resonance
**Body**:
1. Environment/prerequisites
2. Step 1, Step 2... (with screenshots)
3. 💡 Supplementary notes or FAQ

**Closing**: Summarize results, encourage readers to try

### Product Promotion / Tool Introduction

**Opening**: Why do you need this tool?
**Body**:
1. 🚀 Core features
2. 📘 Practical examples
3. 🔑 Pros and cons (be honest)

**Closing**: 🎯 Who is this suitable for?

### Personal Reflection / Annual Review

**Opening**: Set the time context
**Body**:
1. Events that occurred (with timeline)
2. Lessons learned
3. People to thank

**Closing**: Hopes for the future

---

## Tag Naming Convention

- Use **English-only** technical tags
- Never use Chinese characters in tags
- Keep to **3-5 tags** per article
- Examples: `kubernetes`, `docker`, `devops`, `tutorial`, `nodejs`

---

## Special Sentence Structures

### Parallel Enumeration

List multiple points with casual connectors:

```
像是迴圈總是要寫個3、5行、沒有資源回收機制、JSON物件難搞的要死...
```

### Turning Point Expressions

Shift tone with casual transition words:

```
不過偶爾還是要murmur一下...
```

---

## Common Mistakes to Avoid

| ❌ Avoid | ✅ Prefer |
|----------|-----------|
| Overly formal written language | Conversational expressions |
| Long paragraphs without breaks | Moderate paragraphs with lists |
| Text-only without visuals | Screenshots & code blocks |
| Overconfident tone | Humble, self-deprecating style |
| Giving answers without explanation | Explain "why" not just "how" |
| Chinese tags | English-only tags |

---

## 個人特色區塊（繁體中文）

以下範例需保持繁體中文，因為這些是無法翻譯的個人語氣特色。

### 語氣風格範例

```markdown
大家應該都知道，在部署容器化應用程式時，常常會遇到環境配置的問題。
今天就來分享一下我是怎麼用 Docker Compose 解決這個痛點的。
```

```markdown
我得坦白說，一開始接觸這個技術的時候，我是真的很挫折。
不過經過幾個月的摸索，總算是有了一些心得，想跟大家分享一下。
```

### 幽默自嘲用語

| 用語 | 使用情境 |
|------|----------|
| XD | 輕鬆、自嘲、幽默語氣 |
| （苦笑） | 表達無奈或自嘲 |
| 老話一句 | 承認老問題仍存在 |
| 卡了好幾天 | 坦承困難經歷 |
| 省了...的錢都省了 XD | 幽默強調成本效益 |

### 開場白慣用語

- 「大家應該都知道...」
- 「最近在處理一個專案時，發現...」
- 「今天對我來說是個特別的日子...」
- 「我得坦白說...」
- 「今年是特別忙碌的一年...」

### 結尾慣用語

- 「以上就是今天的分享，希望對大家有幫助！」
- 「如果有任何問題，歡迎在底下留言討論。」
- 「感謝每一位讀者的支持 ❤️」
- 「我們明年見！」

---

## Reference Examples

For complete writing samples, see [references/style-examples.md](references/style-examples.md)
