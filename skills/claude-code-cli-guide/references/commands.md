# CLI Commands Reference

## Table of Contents
- [Interactive REPL](#interactive-repl)
- [One-Shot Queries](#one-shot-queries)
- [Conversation Management](#conversation-management)
- [Configuration Management](#configuration-management)
- [MCP Server Management](#mcp-server-management)
- [Other Commands](#other-commands)

## Interactive REPL

### `claude`
Start interactive REPL environment.

### `claude "query"`
Start REPL with initial prompt.
```bash
claude "Explain this project's architecture"
```

## One-Shot Queries

### `claude -p "query"`
Execute single query and exit. Ideal for pipe processing and script automation.
```bash
claude -p "What is TypeScript?"
cat README.md | claude -p "Summarize this document"
claude -p "List files" --output-format json
```

## Conversation Management

### `claude -c`
Continue most recent conversation.
```bash
claude -c
claude -c "Continue the previous task"
```

### `claude -r <session-id>`
Resume specific session. Without argument, lists available sessions.
```bash
claude -r           # List sessions
claude -r abc123    # Resume specific session
```

## Configuration Management

### `claude config`
```bash
claude config list              # List all settings
claude config get theme         # Get specific setting
claude config set theme dark    # Set value
claude config remove customKey  # Remove setting
```

**Scope options:** `--global` (default), `--project`, `--local`

## MCP Server Management

### `claude mcp`
```bash
claude mcp list                                      # List servers
claude mcp add my-server -s project -- npx server    # Add server
claude mcp remove my-server                          # Remove server
claude mcp get my-server                             # Get server JSON
```

**Scope options:** `-s, --scope <scope>` (local/project/global, default: project)

## Other Commands

| Command | Description |
|---------|-------------|
| `claude update` | Update to latest version |
| `claude doctor` | Check installation status |
| `claude api-key` | Configure API key |
