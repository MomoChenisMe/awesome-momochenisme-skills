# Add Note

Save a new note with automatic categorization.

## Usage
/add-note <content> [--category <category>]

## Instructions
1. Read `NOTES.md` from workspace root
2. Determine category:
   - If `--category` specified, use that
   - If content mentions work/code/project → `工作`
   - If content mentions life/food/travel → `生活`
   - Otherwise → `未分類`
3. Create a title from the first sentence or summary
4. Add entry under the category section:
   ```
   ## [YYYY-MM-DD] Title
   Content...
   ```
5. Write the updated file
6. Confirm the addition

## Example
```
/add-note 捷運站附近的咖啡廳很好喝
```
Adds a note under `# 分類：生活`.

```
/add-note API 金鑰位置在環境變數 --category 工作
```
Adds a note under `# 分類：工作`.
