---
name: delete-note
description: 從 NOTES.md 刪除筆記。使用方式：/delete-note <標題關鍵字或日期>
---

# Delete Note

Remove a note entry from NOTES.md.

## Usage
/delete-note <title keyword or date>

## Instructions
1. Read `NOTES.md` from workspace root
2. Find the matching note by title or date
3. Remove the entire section (## header and content until next ## or # section)
4. Write the updated file
5. Confirm deletion

## Example
```
/delete-note 咖啡廳
```
Removes the note with "咖啡廳" in the title.

```
/delete-note 2026-02-03
```
Removes notes from that date.
