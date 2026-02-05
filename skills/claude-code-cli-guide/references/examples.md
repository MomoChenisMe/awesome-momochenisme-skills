# Common Usage Examples

## Table of Contents
- [Pipe Processing](#pipe-processing)
- [Automation Scripts](#automation-scripts)
- [System Prompt Customization](#system-prompt-customization)
- [Permission Control](#permission-control)
- [Multi-Directory Work](#multi-directory-work)
- [Useful Aliases](#useful-aliases)

## Pipe Processing

```bash
# Analyze files
cat src/main.py | claude -p "Explain this code"
cat config.json | claude -p "Check for configuration issues"

# Process command output
git diff | claude -p "Summarize changes"
npm test 2>&1 | claude -p "Explain test failures"
tail -100 app.log | claude -p "Find anomaly patterns"
```

## Automation Scripts

```bash
# Basic automation
#!/bin/bash
git diff --cached | claude -p "Review changes" --max-turns 3

# JSON output processing
RESULT=$(claude -p "List dependencies" --output-format json)
echo "$RESULT" | jq '.dependencies[]'

# CI/CD integration
PR_DIFF=$(gh pr diff $PR_NUMBER)
echo "$PR_DIFF" | claude -p "Review this PR" \
  --output-format json \
  --allowedTools "Read,Glob,Grep"
```

## System Prompt Customization

```bash
# Language settings
claude --append-system-prompt "Respond in formal English"

# Domain expertise
claude --system-prompt "You are a React/TypeScript expert"
claude --system-prompt "You are a DevOps engineer familiar with Docker and K8s"

# Output style
claude --append-system-prompt "Keep responses under 3 sentences"
claude --append-system-prompt "Use Markdown formatting"
```

## Permission Control

```bash
# Read-only analysis
claude --allowedTools "Read,Glob,Grep" -p "Analyze architecture"

# Disable dangerous operations
claude --disallowedTools "Bash,Write" -p "Review code"

# Full automation (controlled environments only)
claude --dangerously-skip-permissions -p "task" --max-turns 10
```

## Multi-Directory Work

```bash
# Cross-project analysis
claude --add-dir ../project-a --add-dir ../project-b \
  -p "Compare architecture differences"

# Reference shared libraries
claude --add-dir ../shared-utils -p "Refactor using utils"
```

## Useful Aliases

```bash
# Git commit helper
alias gc='git diff --cached | claude -p "Generate conventional commit message"'

# Code explanation
explain() { cat "$1" | claude -p "Explain this code"; }

# Test generation
gentest() { cat "$1" | claude -p "Generate unit tests"; }
```
