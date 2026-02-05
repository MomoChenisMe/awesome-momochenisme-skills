# Common Usage Examples

## Table of Contents
- [Basic Usage](#basic-usage)
- [Pipe Processing](#pipe-processing)
- [File Context](#file-context)
- [Automation Scripts](#automation-scripts)
- [Configuration Examples](#configuration-examples)
- [Useful Aliases](#useful-aliases)

## Basic Usage

```bash
# Start interactive session
gemini

# Start with initial prompt
gemini "Help me debug this project"

# One-shot query
gemini -p "What is TypeScript?"

# Use specific model
gemini -m gemini-2.5-flash -p "Quick question"
```

## Pipe Processing

### File Analysis

```bash
# Explain code
cat src/main.py | gemini -p "Explain this code"

# Check configuration
cat config.json | gemini -p "Validate this configuration"

# Analyze logs
cat app.log | gemini -p "Find error patterns"
```

### Git Integration

```bash
# Summarize changes
git diff | gemini -p "Summarize these changes"

# Review staged changes
git diff --cached | gemini -p "Review this code"

# Explain commit history
git log --oneline -20 | gemini -p "Summarize recent changes"

# Generate commit message
git diff --cached | gemini -p "Generate a conventional commit message"
```

### Command Output

```bash
# Analyze test failures
npm test 2>&1 | gemini -p "Explain test failures"

# Debug errors
npm run build 2>&1 | gemini -p "Why is this failing?"

# Analyze logs
tail -100 /var/log/app.log | gemini -p "Find anomalies"

# Process data
curl -s api.example.com/data | gemini -p "Summarize this data"
```

## File Context

### @ Syntax

```bash
# Single file
gemini "Refactor @src/utils.ts to be more efficient"

# Multiple files
gemini "@src/index.ts @src/types.ts Check for type errors"

# Directory
gemini "@src/ What's the architecture of this project?"

# Glob patterns
gemini "@src/*.ts Review all TypeScript files"
```

### Combined with Queries

```bash
# Code review
gemini "@src/api.ts @tests/api.test.ts Are tests comprehensive?"

# Documentation
gemini "@README.md @src/ Update README to match current code"

# Migration
gemini "@package.json @src/ Upgrade to latest dependencies"
```

## Automation Scripts

### Basic Automation

```bash
#!/bin/bash
# code-review.sh - Automated code review

git diff --cached | gemini -p "Review this code for:
1. Bugs and errors
2. Security issues
3. Performance problems
4. Code style"
```

### JSON Output Processing

```bash
#!/bin/bash
# analyze.sh - Process JSON output

RESULT=$(gemini -p "List project dependencies" --output-format json)
echo "$RESULT" | jq '.dependencies[]'
```

### CI/CD Integration

```bash
#!/bin/bash
# pr-review.sh - PR review in CI

PR_DIFF=$(gh pr diff "$PR_NUMBER")
echo "$PR_DIFF" | gemini -p "Review this PR" \
  --output-format json \
  -s  # sandbox mode for safety
```

### Batch Processing

```bash
#!/bin/bash
# batch-docs.sh - Generate docs for all files

for file in src/*.ts; do
  echo "Processing $file..."
  gemini -p "Generate JSDoc comments for @$file" \
    --approval-mode auto-edit
done
```

## Configuration Examples

### Minimal settings.json

```json
{
  "model": {
    "name": "gemini-2.5-flash"
  },
  "ui": {
    "theme": "dark"
  }
}
```

### Full settings.json

```json
{
  "general": {
    "vimMode": true,
    "checkpointing": true
  },
  "ui": {
    "theme": "dark",
    "hideBanner": true
  },
  "model": {
    "name": "gemini-2.5-pro",
    "maxSessionTurns": 100
  },
  "tools": {
    "sandbox": false,
    "allowed": ["read", "write", "shell", "web"],
    "exclude": []
  },
  "context": {
    "includeDirectories": ["src", "lib", "tests"]
  },
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-filesystem"]
    }
  },
  "telemetry": {
    "enabled": false
  }
}
```

### Environment Setup

```bash
# ~/.bashrc or ~/.zshrc

# Authentication
export GEMINI_API_KEY="your-api-key"

# Default model
export GEMINI_MODEL="gemini-2.5-pro"

# Or for Vertex AI
export GOOGLE_CLOUD_PROJECT="my-project"
```

## Useful Aliases

### Shell Aliases

```bash
# ~/.bashrc or ~/.zshrc

# Quick queries
alias g='gemini'
alias gp='gemini -p'
alias gf='gemini -m gemini-2.5-flash -p'

# Git helpers
alias gc='git diff --cached | gemini -p "Generate conventional commit message"'
alias gr='git diff | gemini -p "Review these changes"'

# Code helpers
alias explain='gemini -p "Explain this code" -i "$(cat)"'
alias review='gemini -p "Review this code" -i "$(cat)"'
```

### Shell Functions

```bash
# Explain a file
explain() {
  gemini "Explain @$1"
}

# Generate tests
gentest() {
  gemini "@$1 Generate comprehensive unit tests"
}

# Quick fix
fix() {
  gemini "@$1 Fix any bugs and improve code quality" \
    --approval-mode auto-edit
}

# Document a file
doc() {
  gemini "@$1 Add comprehensive documentation" \
    --approval-mode auto-edit
}
```

### Usage Examples

```bash
# Use aliases
gp "What is Rust?"
gf "Quick question about Python"
gc  # Generate commit message

# Use functions
explain src/main.ts
gentest src/utils.ts
fix src/buggy.py
doc src/api.ts
```
