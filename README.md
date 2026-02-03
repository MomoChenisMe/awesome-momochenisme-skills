# Sync Scribe

A simplified note-taking and todo management plugin for Claude Code.

## Features

- 🎯 **Auto-categorization**: Automatically determines if input is a todo or note
- ✅ **Todo management**: Add, complete, and delete tasks
- 📝 **Note management**: Categorized notes with timestamps
- 🔍 **Search & filter**: Find items by keyword or category

## Installation

### Claude Code Plugin
```bash
# From marketplace
claude plugin install sync-scribe@your-marketplace

# Local testing
claude --plugin-dir ./sync-scribe-plugin
```

## Usage

### Slash Commands
| Command | Description |
|---------|-------------|
| `/add-todo <task>` | Add a new todo |
| `/complete-todo <keyword>` | Mark as complete |
| `/list-todos [filter]` | List all todos |
| `/delete-todo <keyword>` | Remove a todo |
| `/add-note <content>` | Add a new note |
| `/list-notes [category\|keyword]` | List notes |
| `/delete-note <keyword>` | Remove a note |

### Natural Language (Skill)
Just say:
- "記得買牛奶" → Adds to todos
- "記一下：咖啡廳很好喝" → Adds to notes
- "買牛奶完成了" → Marks complete

## File Structure

```
sync-scribe-plugin/
├── .claude-plugin/
│   └── plugin.json        # Plugin manifest
├── commands/              # Slash commands
│   ├── add-todo.md
│   ├── complete-todo.md
│   ├── list-todos.md
│   ├── delete-todo.md
│   ├── add-note.md
│   ├── list-notes.md
│   └── delete-note.md
└── skills/
    └── sync-scribe/
        └── SKILL.md       # Natural language skill
```

## Data Storage

- `TODOS.md` - Todo list
- `NOTES.md` - Categorized notes

Files are stored in your workspace root.

## License

MIT License
