# OpenSpec Quick Reference

## Command Overview

| Command | Purpose | Phase |
|---------|---------|-------|
| `/opsx:new` | Create new change | Planning |
| `/opsx:ff` | Fast-forward: generate all documents | Planning |
| `/opsx:continue` | Create next artifact in dependency chain | Planning |
| `/opsx:apply` | Execute implementation tasks | Implementation |
| `/opsx:verify` | Verify implementation matches specs | Verification |
| `/opsx:sync` | Sync delta specs to main specs | Maintenance |
| `/opsx:archive` | Archive completed change | Wrap-up |
| `/opsx:bulk-archive` | Bulk archive multiple changes | Wrap-up |
| `/opsx:explore` | Explore mode (think without implementing) | Analysis |
| `/opsx:onboard` | Onboarding tutorial | Learning |

## Workflow Diagram

```
                        ┌─────────────────┐
                        │  /opsx:onboard  │ ← New users start here
                        └────────┬────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   /opsx:new     │    │  /opsx:explore  │    │ /opsx:continue  │
│  Create change  │    │   Explore/Analyze│    │  Resume work    │
└────────┬────────┘    └─────────────────┘    └────────┬────────┘
         │                                             │
         ▼                                             │
┌─────────────────┐                                    │
│    /opsx:ff     │ ← Fast-forward: generate all docs  │
└────────┬────────┘                                    │
         │                                             │
         └─────────────────────┬───────────────────────┘
                               ▼
                    ┌─────────────────┐
                    │   /opsx:apply   │
                    │ Execute tasks   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  /opsx:verify   │
                    │ Verify impl     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   /opsx:sync    │ ← Optional: sync delta specs
                    └────────┬────────┘
                             │
         ┌───────────────────┴───────────────────┐
         ▼                                       ▼
┌─────────────────┐                    ┌──────────────────┐
│ /opsx:archive   │                    │/opsx:bulk-archive│
│ Single archive  │                    │ Batch archive    │
└─────────────────┘                    └──────────────────┘
```

## Common Scenarios

### Scenario 1: New Feature Development (Standard Flow)

```
/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive
```

### Scenario 2: Quick Small Change

```
/opsx:new → /opsx:ff → /opsx:apply → /opsx:archive
```

### Scenario 3: Resume Interrupted Work

```
/opsx:continue → /opsx:apply → /opsx:verify → /opsx:archive
```

### Scenario 4: Explore Complex Problem First

```
/opsx:explore → /opsx:new → /opsx:ff → /opsx:apply → /opsx:verify
```

### Scenario 5: Bulk Cleanup Completed Changes

```
/opsx:bulk-archive
```

## Four-Layer Document Structure

```
.openspec/changes/<change-id>/
├── proposal.md      ← Purpose and changes
├── specs/           ← Requirements specs
│   └── *.spec.md    ← Delta specs (incremental)
├── design.md        ← Technical design
└── tasks.md         ← Implementation checklist
```

| File | Purpose | Key Content |
|------|---------|-------------|
| `proposal.md` | Explain change motivation and scope | Why, What, Scope |
| `specs/*.spec.md` | Define requirements and scenarios | User stories, acceptance criteria |
| `design.md` | Technical implementation approach | Architecture, API, data structures |
| `tasks.md` | Implementation step checklist | Checkable task items |

## Core Principles Cheatsheet

**Three Principles**:
- Fluid, not rigid
- Iterative, not waterfall
- Simple, not complex

**Delta Specs Concept**:
- Incremental spec files in the `specs/` directory
- Describe only what's added or modified in this change
- Can be synced to main specs via `/opsx:sync`
