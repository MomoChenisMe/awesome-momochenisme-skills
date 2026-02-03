---
name: sync-scribe
description: Simplified note-taking and todo management. Auto-categorizes input as either a todo (actionable task) or a note (informational). Supports CRUD. Use when user wants to: (1) Record a task, (2) Save an idea, (3) List/search/update/delete todos or notes, (4) Mark a todo complete. No reminders.
---

# Sync Scribe

Capture thoughts and tasks without scheduling overhead.

## Workflow

### 1. Categorize Input
Determine if input is **Todo** or **Note**:
- **Todo**: Action-oriented. Verbs like "買", "做", "聯絡", "處理", "修復".
- **Note**: Informational, descriptive, ideas, facts.

When uncertain: if it can be "done", it's a **Todo**.

### 2. Execute Operation

| Operation | Todo | Note |
|-----------|------|------|
| **Add** | Append `- [ ] task` under `# 待辦事項` | Add `## [YYYY-MM-DD] Title` under category |
| **Complete** | Move to `# 已完成事項`, change to `- [x] ~~task~~ (完成: YYYY-MM-DD)` | N/A |
| **Update** | Edit the task text | Edit the note content |
| **Delete** | Remove the line | Remove the section |
| **List** | Read and filter `TODOS.md` | Read and filter `NOTES.md` |

## File Locations
- **Todos**: `TODOS.md` in workspace root
- **Notes**: `NOTES.md` in workspace root

## Templates

### TODOS.md
```markdown
# 待辦事項 (Active Todos)

- [ ] 任務 1
- [ ] 任務 2

# 已完成事項 (Completed Todos)

- [x] ~~已完成任務~~ (完成: YYYY-MM-DD)
```

### NOTES.md
```markdown
# 分類：工作

## [YYYY-MM-DD] 筆記標題
內容...

# 分類：生活

# 分類：未分類
```

## Examples

**User says**: "幫我記得買牛奶"
→ **Action**: Add `- [ ] 買牛奶` to `TODOS.md`

**User says**: "記一下：捷運站附近的咖啡廳很好喝"
→ **Action**: Add note to `NOTES.md` under `# 分類：生活`

**User says**: "買牛奶完成了"
→ **Action**: Move to completed, strike through

**User says**: "列出所有待辦"
→ **Action**: Read and display `TODOS.md`
