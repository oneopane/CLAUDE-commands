---
allowed-tools: Bash(git branch), Bash(git checkout), Bash(git status), Bash(git add), Bash(git commit), Bash(grep), Bash(sed), DesktopCommander(*)
description: Execute tasks from any markdown plan document with checkboxes
---

Implement tasks from a markdown plan file, automatically tracking progress and committing changes.

## Phase 1: Initialize

1. **Pre-flight Check**
   - Verify plan has been validated:
     - Check for Branch specification
     - Check for Metadata section
     - Verify checkbox presence
   - If missing required elements:
     ```
     ERROR: Plan document is not properly formatted.
     Please run: /user:validate-plan ${ARGUMENTS}
     ```

2. **Load Plan Context**
   - Read Branch specification
   - Parse Metadata (Created, Status, Type)
   - Check Status field:
     - If "completed": warn and confirm continuation
     - If "paused": show last completion date
     - If "active": proceed normally

3. **Branch Management**
   - Checkout specified branch (create if needed)
   - Verify we're on correct branch
   - Show git status

4. **Progress Overview**
   - Parse Progress section if present
   - Show current completion status:
     ```
     Plan: Authentication System Implementation
     Type: feature
     Branch: feature/implement-auth-system
     Progress: 3/15 tasks (20%)
     Last updated: 2024-01-14
     ```

## Phase 2: Parse Plan Structure

1. **Identify Task Format**
   - Find all checkbox items: `- [ ]` or `- [x]`
   - Detect hierarchy (nested lists, sections, phases)
   - Count total tasks vs completed tasks

2. **Extract Metadata**
   - Look for common patterns:
     - Time estimates: `[2h]`, `(30min)`, `~1 day`
     - Priority indicators: 🔴🟡🟢⚪, HIGH/MEDIUM/LOW
     - File references: `file:`, `path:`, backticks
     - Task IDs: `#123`, `TASK-456`

3. **Build Task List**
   - Create ordered list of uncompleted tasks
   - Preserve context (section headers, parent tasks)
   - Note any explicit dependencies

## Phase 3: Task Selection

1. **Find Next Task**
   - Select first unchecked task in document order
   - Or respect priority if indicators present
   - Show task with full context:
   ```
   Next task from "Project Setup" section:
   
   - [ ] Configure database connection
     - Update config/database.yml
     - Set environment variables
     - Test connection
   
   Proceed? [Y/n/skip/browse]
   ```

2. **Browse Option**
   - Allow viewing all unchecked tasks
   - Let user select specific task
   - Support jumping to different sections

## Phase 4: Implementation

1. **Present Task Context**
   - Show the full task description
   - Display any subtasks or details
   - Highlight mentioned files or code

2. **Execute Implementation**
   - If files are mentioned, open and edit them
   - Allow user to describe what was done
   - Support multi-file changes

3. **Capture Changes**
   - Track all modified files
   - Show diff of changes
   - Confirm implementation is complete

## Phase 5: Update Plan

1. **Mark Task Complete**
   - Check the box: `- [ ]` → `- [x]`
   - Add completion annotation:
     ```markdown
     - [x] Configure database connection ✓ 2024-01-15
     ```

2. **Update Progress Section**
   - Locate Progress section
   - Update counters:
     ```markdown
     ## Progress
     - Overall: 4/15 tasks (27%)  ← was 3/15 (20%)
     - Setup: 2/3 tasks           ← if task was in Setup
     ```
   - Recalculate all percentages

3. **Update Metadata**
   - Update last modified date in metadata
   - If all tasks complete, update Status:
     ```markdown
     Status: completed  ← was active
     Completed: 2024-01-15
     ```

4. **Add Implementation Notes**
   - For significant changes, add to task:
     ```markdown
     - [x] Configure database connection ✓ 2024-01-15
       > Note: Used PostgreSQL 14, added connection pooling
     ```

## Phase 6: Commit

1. **Prepare Commit**
   - Stage all changed files
   - Stage updated plan document
   - Generate commit message based on Type from metadata:
     - feature: `feat: <task description>`
     - bugfix: `fix: <task description>`
     - refactor: `refactor: <task description>`
     - migration: `chore: <task description>`

2. **Commit Format**
   ```bash
   git commit -m "<type>: <task description>

   - <summary of changes>
   - Update progress in <plan-file> (4/15 tasks)
   
   Plan: <plan-file>
   Branch: <branch-name>
   Progress: <new-percentage>%"
   ```

3. **Auto-pause Check**
   - If session has been long (>2 hours):
     ```
     You've completed 5 tasks in this session.
     Consider taking a break? [continue/pause]
     ```
   - If pause, update Status to "paused" with timestamp

## Phase 7: Continue

1. **Completion Check**
   - If all tasks complete:
     ```
     🎉 Plan completed!
     
     Summary:
     - Total tasks: 15
     - Time taken: 2 days
     - Branch: feature/implement-auth-system
     
     Next steps:
     1. Create pull request
     2. Archive plan (move to plans/completed/)
     3. Start new plan
     ```

2. **Continue Options**
   ```
   Task completed!
   Progress: 5/20 tasks (25%)
   Status: active
   Estimated remaining: ~12 hours
   
   1. Continue with next task
   2. Browse remaining tasks
   3. View updated plan
   4. Pause work (update status)
   5. End session
   
   Choice:
   ```

3. **Session Summary**
   - When ending, show:
     - Tasks completed this session
     - Progress delta (was 20%, now 35%)
     - Time estimates vs actual
     - Status update if paused

## Special Handlers

1. **Multi-Step Tasks**
   - If task has nested checkboxes, handle as subtasks
   - Only mark parent complete when all children done

2. **Code Blocks**
   - If task contains code blocks, offer to apply them
   - Support file creation from embedded code

3. **External References**
   - Handle URLs, issue numbers, PR references
   - Fetch context if needed

<rules>

- MUST verify plan has required elements (Branch, Metadata, Checkboxes)
- MUST refuse to proceed if plan not validated
- MUST use Branch specification from document
- MUST update Progress section after each task
- MUST update Metadata (last modified, status changes)
- MUST use Type field for commit message prefixes
- MUST handle Status field (active/paused/completed)
- MUST commit both implementation and plan updates together
- SHOULD track session duration for break reminders
- SHOULD calculate estimated remaining effort
- SHOULD auto-archive completed plans
- SHOULD show progress deltas in summaries
- MAY add implementation notes to tasks
- MAY skip tasks that are blocked
- MAY allow browsing and selecting specific tasks

</rules>