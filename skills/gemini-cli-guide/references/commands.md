# Commands Reference

## Table of Contents
- [Slash Commands](#slash-commands)
- [@ Commands (File Context)](#-commands-file-context)
- [! Commands (Shell Execution)](#-commands-shell-execution)

## Slash Commands

### Session Management

| Command | Description |
|---------|-------------|
| `/chat <name>` | Save/switch named conversation |
| `/chat list` | List saved conversations |
| `/clear` | Clear conversation history |
| `/resume [session]` | Resume a previous conversation |
| `/rewind [n]` | Rewind conversation by n turns (default: 1) |
| `/save [label]` | Save conversation history with optional label |
| `/quit` | Exit Gemini CLI |

### Configuration

| Command | Description |
|---------|-------------|
| `/settings` | Open settings UI |
| `/auth` | Manage authentication |
| `/theme [name]` | Switch theme (light/dark/system) |
| `/vim` | Toggle vim mode |
| `/model [name]` | Switch or display current model |

### Tools & Extensions

| Command | Description |
|---------|-------------|
| `/tools` | List available tools |
| `/tools enable <name>` | Enable specific tool |
| `/tools disable <name>` | Disable specific tool |
| `/mcp` | List MCP servers |
| `/mcp add <name> <cmd>` | Add MCP server |
| `/mcp remove <name>` | Remove MCP server |
| `/hooks` | Manage lifecycle hooks |
| `/skills` | Manage agent skills |
| `/extensions` | List active extensions in current session |

### Memory & Context

| Command | Description |
|---------|-------------|
| `/memory` | Show memory status |
| `/memory add <text>` | Add to persistent memory |
| `/memory clear` | Clear memory |
| `/compress` | Compress conversation context |
| `/directory [path]` | Set or show working directory |
| `/restore` | Restore project files to state before tool execution |

### Workflow

| Command | Description |
|---------|-------------|
| `/bug` | Report a bug |
| `/copy` | Copy last response to clipboard |
| `/editor` | Open response in external editor |
| `/init` | Initialize project with GEMINI.md |
| `/setup-github` | Set up GitHub Actions integration |
| `/export [format]` | Export conversation to Markdown or JSON |

### Information & Debugging

| Command | Description |
|---------|-------------|
| `/help` | Show help |
| `/help <command>` | Show command help |
| `/about` | Show version info |
| `/version` | Show version information |
| `/docs` | Open documentation in browser |
| `/stats` | Show session statistics |
| `/privacy` | Show privacy information |
| `/introspect` | Show debug information |

### IDE & Terminal

| Command | Description |
|---------|-------------|
| `/ide` | IDE integration settings |
| `/terminal-setup` | Terminal configuration helper |
| `/policies` | Manage security policies |
| `/shells` | View background shells |
| `/bashes` | Alias for `/shells` |

## @ Commands (File Context)

Add files or directories to conversation context.

### Syntax

```bash
@path/to/file          # Single file
@path/to/directory     # Entire directory
@./relative/path       # Relative path
@~/home/path           # Home directory path
```

### Examples

```bash
# Include single file
gemini "Explain this code @src/main.py"

# Include multiple files
gemini "@package.json @tsconfig.json Check for issues"

# Include directory
gemini "@src/ Analyze the codebase structure"

# Combine with queries
gemini "Refactor @src/utils.ts to use TypeScript generics"
```

### Glob Patterns

```bash
@src/*.ts              # All TypeScript files in src
@**/*.test.js          # All test files recursively
@docs/**/*.md          # All markdown in docs tree
```

## ! Commands (Shell Execution)

Execute shell commands directly from Gemini.

### Syntax

```bash
!command               # Execute and show output
!!command              # Execute silently
```

### Examples

```bash
# Run commands
!ls -la
!git status
!npm test

# Pipe output to context
!cat config.json       # Shows output and adds to context

# Chain with questions
!git diff
"Explain these changes"

# Silent execution
!!npm install          # Runs without showing output
```

### Combined Usage

```bash
# Check files then ask about them
!ls src/
"Which of these files handles routing?"

# Run tests and analyze
!npm test 2>&1
"Why are these tests failing?"
```
