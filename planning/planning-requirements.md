# Planning Document Requirements Specification

## Core Requirements (Mandatory)

### 1. Branch Specification
**Format:** 
```markdown
Branch: feature/descriptive-name
```
- Must appear at the beginning of the document
- Used for version control during implementation
- Format: `Branch: <branch-type>/<descriptive-name>`
- Branch types typically: feature, bugfix, refactor, chore

### 2. Document Title
**Format:**
```markdown
# Plan Title
```
- Must be a level 1 markdown heading
- Should clearly describe the plan's purpose

### 3. Metadata Section
**Format:**
```markdown
Created: YYYY-MM-DD
Status: active|completed|paused
Type: refactor|feature|bugfix|migration|other
```- **Created**: Date when plan was created (YYYY-MM-DD format)
- **Status**: Current state of the plan
  - `active`: Currently being worked on
  - `completed`: All tasks finished
  - `paused`: Temporarily halted (with timestamp)
- **Type**: Category of work, used for commit message prefixes
  - `feature` → `feat:` prefix
  - `bugfix` → `fix:` prefix
  - `refactor` → `refactor:` prefix
  - `migration` → `chore:` prefix
  - `other` → generic commit messages

### 4. Checkbox Tasks
**Format:**
```markdown
- [ ] Uncompleted task
- [x] Completed task
```
- Must have at least one checkbox item
- Can be nested for subtasks
- Properly formatted markdown lists
- Can include task metadata (see Task Metadata section)

## Recommended Sections

### 5. Progress Tracking
**Format:**
```markdown
## Progress
- Overall: 0/10 tasks (0%)
- Phase 1: 0/5 tasks
- Phase 2: 0/5 tasks
```- Automatically updated by implementation commands
- Shows completion status at various levels
- Helps track work across sessions

### 6. Task Organization
- Clear sections or phases using markdown headers
- Logical grouping of related tasks
- Consistent formatting throughout
- Hierarchical structure for complex plans

## Task Metadata (Optional)

Tasks can include additional metadata for better tracking:

### Time Estimates
```markdown
- [ ] Implement user authentication [2h]
- [ ] Create database schema (30min)
- [ ] Refactor API endpoints ~1 day
```

### Priority Indicators
```markdown
- [ ] 🔴 Fix critical security bug
- [ ] 🟡 Update documentation
- [ ] 🟢 Add unit tests
- [ ] HIGH: Implement core feature
- [ ] MEDIUM: Improve performance
- [ ] LOW: Code cleanup
```
### File References
```markdown
- [ ] Update configuration
  - file: config/database.yml
  - path: src/models/user.js
  - Modify `app.config.js`
```

### Dependencies
```markdown
- [ ] Create user model
- [ ] Implement user API endpoints
  - depends on: Create user model
  - requires: Database connection setup
  - after: Authentication middleware
```

### Completion Annotations
```markdown
- [x] Configure database connection ✓ 2024-01-15
- [x] Set up testing framework ✓ 2024-01-15
  > Note: Used Jest with React Testing Library
```

## Parallel Execution Requirements

For plans that will be executed in parallel, additional metadata is required:

### 7. Parallelization Strategy
```markdown
## Parallelization Strategy

Agents: 3
Estimated Sequential Time: 14 hours
Estimated Parallel Time: 6 hours
Speedup: 2.3x
```
### 8. Stage Definitions
```markdown
### Stage Definitions

#### Stage 1: Independent Setup (3 agents)
Duration: 2 hours
Tasks:
- [ ] [Agent1] Initialize project structure
- [ ] [Agent2] Set up frontend framework
- [ ] [Agent3] Configure CI/CD pipeline

#### Stage 2: Core Development (3 agents)
Duration: 3 hours
Depends on: Stage 1
```

### 9. Task Metadata for Parallel Execution
```markdown
- [ ] Create user model
  - agent: backend-specialist
  - stage: 2
  - depends_on: ["database-schema"]
  - provides: ["user-model-interface"]
  - estimated_time: 45min
  - files: ["src/models/user.js", "src/models/index.js"]
```

### 10. Coordination Protocol
```markdown
## Coordination Protocol

### Agent Communication
- Status updates: .claude/status/<agent-id>.json
- Shared interfaces: .claude/interfaces/
- Lock files: .claude/locks/<resource>.lock
### Branch Strategy  
- Main branch: feature/implement-auth-system
- Agent branches: feature/implement-auth-system-<agent-id>
- Merge points: After each stage completion

### Conflict Resolution
- File conflicts: Later agent rebases
- Logic conflicts: Designated resolver (Agent1)
- API conflicts: Interface negotiation required
```

## Format Requirements

### Document Structure
- Consistent markdown formatting
- Proper heading hierarchy (H1 → H2 → H3)
- Clear separation between sections
- Logical flow from overview to details

### Task Formatting
- One task per checkbox line
- Subtasks properly indented
- Clear, actionable task descriptions
- Consistent checkbox formatting (`- [ ]` not `* [ ]` or other variants)

### Best Practices
- Keep task descriptions concise but complete
- Include enough context to understand the task
- Group related tasks together
- Use descriptive section headers
- Maintain consistent terminology throughout
## Validation Rules

A plan document is considered valid when:

1. **All mandatory sections present**:
   - ✓ Branch specification exists
   - ✓ Document has a title (H1 heading)
   - ✓ Metadata section with all three fields
   - ✓ At least one checkbox task

2. **Proper formatting**:
   - ✓ Branch follows format: `Branch: <type>/<name>`
   - ✓ Metadata uses correct field names and values
   - ✓ Checkboxes use standard markdown format
   - ✓ Consistent heading hierarchy

3. **Implementation ready**:
   - ✓ All tasks are actionable
   - ✓ No placeholder content (TBD, TODO without details)
   - ✓ File references are valid paths (if included)
   - ✓ Dependencies are clear (if specified)

4. **For parallel execution**:
   - ✓ All standard requirements met
   - ✓ Parallelization strategy defined
   - ✓ Stage definitions with agent assignments
   - ✓ Task metadata includes agent and stage
   - ✓ Coordination protocol specified
## Example Plan Structure

```markdown
Branch: feature/user-authentication

# User Authentication System Implementation

Created: 2024-01-15
Status: active
Type: feature

## Overview
Implement a complete user authentication system with JWT tokens.

## Progress
- Overall: 0/12 tasks (0%)
- Backend: 0/7 tasks
- Frontend: 0/5 tasks

## Phase 1: Backend Setup

- [ ] Create user model
  - file: src/models/user.js
  - estimated_time: 45min
  
- [ ] Set up database migrations
  - depends_on: ["Create user model"]
  - files: ["migrations/001-create-users.js"]

## Phase 2: API Implementation

- [ ] Implement registration endpoint [2h]
  - path: src/api/auth/register.js
  - depends_on: ["Create user model"]
  
- [ ] Implement login endpoint [1.5h]
  - path: src/api/auth/login.js
  - depends_on: ["Create user model"]

## Phase 3: Frontend Integration

- [ ] Create login form component
  - file: src/components/LoginForm.jsx
  - depends_on: ["Implement login endpoint"]
  
- [ ] Add authentication context
  - file: src/contexts/AuthContext.jsx
```

This specification ensures that planning documents are properly structured for both sequential and parallel execution by the Claude Code commands.