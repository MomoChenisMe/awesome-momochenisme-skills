# Plugin Directory Structure

This document explains the directory structure and manifest configuration for Claude Code plugins.

## Directory Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (required)
├── commands/                # User-invocable slash commands
│   ├── my-command.md
│   └── another-command.md
├── skills/                  # Agent skills
│   └── my-skill.md
├── hooks/                   # Hook configurations
│   └── hooks.json
├── agents/                  # Custom agents
│   └── my-agent.md
└── README.md
```

## Manifest Schema (plugin.json)

`plugin.json` is the core configuration file and **must** be located inside the `.claude-plugin/` directory.

### Basic Fields

```json
{
  "name": "my-plugin",
  "description": "Plugin functionality description",
  "version": "1.0.0",
  "author": "Author Name"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✓ | Plugin identifier, use kebab-case |
| `description` | string | ✓ | Brief description of plugin functionality |
| `version` | string | | Version number, semver format recommended |
| `author` | string | | Author name or organization |

### Advanced Fields

```json
{
  "name": "advanced-plugin",
  "description": "Advanced plugin example",
  "version": "1.0.0",
  "author": "Example Team",
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["./servers/my-server.js"]
    }
  },
  "lspServers": {
    "my-lsp": {
      "command": "my-lsp-binary",
      "args": ["--stdio"],
      "languages": ["mylang"]
    }
  }
}
```

## Directory Descriptions

### commands/

Stores user-invocable skills (slash commands).

- Each `.md` file represents one command
- Filename (without extension) becomes the command name
- Must set `user-invocable: true` in frontmatter

```markdown
---
name: Deploy
description: Deploy application
user-invocable: true
---

# Deploy Command

Deployment instructions...
```

### skills/

Stores agent skills that are automatically used by the agent.

- No need to set `user-invocable`
- Should clearly describe when to use this skill

### hooks/

Stores hook configurations. Define hooks using `hooks.json`:

```json
{
  "hooks": {
    "pre-commit": {
      "command": "npm run lint",
      "description": "Run lint before commit"
    }
  }
}
```

### agents/

Stores custom agent definitions.

## Common Errors

### ❌ Wrong: Placing commands inside .claude-plugin

```
my-plugin/
├── .claude-plugin/
│   ├── plugin.json
│   └── commands/        ← Wrong location!
│       └── my-command.md
```

### ✓ Correct: Placing commands in plugin root

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/            ← Correct location
│   └── my-command.md
```

### ❌ Wrong: plugin.json not in .claude-plugin directory

```
my-plugin/
├── plugin.json          ← Wrong location!
├── commands/
```

### ✓ Correct: plugin.json inside .claude-plugin directory

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      ← Correct location
├── commands/
```

### ❌ Wrong: Invalid JSON format

```json
{
  "name": "my-plugin",
  "description": "description",  // Comments not allowed
}
```

### ✓ Correct: Valid JSON

```json
{
  "name": "my-plugin",
  "description": "description"
}
```

## Best Practices

1. **Naming Conventions**
   - Plugin names use kebab-case: `my-awesome-plugin`
   - Command files use kebab-case: `deploy-app.md`
   - Skill files use kebab-case: `code-review.md`

2. **Version Management**
   - Use semver format: `major.minor.patch`
   - Document changes in README

3. **File Organization**
   - One file per command/skill
   - Use meaningful filenames
   - List all features in README.md

4. **Testing**
   - Use `--plugin-dir` to test local plugins
   - Ensure all commands trigger correctly
