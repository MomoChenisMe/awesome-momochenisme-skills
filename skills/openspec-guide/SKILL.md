---
name: openspec-guide
description: OpenSpec usage guide and workflow reference. Triggers when users ask about OpenSpec, including: (1) how to use /opsx commands, (2) OpenSpec workflow explanations, (3) Spec-Driven Development (SDD) best practices, (4) purpose and format of proposal, specs, design, and tasks files, (5) delta specs concepts and usage.
---

# OpenSpec User Guide

OpenSpec is a lightweight Spec-Driven Development (SDD) framework. Core philosophy: **fluid not rigid, iterative not waterfall, simple not complex**.

## Four-Layer Document Structure

```
.openspec/changes/<change-id>/
├── proposal.md      # Purpose and changes (Why & What)
├── specs/           # Requirements specifications (delta specs)
│   └── *.spec.md    # Incremental spec files
├── design.md        # Technical approach (How)
└── tasks.md         # Implementation checklist
```

## Command Quick Reference

| Command | Purpose |
|---------|---------|
| `/opsx:new` | Create a new change |
| `/opsx:ff` | Fast-forward: generate all planning documents |
| `/opsx:continue` | Create next artifact in dependency chain |
| `/opsx:apply` | Execute implementation tasks |
| `/opsx:verify` | Verify implementation matches specs |
| `/opsx:sync` | Sync delta specs to main specifications |
| `/opsx:archive` | Archive completed change |
| `/opsx:bulk-archive` | Bulk archive multiple changes |
| `/opsx:explore` | Explore mode (think without implementing) |
| `/opsx:onboard` | Onboarding tutorial for new users |

### Command Syntax by Tool

OpenSpec supports 21+ AI coding tools with tool-specific syntax:

| Tool | Syntax |
|------|--------|
| Claude Code | `/opsx:command` |
| Cursor / Windsurf / Copilot | `/opsx-command` |
| Trae | `/openspec-command-name` |

Other supported tools include: Amazon Q Developer, Antigravity, Auggie, Cline, CodeBuddy, Codex, Continue, CoStrict, Crush, Factory Droid, Gemini CLI, iFlow, Kilo Code, OpenCode, Qoder, Qwen Code, RooCode, and more.

> **Note**: Legacy commands (`/openspec:proposal`, `/openspec:apply`, `/openspec:archive`) were removed in v1.0.0.

## Typical Workflows

### Standard Flow

```
/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive
```

1. **Create change**: `/opsx:new` initializes the change directory
2. **Fast planning**: `/opsx:ff` generates proposal, specs, design, tasks
3. **Implement**: `/opsx:apply` writes code based on tasks.md
4. **Verify specs**: `/opsx:verify` confirms implementation matches specs
5. **Archive**: `/opsx:archive` completes and archives the change

### Resume Work

Use `/opsx:continue` to create the next artifact based on dependencies, automatically loading context and determining what to generate next.

### Explore Mode

Use `/opsx:explore` for technical research or evaluation **without modifying any files**. Once direction is confirmed, use `/opsx:new` to start a formal change.

## References

For detailed documentation:

- **Quick Reference**: [references/quick-reference.md](references/quick-reference.md) - Command overview, workflow diagrams, common scenarios
- **Command Details**: [references/command-details.md](references/command-details.md) - Complete documentation for all 10 commands with examples
