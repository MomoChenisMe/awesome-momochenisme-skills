# Awesome MomoChenIsMe Skills

A collection of Claude Code skills for productivity, content creation, and development workflows.

## Skills Overview

| Skill | Description |
|-------|-------------|
| **Sync Scribe** | Note-taking and todo management |
| **MomoChenIsMe Writing Style** | Blog writing style guide (Traditional Chinese) |
| **Conventional Commit** | Git commit messages following Conventional Commits v1.0.0 |
| **UI/UX Pro Max** | Comprehensive UI/UX design intelligence |
| **Skill Creator** | Guide for creating effective Claude Code skills |
| **Plugin Creator** | Guide for creating Claude Code plugins |
| **Claude Code CLI Guide** | Complete CLI usage reference |
| **OpenSpec Workflow** | Spec-driven development workflow methodology and decision framework |
| **Gemini CLI Guide** | Complete Gemini CLI usage reference |

---

## Sync Scribe

A simplified note-taking and todo management skill for Claude Code.

### Features

- **Auto-categorization**: Automatically determines if input is a todo or note
- **Todo management**: Add, complete, and delete tasks
- **Note management**: Categorized notes with timestamps
- **Search & filter**: Find items by keyword or category

### Usage

#### Slash Commands

| Command | Description |
|---------|-------------|
| `/add-todo <task>` | Add a new todo |
| `/complete-todo <keyword>` | Mark as complete |
| `/list-todos [filter]` | List all todos |
| `/delete-todo <keyword>` | Remove a todo |
| `/add-note <content>` | Add a new note |
| `/list-notes [category\|keyword]` | List notes |
| `/delete-note <keyword>` | Remove a note |

#### Natural Language

Just say:
- "Remember to buy milk" → Adds to todos
- "Note: the coffee shop was great" → Adds to notes
- "Buying milk is done" → Marks complete

### Data Storage

- `TODOS.md` - Todo list
- `NOTES.md` - Categorized notes

Files are stored in your workspace root.

---

## MomoChenIsMe Writing Style

A skill that mimics the unique writing style of MomoChenIsMe blogger for technical articles.

### Features

- **Conversational tone**: Friendly, approachable writing like chatting with a friend
- **Moderate humor**: Light self-deprecating humor with frequent use of "XD"
- **Practice-oriented**: Emphasizes "how to do" over abstract theory
- **Language style**: Traditional Chinese with English technical terms preserved

### Suitable Article Types

- **Technical tutorials**: Step-by-step guides with screenshots and code blocks
- **Product reviews**: Tool introductions with honest pros and cons
- **Personal reflections**: Experience sharing with lessons learned
- **Year-end reviews**: Timeline-based retrospectives

### Usage

Trigger naturally by asking Claude:
- "Use MomoChenIsMe style to write a Docker tutorial"
- "Introduce this tool in MomoChenIsMe style"
- "Write a year-end review in MomoChenIsMe's voice"

### Style Highlights

| Element | Usage |
|---------|-------|
| **Bold** | Emphasis on keywords |
| `Code` | Technical terms and commands |
| > Quote | Important callouts |

---

## Conventional Commit

Write git commit messages following the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### Features

- **Complete specification**: All 16 rules with RFC 2119 keywords
- **Type system**: 10 standard types (feat, fix, build, chore, ci, docs, style, refactor, perf, test) with SemVer mapping
- **BREAKING CHANGE**: Dual mechanism support (`!` suffix and footer)
- **Footer format**: Git trailer convention with common tokens
- **Writing guidelines**: Imperative mood, 72-char limit, "why not what" principle
- **Rich examples**: 13+ examples covering all types and scenarios

### Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Standard Types

| Type | Purpose | SemVer |
| --- | --- | --- |
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `build` | Build system / external deps | — |
| `chore` | Maintenance tasks | — |
| `ci` | CI configuration | — |
| `docs` | Documentation only | — |
| `style` | Code formatting (NOT CSS) | — |
| `refactor` | Code restructuring | — |
| `perf` | Performance improvement | — |
| `test` | Tests | — |

### References

- [specification.md](skills/conventional-commit/references/specification.md) - Full v1.0.0 specification, BNF grammar, SemVer correlation, and FAQ

---

## UI/UX Pro Max

> Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

AI-powered comprehensive UI/UX design intelligence for building professional interfaces.

### Features

- **67 design styles**: From minimalist to brutalist, covering all major design aesthetics
- **96 color palettes**: Industry-specific and mood-based color systems
- **Industry-specific rules**: Tailored design patterns for different sectors
- **Accessibility compliance**: WCAG guidelines integration
- **Responsive design**: Mobile-first and adaptive layout patterns

### Usage

Trigger naturally by asking Claude:

- "Design a dashboard for a SaaS product"
- "Create a landing page with a modern minimalist style"
- "Build a mobile app UI for a fitness tracker"

---

## Skill Creator

> Source: [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

A comprehensive guide for creating effective Claude Code skills.

### Features

- **Skill anatomy**: SKILL.md structure, frontmatter, and body guidelines
- **Resource bundling**: Scripts, references, and assets organization
- **Progressive disclosure**: Three-level loading system for context efficiency
- **Best practices**: Concise writing, appropriate degrees of freedom

### Key Concepts

- **SKILL.md**: Required file with YAML frontmatter (name, description) and Markdown body
- **scripts/**: Executable code for deterministic, repetitive tasks
- **references/**: Documentation loaded on-demand into context
- **assets/**: Files used in output (templates, images, fonts)

### Workflow

1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize with `scripts/init_skill.py`
4. Edit SKILL.md and implement resources
5. Package with `scripts/package_skill.py`
6. Iterate based on real usage

---

## Plugin Creator

A guide for creating Claude Code plugins - distributable packages that bundle skills, hooks, and MCP servers.

### Features

- **Plugin structure**: Directory layout and manifest configuration
- **Component types**: Commands, skills, hooks, MCP servers, LSP servers
- **Initialization script**: Quick plugin scaffolding
- **Testing guide**: Local plugin loading and debugging

### When to Use Plugin vs Standalone

| Use Case | Recommended |
|----------|-------------|
| Single project only | Place in `.claude/` |
| Share across projects | Create a Plugin |
| Distribute to others | Create a Plugin |

### Quick Start

```bash
# Create new plugin
python skills/plugin-creator/scripts/init_plugin.py my-plugin

# Test local plugin
claude --plugin-dir ./my-plugin
```

### Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # Manifest (required)
├── commands/            # User-invocable skills
├── skills/              # Agent skills
├── hooks/               # Hook configurations
└── README.md
```

---

## Claude Code CLI Guide

Complete reference for Claude Code CLI commands and flags.

### Basic Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive REPL |
| `claude "query"` | Start REPL with initial prompt |
| `claude -p "query"` | One-shot query (pipe/SDK mode) |
| `claude -c` | Continue most recent conversation |
| `claude -r <id>` | Resume specific session |
| `claude config` | Configuration management |
| `claude mcp` | MCP server configuration |
| `claude update` | Update to latest version |

### Common Flags

| Flag | Description |
|------|-------------|
| `-p, --print` | One-shot query mode |
| `-c, --continue` | Continue recent conversation |
| `--model <name>` | Specify model (opus/sonnet/haiku) |
| `--output-format <fmt>` | Output format (text/json/stream-json) |
| `--max-turns <n>` | Limit agent turns |
| `--verbose` | Verbose logging |

### References

- [commands.md](skills/claude-code-cli-guide/references/commands.md) - All commands explained
- [flags.md](skills/claude-code-cli-guide/references/flags.md) - All flags by category
- [examples.md](skills/claude-code-cli-guide/references/examples.md) - Common usage examples

---

## Gemini CLI Guide

Complete reference for Gemini CLI commands and configuration.

### Basic Commands

| Command | Description |
|---------|-------------|
| `gemini` | Start interactive REPL |
| `gemini "query"` | Start REPL with initial prompt |
| `gemini -p "query"` | One-shot query (pipe mode) |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/chat` | Start new conversation |
| `/resume` | Restore previous conversation |
| `/save` | Save current conversation |
| `/memory` | Show active memories |

### Common Flags

| Flag | Description |
|------|-------------|
| `-p, --prompt` | One-shot query mode |
| `-m, --model` | Specify model |
| `-s, --sandbox` | Enable sandbox mode |
| `--approval-mode` | Set approval mode (default/auto_edit/plan/yolo) |
| `--output-format` | Output format (text/json/stream-json) |
| `-d, --debug` | Enable debug mode |

### References

- [commands.md](skills/gemini-cli-guide/references/commands.md) - All commands explained
- [flags.md](skills/gemini-cli-guide/references/flags.md) - All CLI flags by category
- [configuration.md](skills/gemini-cli-guide/references/configuration.md) - Settings and MCP configuration
- [examples.md](skills/gemini-cli-guide/references/examples.md) - Common usage examples

---

## OpenSpec Workflow

A spec-driven collaborative development workflow framework. Guides you through the right workflow based on requirement clarity and scope.

### Key Concepts

- **Workflow Selection**: Decision tree to choose between Quick Feature, Exploratory, or Parallel Changes workflows
- **Artifact Generation Strategy**: One-shot vs step-by-step artifact creation based on complexity
- **Change Lifecycle**: Proposal → Delta Specs → Design → Tasks → Implement → Verify → Archive
- **Verification Dimensions**: Completeness, Correctness, Coherence
- **Update vs Restart**: When to refine an existing change vs start fresh

### Usage

Trigger naturally by asking Claude:

- "I want to plan a new feature using OpenSpec"
- "Should I use quick feature or exploratory workflow?"
- "Help me write a proposal for this change"

---

## Other Recommended Skills

A curated list of useful Claude Code skills from the community.

- [View Full List](RECOMMENDED_SKILLS.md)

---

## Installation

```bash
# Local development
claude --plugin-dir ./
```

## File Structure

```
awesome-momochenisme-skills/
├── README.md
├── README_zh.md
├── RECOMMENDED_SKILLS.md
├── RECOMMENDED_SKILLS_zh.md
├── .gitignore
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── add-todo.md
│   ├── complete-todo.md
│   ├── list-todos.md
│   ├── delete-todo.md
│   ├── add-note.md
│   ├── list-notes.md
│   └── delete-note.md
└── skills/
    ├── sync-scribe/
    │   └── SKILL.md
    ├── momochenisme-writing-style/
    │   ├── SKILL.md
    │   └── references/
    ├── conventional-commit/
    │   ├── SKILL.md
    │   └── references/
    ├── ui-ux-pro-max/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── data/
    ├── openspec-workflow/
    │   ├── SKILL.md
    │   └── references/
    ├── skill-creator/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── references/
    ├── plugin-creator/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── references/
    ├── claude-code-cli-guide/
    │   ├── SKILL.md
    │   └── references/
    └── gemini-cli-guide/
        ├── SKILL.md
        └── references/
```

## License

MIT License
