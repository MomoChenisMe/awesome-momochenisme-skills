# CLI Flags Reference

## Table of Contents
- [Mode and Prompt](#mode-and-prompt)
- [Model Selection](#model-selection)
- [Safety and Permissions](#safety-and-permissions)
- [Output Control](#output-control)
- [Context and Directory](#context-and-directory)
- [Debugging](#debugging)

## Mode and Prompt

| Flag | Description |
|------|-------------|
| `-p, --prompt <text>` | One-shot query mode (pipe mode) |
| `-i, --prompt-interactive` | Interactive prompt mode (takes input, then enters REPL) |
| `--input <text>` | Input for the prompt |
| `-r, --resume [session]` | Resume previous conversation |

### Examples

```bash
# One-shot query (pipe mode)
gemini --prompt "What is Rust?"

# Interactive prompt mode
gemini -i "Start with this context"

# With input
gemini --prompt "Explain this" --input "$(cat file.py)"

# Pipe mode
cat README.md | gemini --prompt "Summarize this"
echo "Hello" | gemini --prompt "Translate to French"

# Resume previous session
gemini -r
gemini --resume my-session
```

## Model Selection

| Flag | Description |
|------|-------------|
| `-m, --model <name>` | Specify model to use |

### Available Models

- `gemini-2.5-pro` (default)
- `gemini-2.5-flash`
- `gemini-2.0-flash`
- `gemini-1.5-pro`
- `gemini-1.5-flash`

### Examples

```bash
gemini -m gemini-2.5-flash -p "Quick question"
gemini --model gemini-2.5-pro -p "Complex analysis"
```

## Safety and Permissions

| Flag | Description |
|------|-------------|
| `-s, --sandbox` | Enable sandbox mode (restricted file access) |
| `--approval-mode <mode>` | Set approval mode |

### Approval Modes

| Mode | Description |
|------|-------------|
| `default` | Suggest actions, require approval (default) |
| `auto_edit` | Auto-approve file edits only |
| `plan` | Plan mode: analyze without executing |
| `yolo` | Auto-approve all actions (use carefully) |

> **Note**: The `--yolo` flag has been deprecated in favor of `--approval-mode=yolo`.

### Examples

```bash
# Safe mode - restricted access
gemini -s --prompt "Analyze code"

# Auto-edit mode (auto-approve file edits)
gemini --approval-mode auto_edit --prompt "Refactor function"

# Full automation (use carefully)
gemini --approval-mode yolo --prompt "Fix all lint errors"
```

## Output Control

| Flag | Description |
|------|-------------|
| `--output-format <fmt>` | Output format |

### Output Formats

| Format | Description |
|--------|-------------|
| `text` | Plain text (default) |
| `json` | JSON object |
| `stream-json` | Streaming JSON |

### Examples

```bash
# JSON output for scripts
gemini -p "List dependencies" --output-format json

# Process JSON output
gemini -p "Analyze" --output-format json | jq '.result'
```

## Context and Directory

| Flag | Description |
|------|-------------|
| `--include-all-files` | Include all files in context |
| `--include-directories <dirs>` | Include specific directories |

### Examples

```bash
# Include all project files
gemini --include-all-files -p "Review architecture"

# Include specific directories
gemini --include-directories "src,lib" -p "Find bugs"
```

## Session Management

| Flag | Description |
|------|-------------|
| `-r, --resume [session]` | Resume previous conversation |
| `--list-sessions` | List available sessions |
| `--delete-session <id>` | Delete a specific session |

### Examples

```bash
# List all sessions
gemini --list-sessions

# Resume specific session
gemini --resume my-session

# Delete a session
gemini --delete-session old-session-id
```

## Extensions

| Flag | Description |
|------|-------------|
| `-e, --extensions <names>` | Specify extensions to use |
| `-l, --list-extensions` | List available extensions |
| `--allowed-mcp-server-names` | Configure MCP servers |
| `--allowed-tools <list>` | Specify tools that bypass confirmation |

### Examples

```bash
# List available extensions
gemini -l

# Use specific extensions
gemini -e "web-search,file-reader" -p "Research topic"

# Allow specific tools without confirmation
gemini --allowed-tools "read_file,list_dir" -p "Analyze code"
```

## Accessibility

| Flag | Description |
|------|-------------|
| `--screen-reader` | Screen reader optimization |

## Debugging

| Flag | Description |
|------|-------------|
| `-d, --debug` | Enable debug mode |
| `--version` | Show version |
| `--help` | Show help |

### Examples

```bash
# Debug mode
gemini -d -p "Debug this request"

# Version info
gemini --version

# Help
gemini --help
gemini -p --help
```
