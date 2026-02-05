# CLI Flags Reference

## Table of Contents
- [Mode and Query](#mode-and-query)
- [Session Management](#session-management)
- [Working Directory](#working-directory)
- [Agent Configuration](#agent-configuration)
- [Permission Control](#permission-control)
- [Output Format](#output-format)
- [System Prompt](#system-prompt)
- [MCP Configuration](#mcp-configuration)
- [Model Settings](#model-settings)
- [Remote Sessions](#remote-sessions)
- [Plugins and Tools](#plugins-and-tools)
- [IDE Integration](#ide-integration)
- [Initialization](#initialization)
- [Advanced Options](#advanced-options)
- [Debugging](#debugging)

## Mode and Query

| Flag | Description |
|------|-------------|
| `-p, --print` | One-shot query mode (pipe/SDK mode) |
| `-c, --continue` | Continue most recent conversation |
| `-r, --resume <id\|name>` | Resume specific session by ID or session name |
| `--input-format <fmt>` | Input format (text/stream-json) |

### Examples

```bash
# One-shot query
claude -p "Explain this code"

# Continue recent conversation
claude -c "What else can you tell me?"

# Resume by session ID
claude -r abc123

# Resume by session name
claude -r my-project-session
```

## Session Management

| Flag | Description |
|------|-------------|
| `-c, --continue` | Continue most recent conversation |
| `-r, --resume <id\|name>` | Resume session by ID or name |
| `--session-id <id>` | Specify session ID for new session |
| `--fork-session` | Create new session ID (fork from current) |

## Working Directory

### `--add-dir <path>`
Add additional working directories. Can be used multiple times.
```bash
claude --add-dir ../shared-lib --add-dir ../docs
```

## Agent Configuration

| Flag | Description |
|------|-------------|
| `--agent <name>` | Use single specified agent |
| `--agents <json>` | Define custom subagents (JSON format) |

### Examples

```bash
# Use specific agent
claude --agent code-reviewer

# Define custom subagents (JSON object format)
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer",
    "prompt": "You are a senior code reviewer",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

## Permission Control

| Flag | Description |
|------|-------------|
| `--permission-mode <mode>` | Permission mode (default/acceptEdits/plan/dontAsk/bypassPermissions) |
| `--allowedTools <patterns>` | Restrict available tools |
| `--disallowedTools <patterns>` | Disable specific tools |
| `--tools <list>` | Limit available tools |
| `--dangerously-skip-permissions` | ⚠️ Skip all permission prompts |
| `--permission-prompt-tool <tool>` | Custom permission prompt tool |

### Permission Modes

| Mode | Description |
|------|-------------|
| `default` | Standard behavior: prompts for permission on first use of each tool |
| `acceptEdits` | Auto-accept file edit permissions for the session |
| `plan` | Plan mode: can analyze but cannot modify files or execute commands |
| `dontAsk` | Auto-reject tools unless pre-approved via `/permissions` |
| `bypassPermissions` | Skip all permission prompts (dangerous) |

### Tool Patterns

`--allowedTools` and `--disallowedTools` support glob patterns:

```bash
# Allow only read operations
claude --allowedTools "Read,Glob,Grep"

# Allow all tools matching pattern
claude --allowedTools "mcp__*"

# Disable all bash-related tools
claude --disallowedTools "Bash*"

# Full automation (dangerous)
claude --dangerously-skip-permissions -p "task"
```

## Output Format

| Flag | Description |
|------|-------------|
| `--output-format <fmt>` | Format: text/json/stream-json |
| `--json-schema <schema>` | JSON output schema |

### Examples

```bash
# JSON output for scripts
claude -p "List files" --output-format json

# With schema validation
claude -p "Get user info" --json-schema '{"type": "object", "properties": {"name": {"type": "string"}}}'
```

## System Prompt

| Flag | Description |
|------|-------------|
| `--system-prompt <p>` | Override default system prompt |
| `--append-system-prompt <p>` | Append to system prompt |
| `--system-prompt-file <path>` | Load system prompt from file |
| `--append-system-prompt-file <path>` | Append prompt from file |

### Examples

```bash
# Override system prompt
claude --system-prompt "You are a Python expert"

# Append to default
claude --append-system-prompt "Respond in formal English"

# Load from file
claude --system-prompt-file ./prompts/expert.md

# Append from file
claude --append-system-prompt-file ./prompts/style.md
```

## MCP Configuration

| Flag | Description |
|------|-------------|
| `--mcp-config <path>` | Specify MCP config file |
| `--strict-mcp-config` | Fail if MCP config has issues |

## Model Settings

| Flag | Description |
|------|-------------|
| `--model <name>` | Specify model (opus/sonnet/haiku) |
| `--fallback-model <name>` | Fallback model when primary unavailable |
| `--max-turns <n>` | Limit agent turns |
| `--max-budget-usd <n>` | Maximum budget in USD |

### Examples

```bash
# Use specific model
claude --model opus -p "Complex task"

# With budget limit
claude --max-budget-usd 5.00 -p "Large refactor"

# With fallback
claude --model opus --fallback-model sonnet -p "Task"
```

## Remote Sessions

| Flag | Description |
|------|-------------|
| `--remote` | Create web session |
| `--teleport <id>` | Resume web session |
| `--from-pr <url>` | Resume session from GitHub PR |

### Examples

```bash
# Create web session
claude --remote

# Resume web session
claude --teleport session-abc123

# Resume from PR
claude --from-pr https://github.com/org/repo/pull/123
```

## Plugins and Tools

| Flag | Description |
|------|-------------|
| `--plugin-dir <path>` | Load plugins from directory |
| `--tools <list>` | Limit available tools |
| `--disable-slash-commands` | Disable slash commands |
| `--betas <features>` | Enable beta features |

### Examples

```bash
# Load custom plugins
claude --plugin-dir ./my-plugins

# Limit tools
claude --tools "Read,Write,Edit"

# Enable beta features
claude --betas "new-feature,experimental"
```

## IDE Integration

| Flag | Description |
|------|-------------|
| `--ide` | Auto-connect to IDE on startup if exactly one valid IDE is available |
| `--chrome` / `--no-chrome` | Chrome browser integration |

### Examples

```bash
# Auto-connect to IDE
claude --ide

# With Chrome
claude --chrome

# Without Chrome
claude --no-chrome
```

## Initialization

| Flag | Description |
|------|-------------|
| `--init` | Initialize hooks and settings |
| `--init-only` | Initialize without starting session |
| `--maintenance` | Run maintenance hooks |
| `--setting-sources <sources>` | Specify setting sources |
| `--settings <path>` | Settings file path |

### Examples

```bash
# Initialize project
claude --init

# Initialize only (no session)
claude --init-only

# Run maintenance
claude --maintenance
```

## Advanced Options

| Flag | Description |
|------|-------------|
| `--fork-session` | Create new session ID |
| `--session-id <id>` | Specify session ID |
| `--input-format <fmt>` | Input format (text/stream-json) |
| `--json-schema <schema>` | JSON output schema |

## Debugging

| Flag | Description |
|------|-------------|
| `--debug` | Enable debug mode |
| `--verbose` | Show verbose logs |
| `--no-cache` | Disable cache |
| `--version` | Show version |
| `--help` | Show help |

### Examples

```bash
# Debug mode
claude --debug -p "Debug this request"

# Verbose output
claude --verbose -p "Show details"

# Version info
claude --version

# Help
claude --help
```
