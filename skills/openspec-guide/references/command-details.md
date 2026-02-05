# OpenSpec Command Details

## 1. /opsx:new

**Purpose**: Create a new change and initialize the OpenSpec structure.

**When to use**:
- Starting a new feature development
- Major refactoring
- Fixing a bug that needs tracking

**Execution flow**:
1. Ask for change name or auto-generate one
2. Create `.openspec/changes/<change-id>/` directory
3. Initialize `proposal.md` template
4. Prepare for subsequent planning work

**Example conversation**:
```
User: /opsx:new add user authentication feature
Claude: Created change 'add-user-authentication'
        Change directory: .openspec/changes/add-user-authentication/
        Next, you can use /opsx:ff to quickly generate planning documents
```

**Notes**:
- Change name is converted to kebab-case format
- Recommend using descriptive names
- Focus on one change at a time

---

## 2. /opsx:ff

**Purpose**: Fast Forward - quickly generate all planning documents (proposal, specs, design, tasks).

**When to use**:
- Immediately after `/opsx:new`
- When quick complete planning is needed
- Small to medium changes

**Execution flow**:
1. Analyze change requirements
2. Generate `proposal.md` (change proposal)
3. Generate `specs/*.spec.md` (requirement specs)
4. Generate `design.md` (technical design)
5. Generate `tasks.md` (implementation task list)

**Example conversation**:
```
User: /opsx:ff
Claude: Generating planning documents for 'add-user-authentication'...
        ✓ proposal.md - Change proposal
        ✓ specs/auth-flow.spec.md - Authentication flow spec
        ✓ specs/session-management.spec.md - Session management spec
        ✓ design.md - Technical design document
        ✓ tasks.md - Implementation task list (12 tasks)
```

**Notes**:
- Ensure running after `/opsx:new`
- Complex changes may need manual review and adjustment
- Can run multiple times to update documents

---

## 3. /opsx:continue

**Purpose**: Create the next artifact based on dependencies in the change workflow.

**When to use**:
- After creating a proposal, to generate the next document (specs, design, or tasks)
- When artifacts have dependencies and you want to generate them in order
- Continuing a workflow where not all documents are yet created

**Execution flow**:
1. Analyze existing artifacts in the change directory
2. Determine which artifact to create next based on dependency chain
3. Generate the next required artifact
4. Update change status

**Example conversation**:
```
User: /opsx:continue
Claude: Analyzing change 'add-user-authentication'...

        Existing artifacts:
        - proposal.md (complete)
        - specs/auth-flow.spec.md (complete)

        Next artifact to create: design.md
        Generating technical design based on specs...
```

**Notes**:
- Follows the dependency chain: proposal → specs → design → tasks
- Automatically determines what needs to be created next
- Can directly specify change ID

---

## 4. /opsx:apply

**Purpose**: Execute implementation tasks based on tasks.md.

**When to use**:
- Starting implementation after planning is complete
- Continuing unfinished tasks
- Developing according to the checklist

**Execution flow**:
1. Read task list from `tasks.md`
2. Identify pending tasks
3. Execute tasks sequentially (write code, modify files, etc.)
4. Update task status (check off completed items)

**Example conversation**:
```
User: /opsx:apply
Claude: Executing implementation tasks for 'add-user-authentication'...

        Current task: Create User model
        - Creating models/user.ts
        - Adding fields: id, email, password_hash, created_at

        [In progress...]
```

**Notes**:
- Will modify actual code
- Updates tasks.md after completing each task
- Pauses and asks when encountering issues

---

## 5. /opsx:verify

**Purpose**: Verify implementation matches specifications (specs).

**When to use**:
- Verification after implementation is complete
- Confirming all requirements are met
- Final check before archiving

**Execution flow**:
1. Read all specs in `specs/` directory
2. Compare with actual implementation
3. Check if acceptance criteria are met
4. Generate verification report

**Example conversation**:
```
User: /opsx:verify
Claude: Verifying implementation for 'add-user-authentication'...

        ✓ auth-flow.spec.md
          - ✓ User can register a new account
          - ✓ User can login with email/password
          - ✓ System sends verification email

        ✗ session-management.spec.md
          - ✓ Session expires after 24 hours
          - ✗ User can manually logout all devices (not implemented)

        Verification result: 1/2 specs fully passed
```

**Notes**:
- Does not modify code, only checks
- Lists unmet conditions in detail
- Can use `/opsx:apply` to fix issues

---

## 6. /opsx:sync

**Purpose**: Sync delta specs to main specification files.

**When to use**:
- Organizing specs after change completion
- When main project docs need updating
- Maintaining document consistency

**Execution flow**:
1. Read delta specs in `specs/`
2. Identify content to merge
3. Update project main spec files
4. Mark synced delta specs

**Example conversation**:
```
User: /opsx:sync
Claude: Syncing delta specs...

        Source: .openspec/changes/add-user-authentication/specs/
        Target: specs/ (main specs directory)

        ✓ Merged auth-flow.spec.md → specs/authentication.spec.md
        ✓ Added session-management.spec.md

        Sync complete!
```

**Notes**:
- This is an optional step
- Suitable for long-term maintained projects
- Preserves change traceability

---

## 7. /opsx:archive

**Purpose**: Archive a completed change.

**When to use**:
- Change is fully completed and verified
- Cleaning up work directory
- Preserving historical records

**Execution flow**:
1. Confirm change is complete
2. Move change directory to archive area
3. Update archive index
4. Clean up work area

**Example conversation**:
```
User: /opsx:archive
Claude: Preparing to archive 'add-user-authentication'...

        Status check:
        - ✓ All tasks completed
        - ✓ Specs verification passed

        Confirm archive? This will move the change to .openspec/archive/

User: confirm
Claude: ✓ Archived to .openspec/archive/add-user-authentication/
```

**Notes**:
- History remains viewable after archiving
- Recommend archiving only after full confirmation
- Can specify change ID to archive directly

---

## 8. /opsx:bulk-archive

**Purpose**: Bulk archive multiple completed changes.

**When to use**:
- Multiple completed changes need cleanup
- Regular workspace maintenance
- Cleanup after project milestones

**Execution flow**:
1. Scan all change directories
2. Identify completed changes
3. Execute bulk archive
4. Generate archive report

**Example conversation**:
```
User: /opsx:bulk-archive
Claude: Found the following archivable changes:

        1. ✓ add-user-authentication (all tasks completed)
        2. ✓ fix-login-bug (all tasks completed)
        3. ✗ refactor-database (in progress, skipping)

        Will archive 2 changes, confirm?

User: confirm
Claude: ✓ Bulk archived 2 changes
```

**Notes**:
- Only archives fully completed changes
- In-progress changes are skipped
- Shows detailed archive list

---

## 9. /opsx:explore

**Purpose**: Explore mode - think and analyze without implementing.

**When to use**:
- Researching technical feasibility
- Analyzing existing code
- Thinking about architecture design
- When unsure whether to make a change

**Execution flow**:
1. Enter explore mode (no file modifications)
2. Analyze problem or research topic
3. Provide thoughts and recommendations
4. Ask whether to convert to formal change

**Example conversation**:
```
User: /opsx:explore evaluate whether database layer needs refactoring
Claude: [Explore Mode] Analyzing database layer...

        Issues found:
        1. Query logic scattered across multiple files
        2. Lack of connection pool management
        3. No unified error handling

        Recommended approaches:
        A. Introduce Repository pattern (medium effort)
        B. Use ORM framework (larger refactor)

        Would you like to create a formal change to address this?
```

**Notes**:
- **Does not modify any files**
- Suitable for early research and evaluation
- Can transition to `/opsx:new` anytime to start formal change

---

## 10. /opsx:onboard

**Purpose**: Onboarding tutorial introducing how to use OpenSpec.

**When to use**:
- First time using OpenSpec
- Need to review workflows
- Introducing project process to new members

**Execution flow**:
1. Introduce OpenSpec core concepts
2. Explain four-layer document structure
3. Demonstrate basic workflow
4. Provide common command reference

**Example conversation**:
```
User: /opsx:onboard
Claude: Welcome to OpenSpec! Let me introduce...

        What is OpenSpec?
        A lightweight Spec-Driven Development framework that helps you:
        - Clearly define change scope
        - Systematically track development progress
        - Ensure implementation matches specs

        Four-Layer Document Structure:
        1. proposal.md - Explain why to make this change
        2. specs/ - Define what to do
        3. design.md - Explain how to do it
        4. tasks.md - Track what's done

        Quick Start:
        1. /opsx:new - Create new change
        2. /opsx:ff - Quick generate planning documents
        3. /opsx:apply - Start implementation

        Need more information?
```

**Notes**:
- Suitable for new users
- Provides interactive tutorial
- Can ask specific topics for more information
