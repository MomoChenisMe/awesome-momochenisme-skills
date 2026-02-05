# Plugin Component Types

This document explains the various component types that can be included in a Claude Code plugin.

## Component Overview

| Component Type | Directory/Config | Trigger Method | Primary Purpose |
|----------------|------------------|----------------|-----------------|
| Commands | `commands/` | User types `/command` | User-invoked functionality |
| Skills | `skills/` | Agent auto-detection | Agent auto-used knowledge/workflows |
| Hooks | `hooks/` | Event triggers | Automation scripts |
| MCP Servers | `plugin.json` | Tool calls | Extend Claude's tool capabilities |
| LSP Servers | `plugin.json` | Auto-start | Code intelligence features |
| Agents | `agents/` | Task tool | Specialized sub-agents |

---

## Commands (User-Invocable Skills)

Commands are features users can invoke via slash commands.

### Location
```
my-plugin/
└── commands/
    └── my-command.md
```

### Format

```markdown
---
name: Command Name
description: Brief description (shown in command list)
user-invocable: true
---

# Command Title

## Description

Describe what this command does.

## Usage

Explain how users should use it, including parameters.

## Steps

1. Step one
2. Step two
3. ...
```

### Key Frontmatter

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✓ | Display name |
| `description` | ✓ | Brief description |
| `user-invocable` | ✓ | Must be `true` |

### Example: Deploy Command

```markdown
---
name: Deploy
description: Deploy application to specified environment
user-invocable: true
---

# Deploy

Deploy current project to specified environment.

## Parameters

- Environment name (production, staging, development)

## Workflow

1. Check current branch status
2. Run tests
3. Build project
4. Deploy to specified environment
5. Verify deployment result
```

---

## Skills (Agent Skills)

Skills are knowledge and workflow guidance that agents automatically use.

### Location
```
my-plugin/
└── skills/
    └── my-skill.md
```

### Format

```markdown
---
name: Skill Name
description: Brief description
---

# Skill Title

## When to Use

Describe when the agent should use this skill.

## Guidelines

Provide specific operational guidance and best practices.
```

### Difference from Commands

| Property | Commands | Skills |
|----------|----------|--------|
| Trigger | User types `/command` | Agent auto-detection |
| `user-invocable` | Must be `true` | Not set or `false` |
| Purpose | Explicit user commands | Background knowledge/workflow guidance |

---

## Hooks

Hooks let you automatically run scripts when specific events occur.

### Location
```
my-plugin/
└── hooks/
    └── hooks.json
```

### Configuration Format

```json
{
  "hooks": {
    "hook-name": {
      "command": "command to execute",
      "args": ["arg1", "arg2"],
      "description": "Hook description",
      "timeout": 30000
    }
  }
}
```

### Available Hook Events

| Hook Name | Trigger Time |
|-----------|--------------|
| `pre-commit` | Before git commit |
| `post-commit` | After git commit |
| `pre-push` | Before git push |
| `on-file-save` | When file is saved |
| `on-session-start` | When session starts |
| `on-session-end` | When session ends |

### Example

```json
{
  "hooks": {
    "pre-commit": {
      "command": "npm",
      "args": ["run", "lint"],
      "description": "Run linting before commit"
    },
    "on-file-save": {
      "command": "prettier",
      "args": ["--write", "$FILE"],
      "description": "Auto-format on save"
    }
  }
}
```

---

## MCP Servers

MCP (Model Context Protocol) servers extend Claude's tool capabilities.

### Configuration Location

In `plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "...",
  "mcpServers": {
    "server-name": {
      "command": "execution command",
      "args": ["arguments"],
      "env": {
        "ENV_VAR": "value"
      }
    }
  }
}
```

### Configuration Fields

| Field | Type | Description |
|-------|------|-------------|
| `command` | string | Command to start server |
| `args` | string[] | Command arguments |
| `env` | object | Environment variables |

### Example: Database MCP Server

```json
{
  "mcpServers": {
    "database": {
      "command": "node",
      "args": ["./servers/database-server.js"],
      "env": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432"
      }
    }
  }
}
```

---

## LSP Servers

LSP (Language Server Protocol) servers provide code intelligence features.

### Configuration Location

In `plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "...",
  "lspServers": {
    "server-name": {
      "command": "execution command",
      "args": ["arguments"],
      "languages": ["supported languages"]
    }
  }
}
```

### Configuration Fields

| Field | Type | Description |
|-------|------|-------------|
| `command` | string | Command to start server |
| `args` | string[] | Command arguments |
| `languages` | string[] | Supported programming languages |

### Example

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "languages": ["typescript", "javascript"]
    }
  }
}
```

---

## Agents

Custom agents handle specific types of tasks.

### Location
```
my-plugin/
└── agents/
    └── my-agent.md
```

### Format

```markdown
---
name: Agent Name
description: Agent description
tools: [list of available tools]
---

# Agent Guidelines

## Role Definition

Describe this agent's role and expertise.

## Task Scope

Explain what types of tasks this agent handles.

## Workflow

1. Step one
2. Step two
3. ...
```

---

## Component Selection Guide

### Which component should I use?

```
Does the user need to actively invoke the feature?
├── Yes → Use Commands
└── No → Does the agent need background knowledge?
    ├── Yes → Use Skills
    └── No → Need to auto-run scripts?
        ├── Yes → Use Hooks
        └── No → Need external tool integration?
            ├── Yes → Use MCP Servers
            └── No → Need code intelligence?
                ├── Yes → Use LSP Servers
                └── No → May not need a plugin
```

### Combined Usage Example

A complete CI/CD plugin might include:

- **Commands**: `/deploy`, `/rollback`, `/status`
- **Skills**: CI/CD best practices guidance
- **Hooks**: `pre-push` to run tests
- **MCP Server**: Interact with CI platform API
