#!/usr/bin/env python3
"""
Plugin 初始化腳本

用法:
    python init_plugin.py <plugin-name> [--output <path>]

範例:
    python init_plugin.py my-awesome-plugin
    python init_plugin.py my-plugin --output ~/plugins
"""

import argparse
import json
import os
import sys
from pathlib import Path


def create_plugin_structure(plugin_name: str, output_path: Path) -> None:
    """建立 plugin 目錄結構"""

    plugin_dir = output_path / plugin_name

    # 檢查是否已存在
    if plugin_dir.exists():
        print(f"錯誤: 目錄 '{plugin_dir}' 已存在", file=sys.stderr)
        sys.exit(1)

    # 建立目錄結構
    directories = [
        plugin_dir / ".claude-plugin",
        plugin_dir / "commands",
        plugin_dir / "skills",
        plugin_dir / "hooks",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ 建立目錄: {directory.relative_to(output_path)}")

    # 建立 plugin.json manifest
    manifest = {
        "name": plugin_name,
        "description": f"{plugin_name} plugin for Claude Code",
        "version": "1.0.0",
        "author": ""
    }

    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"✓ 建立 manifest: {manifest_path.relative_to(output_path)}")

    # 建立範例 command
    example_command = '''---
name: Hello
description: 範例 command，顯示問候訊息
user-invocable: true
---

# Hello Command

這是一個範例 command。當使用者輸入 `/hello` 時會觸發此技能。

## 行為

回應使用者一個友善的問候訊息。
'''

    command_path = plugin_dir / "commands" / "hello.md"
    with open(command_path, "w", encoding="utf-8") as f:
        f.write(example_command)
    print(f"✓ 建立範例 command: {command_path.relative_to(output_path)}")

    # 建立範例 skill
    example_skill = '''---
name: Example Skill
description: 範例 agent skill
---

# Example Skill

這是一個範例 agent skill。Agent 會在適當的時機自動使用此技能。

## 使用時機

描述 agent 應該何時使用此技能。

## 指引

提供給 agent 的具體指引和最佳實踐。
'''

    skill_path = plugin_dir / "skills" / "example-skill.md"
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(example_skill)
    print(f"✓ 建立範例 skill: {skill_path.relative_to(output_path)}")

    # 建立 README
    readme_content = f'''# {plugin_name}

Claude Code plugin.

## 安裝

```bash
claude --plugin-dir ./{plugin_name}
```

## 功能

- `/hello` - 範例 command

## 開發

編輯 `commands/` 和 `skills/` 目錄中的文件來擴展功能。

## 測試

```bash
claude --plugin-dir ./{plugin_name}
```
'''

    readme_path = plugin_dir / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✓ 建立 README: {readme_path.relative_to(output_path)}")

    # 建立 .gitignore
    gitignore_content = '''# Claude Code
.claude/

# OS
.DS_Store
Thumbs.db

# Editor
*.swp
*.swo
.idea/
.vscode/
'''

    gitignore_path = plugin_dir / ".gitignore"
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print(f"✓ 建立 .gitignore: {gitignore_path.relative_to(output_path)}")

    print()
    print(f"Plugin '{plugin_name}' 建立完成！")
    print()
    print("下一步:")
    print(f"  1. 編輯 {plugin_dir / '.claude-plugin' / 'plugin.json'} 填寫作者資訊")
    print(f"  2. 在 commands/ 和 skills/ 目錄中建立你的組件")
    print(f"  3. 使用以下指令測試: claude --plugin-dir {plugin_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="初始化 Claude Code plugin 目錄結構",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  %(prog)s my-plugin              在當前目錄建立 my-plugin
  %(prog)s my-plugin -o ~/plugins 在指定路徑建立 my-plugin
        """
    )

    parser.add_argument(
        "name",
        help="Plugin 名稱 (將作為目錄名稱)"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path.cwd(),
        help="輸出路徑 (預設: 當前目錄)"
    )

    args = parser.parse_args()

    # 驗證 plugin 名稱
    if not args.name.replace("-", "").replace("_", "").isalnum():
        print("錯誤: Plugin 名稱只能包含字母、數字、底線和連字號", file=sys.stderr)
        sys.exit(1)

    # 確保輸出路徑存在
    output_path = args.output.resolve()
    if not output_path.exists():
        print(f"錯誤: 輸出路徑 '{output_path}' 不存在", file=sys.stderr)
        sys.exit(1)

    create_plugin_structure(args.name, output_path)


if __name__ == "__main__":
    main()
