# Configuration Reference

## Table of Contents
- [Configuration Files](#configuration-files)
- [settings.json Structure](#settingsjson-structure)
- [Environment Variables](#environment-variables)
- [GEMINI.md Project Instructions](#geminimd-project-instructions)
- [MCP Server Configuration](#mcp-server-configuration)

## Configuration Files

### File Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `~/.gemini/settings.json` | Global | Lowest |
| `.gemini/settings.json` | Project | Higher |
| Environment variables | Session | Highest |

### Precedence

Project settings override global settings. Environment variables override both.

## settings.json Structure

The settings.json file supports the following sections:

### General Settings

```json
{
  "general": {
    "vimMode": false,
    "checkpointing": true
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `vimMode` | boolean | false | Enable vim keybindings |
| `checkpointing` | boolean | true | Auto-save conversation checkpoints |

### Output Settings

```json
{
  "output": {
    "format": "text",
    "color": true
  }
}
```

### UI Settings

```json
{
  "ui": {
    "theme": "system",
    "hideBanner": false
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `theme` | string | "system" | Theme (light/dark/system) |
| `hideBanner` | boolean | false | Hide startup banner |

### IDE Settings

```json
{
  "ide": {
    "enabled": false,
    "editor": "vscode"
  }
}
```

### Privacy Settings

```json
{
  "privacy": {
    "telemetry": true,
    "collectUsageData": true
  }
}
```

### Model Settings

```json
{
  "model": {
    "name": "gemini-2.5-pro",
    "maxSessionTurns": 100
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | "gemini-2.5-pro" | Default model |
| `maxSessionTurns` | number | 100 | Max turns per session |

### Model Configs

```json
{
  "modelConfigs": {
    "gemini-2.5-pro": {
      "temperature": 0.7,
      "maxTokens": 8192
    }
  }
}
```

### Agents Settings

```json
{
  "agents": {
    "enabled": true,
    "customAgents": []
  }
}
```

### Context Settings

```json
{
  "context": {
    "includeDirectories": ["src", "lib", "docs"],
    "excludePatterns": ["node_modules", ".git"]
  }
}
```

### Tools Settings

```json
{
  "tools": {
    "sandbox": false,
    "allowed": ["read", "write", "shell"],
    "exclude": ["dangerous_tool"]
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `sandbox` | boolean | false | Enable sandbox mode |
| `allowed` | array | all | Allowed tools |
| `exclude` | array | [] | Excluded tools |

### MCP Settings

```json
{
  "mcp": {
    "servers": {}
  }
}
```

### Security Settings

```json
{
  "security": {
    "approvalMode": "default",
    "trustedPaths": []
  }
}
```

### Advanced Settings

```json
{
  "advanced": {
    "debug": false,
    "verbose": false
  }
}
```

### Experimental Settings

```json
{
  "experimental": {
    "features": []
  }
}
```

### Skills Settings

```json
{
  "skills": {
    "enabled": true,
    "customSkills": []
  }
}
```

### Hooks Settings

```json
{
  "hooks": {
    "preCommand": [],
    "postCommand": []
  }
}
```

### Admin Settings

```json
{
  "admin": {
    "allowedUsers": []
  }
}
```

### Telemetry Settings

```json
{
  "telemetry": {
    "enabled": true
  }
}
```

### Complete Example

```json
{
  "general": {
    "vimMode": true,
    "checkpointing": true
  },
  "output": {
    "format": "text",
    "color": true
  },
  "ui": {
    "theme": "dark",
    "hideBanner": false
  },
  "ide": {
    "enabled": false
  },
  "privacy": {
    "telemetry": false
  },
  "model": {
    "name": "gemini-2.5-pro",
    "maxSessionTurns": 50
  },
  "modelConfigs": {
    "gemini-2.5-pro": {
      "temperature": 0.7
    }
  },
  "agents": {
    "enabled": true
  },
  "context": {
    "includeDirectories": ["src"]
  },
  "tools": {
    "sandbox": false,
    "allowed": ["read", "write", "shell", "web"],
    "exclude": []
  },
  "mcp": {
    "servers": {}
  },
  "security": {
    "approvalMode": "default"
  },
  "advanced": {
    "debug": false
  },
  "experimental": {
    "features": []
  },
  "skills": {
    "enabled": true
  },
  "hooks": {
    "preCommand": [],
    "postCommand": []
  },
  "telemetry": {
    "enabled": false
  }
}
```

## Environment Variables

### Authentication

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Gemini API key (from aistudio.google.com/apikey) |
| `GOOGLE_API_KEY` | Google API key (for Vertex AI) |
| `GOOGLE_GENAI_USE_VERTEXAI` | Set to `true` to use Vertex AI |
| `GOOGLE_CLOUD_PROJECT` | GCP project ID (for licensed users) |

### Model Configuration

| Variable | Description |
|----------|-------------|
| `GEMINI_MODEL` | Default model |
| `GEMINI_MAX_TOKENS` | Max output tokens |

### Other Settings

| Variable | Description |
|----------|-------------|
| `GEMINI_DEBUG` | Enable debug mode (1/true) |
| `GEMINI_SANDBOX` | Enable sandbox mode (1/true) |
| `NO_COLOR` | Disable colored output |

### Examples

```bash
# Set API key (from aistudio.google.com/apikey)
export GEMINI_API_KEY="your-api-key"

# Use specific model
export GEMINI_MODEL="gemini-2.5-flash"

# Enable debug mode
export GEMINI_DEBUG=1

# Vertex AI setup
export GOOGLE_API_KEY="your-api-key"
export GOOGLE_GENAI_USE_VERTEXAI=true

# For Gemini Code Assist licensed users
export GOOGLE_CLOUD_PROJECT="my-project"
```

## GEMINI.md Project Instructions

Create `GEMINI.md` in project root to provide context and instructions.

### Structure

```markdown
# Project: My App

## Overview
Brief description of the project.

## Tech Stack
- TypeScript
- React
- Node.js

## Code Style
- Use functional components
- Prefer async/await over promises
- Follow ESLint rules

## Important Files
- `src/index.ts` - Entry point
- `src/config.ts` - Configuration
- `src/types/` - TypeScript types

## Commands
- `npm run dev` - Start development server
- `npm test` - Run tests
- `npm run build` - Build for production
```

### Best Practices

1. Keep it concise - focus on non-obvious information
2. Include project-specific conventions
3. List important files and their purposes
4. Document common commands
5. Note any quirks or gotchas

## MCP Server Configuration

### In settings.json

```json
{
  "mcp": {
    "servers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@anthropic/mcp-server-filesystem"],
        "env": {
          "ALLOWED_PATHS": "/home/user/projects"
        }
      },
      "github": {
        "command": "npx",
        "args": ["-y", "@anthropic/mcp-server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Using /mcp Command

```bash
# List servers
/mcp

# Add server
/mcp add myserver npx -y @my/mcp-server

# Remove server
/mcp remove myserver
```

### Server Configuration Fields

| Field | Type | Description |
|-------|------|-------------|
| `command` | string | Executable command |
| `args` | array | Command arguments |
| `env` | object | Environment variables |
| `cwd` | string | Working directory |
