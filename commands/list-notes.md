---
name: list-notes
description: 顯示所有筆記，可按分類或關鍵字篩選。使用方式：/list-notes [分類|關鍵字]
---

# List Notes

Display all notes, optionally filtered by category or keyword.

## Usage
/list-notes [category|keyword]

## Instructions
1. Read `NOTES.md` from workspace root
2. If `$ARGUMENTS` matches a category (工作/生活/未分類), show only that category
3. Otherwise, search all notes for the keyword
4. Display matching notes with their dates and titles

## Example
```
/list-notes
```
Shows all notes.

```
/list-notes 工作
```
Shows only notes in the "工作" category.

```
/list-notes API
```
Shows notes containing "API".
