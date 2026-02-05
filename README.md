# Awesome MomoChenIsMe Skills

A collection of Claude Code skills for productivity and content creation.

## Skills Overview

| Skill | Description |
|-------|-------------|
| **Sync Scribe** | Note-taking and todo management |
| **MomoChenIsMe Writing Style** | Blog writing style guide |

---

## Sync Scribe

A simplified note-taking and todo management skill for Claude Code.

### Features

- 🎯 **Auto-categorization**: Automatically determines if input is a todo or note
- ✅ **Todo management**: Add, complete, and delete tasks
- 📝 **Note management**: Categorized notes with timestamps
- 🔍 **Search & filter**: Find items by keyword or category

### Usage

#### Slash Commands

| Command | Description |
|---------|-------------|
| `/add-todo <task>` | Add a new todo |
| `/complete-todo <keyword>` | Mark as complete |
| `/list-todos [filter]` | List all todos |
| `/delete-todo <keyword>` | Remove a todo |
| `/add-note <content>` | Add a new note |
| `/list-notes [category\|keyword]` | List notes |
| `/delete-note <keyword>` | Remove a note |

#### Natural Language

Just say:
- "記得買牛奶" → Adds to todos
- "記一下：咖啡廳很好喝" → Adds to notes
- "買牛奶完成了" → Marks complete

### Data Storage

- `TODOS.md` - Todo list
- `NOTES.md` - Categorized notes

Files are stored in your workspace root.

---

## MomoChenIsMe Writing Style

A skill that mimics the unique writing style of MomoChenIsMe blogger for technical articles.

### Features

- 🗣️ **Conversational tone**: Friendly, approachable writing like chatting with a friend
- 😄 **Moderate humor**: Light self-deprecating humor with frequent use of "XD"
- 🎯 **Practice-oriented**: Emphasizes "how to do" over abstract theory
- 🌏 **Language style**: Traditional Chinese with English technical terms preserved

### Suitable Article Types

- **Technical tutorials**: Step-by-step guides with screenshots and code blocks
- **Product reviews**: Tool introductions with honest pros and cons
- **Personal reflections**: Experience sharing with lessons learned
- **Year-end reviews**: Timeline-based retrospectives

### Usage

Trigger naturally by asking Claude:
- "用 MomoChenIsMe 的風格寫一篇關於 Docker 的教學"
- "幫我用 MomoChenIsMe 風格介紹這個工具"
- "以 MomoChenIsMe 的口吻寫年度回顧"

### Style Highlights

| Element | Usage |
|---------|-------|
| 💡 | Important tips, notes, limitations |
| ✨ | Exciting features or highlights |
| XD | Humor and light-hearted moments |
| 「」 | Technical terms and key concepts |
| **Bold** | Emphasis on keywords |

---

## Installation

```bash
# Local development
claude --plugin-dir ./
```

## File Structure

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

## License

MIT License
