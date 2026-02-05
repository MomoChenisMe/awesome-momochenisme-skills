---
name: list-todos
description: 顯示所有待辦事項和已完成事項。使用方式：/list-todos [篩選關鍵字]
---

# List Todos

Display all active and completed todos.

## Usage
/list-todos [filter]

## Instructions
1. Read `TODOS.md` from workspace root
2. If `$ARGUMENTS` provided, filter tasks containing that keyword
3. Display active todos first, then completed todos
4. Show count summary

## Example
```
/list-todos
```
Shows all todos.

```
/list-todos 工作
```
Shows only todos containing "工作".
