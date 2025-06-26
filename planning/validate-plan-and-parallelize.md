---
allowed-tools: Bash(grep), Bash(sed), Bash(head), Bash(tail), Bash(jq), DesktopCommander(*)
description: Validate plan documents and analyze them for parallel execution opportunities
---

Validate a markdown plan document, ensure it meets requirements for automated implementation, and analyze tasks to create an optimal parallelization strategy.

Requirements are defined in: @/Users/ojash/.claude/commands/CLAUDE-commands/planning/planning-requirements.md

## Phase 1: Standard Validation

Perform all standard validation checks from validate-plan:

1. **Required Elements**
   - Branch specification
   - Title and metadata
   - Checkbox tasks
   - Progress tracking

2. **Fix Issues Interactively**
   - Apply all fixes from standard validation
   - Ensure plan is implementation-ready

## Phase 2: Task Analysis

### Extract Task Graph

1. **Parse All Tasks**
   ```
   Analyzing task structure...
   
   Found 25 tasks across 4 sections:
   - Setup: 5 tasks
   - Backend Implementation: 10 tasks  
   - Frontend Implementation: 7 tasks
   - Testing: 3 tasks
   ```

2. **Identify Dependencies**
   
   Look for dependency indicators:
   - Explicit: "depends on:", "requires:", "after:"
   - Implicit: "use the", "from previous", "based on"
   - File-based: Tasks modifying same files
   - Logical: Database before API, API before frontend
   
   ```
   Dependency Analysis:
   
   Task: "Create user model"
     → No dependencies
   
   Task: "Implement user API endpoints"  
     → Depends on: "Create user model"
     → Reason: Explicit reference "use the user model"
   
   Task: "Add user authentication"
     → Depends on: "Implement user API endpoints"
     → Reason: Requires existing endpoints
   ```

3. **Resource Analysis**
   
   Identify shared resources:
   ```
   Resource Conflicts Detected:
   
   File: src/config/database.js
     - Modified by: "Configure database connection"
     - Modified by: "Add connection pooling"
     → These tasks must be sequential
   
   File: src/models/user.js
     - Created by: "Create user model"
     - Modified by: "Add validation rules"
     - Modified by: "Add user relationships"
     → Enforce ordering or merge strategy
   ```

## Phase 3: Parallelization Strategy

### Build Execution Stages

1. **Topological Sort**
   ```
   Calculating optimal execution order...
   
   Stage 1 (can run in parallel):
   - [ ] Initialize project structure
   - [ ] Set up development environment
   - [ ] Configure linting and formatting
   
   Stage 2 (can run in parallel):
   - [ ] Create database schema
   - [ ] Design API structure
   - [ ] Set up frontend framework
   
   Stage 3 (dependencies from Stage 2):
   - [ ] Create user model (depends: database schema)
   - [ ] Create product model (depends: database schema)
   - [ ] Set up routing (depends: API structure)
   ```

2. **Agent Assignment Strategy**
   ```
   Recommended Agent Distribution:
   
   Agent 1 (Backend Specialist):
   - Stage 1: Database and models
   - Stage 2: API implementation
   - Estimated time: 6 hours
   
   Agent 2 (Frontend Specialist):
   - Stage 1: UI framework setup
   - Stage 2: Component development  
   - Estimated time: 5 hours
   
   Agent 3 (Infrastructure):
   - Stage 1: DevOps setup
   - Stage 2: Testing framework
   - Estimated time: 3 hours
   
   Maximum parallelization: 3x speedup
   Critical path duration: 6 hours
   ```

3. **Coordination Points**
   ```
   Synchronization Required:
   
   Checkpoint 1 (after Stage 1):
   - All agents must complete setup tasks
   - Verify no conflicts in configuration
   
   Checkpoint 2 (after models):
   - Backend must share model interfaces
   - Frontend waits for API contracts
   
   Checkpoint 3 (integration):
   - All agents converge for integration tests
   ```

## Phase 4: Add Parallelization Metadata

### Enhance Plan Document

1. **Add Execution Metadata**
   ```markdown
   ## Parallelization Strategy
   
   Agents: 3
   Estimated Sequential Time: 14 hours
   Estimated Parallel Time: 6 hours
   Speedup: 2.3x
   
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
   Tasks:
   - [ ] [Agent1] Create database models
   - [ ] [Agent2] Build UI components
   - [ ] [Agent3] Set up testing framework
   ```

2. **Annotate Tasks with Metadata**
   ```markdown
   - [ ] Create user model
     - agent: backend-specialist
     - stage: 2
     - depends_on: ["database-schema"]
     - provides: ["user-model-interface"]
     - estimated_time: 45min
     - files: ["src/models/user.js", "src/models/index.js"]
   ```

3. **Add Coordination Instructions**
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

## Phase 5: Interactive Optimization

### Review with User

1. **Dependency Validation**
   ```
   QUESTION: Task "Add user authentication" was auto-detected
   to depend on "Create user model". Is this correct?
   
   1. Yes, keep dependency
   2. No, they're independent  
   3. Add more dependencies
   4. View task details
   
   Choice:
   ```

2. **Agent Specialization**
   ```
   SUGGESTION: Based on task analysis, optimal agent roles:
   
   1. Backend Specialist (10 tasks)
   2. Frontend Specialist (8 tasks)
   3. Full-Stack Generalist (7 tasks)
   
   Alternative: 2 Full-Stack agents (12-13 tasks each)
   
   Which configuration do you prefer?
   ```

3. **Risk Assessment**
   ```
   ATTENTION: Parallel execution risks identified:
   
   1. Database migrations (HIGH risk)
      - Multiple agents modifying schema
      - Suggestion: Assign to single agent
   
   2. Shared configuration files (MEDIUM risk)
      - 3 agents updating config/app.js
      - Suggestion: Use staged updates
   
   3. API contract changes (MEDIUM risk)
      - Frontend depends on backend API
      - Suggestion: Lock interface early
   
   Review and adjust? [Y/n]:
   ```

## Phase 6: Generate Parallel Execution Plan

### Final Output

1. **Enhanced Plan Document**
   - Original plan with validation fixes
   - Parallelization metadata added
   - Coordination instructions included
   
2. **Execution Manifest**
   ```json
   {
     "plan": "project-plan.md",
     "stages": 4,
     "agents": 3,
     "total_tasks": 25,
     "critical_path": ["task-1", "task-5", "task-12"],
     "estimated_time": {
       "sequential": "14h",
       "parallel": "6h"
     },
     "checkpoints": [
       {
         "after_stage": 1,
         "type": "hard_sync",
         "verify": ["no_conflicts", "all_tests_pass"]
       }
     ]
   }
   ```

3. **Agent Launch Commands**
   ```bash
   # Generated launch script
   claude-code --agent-id backend \
     --plan project-plan.md \
     --stage 1 \
     --command /user:implement-plan-parallel
   
   claude-code --agent-id frontend \
     --plan project-plan.md \
     --stage 1 \
     --command /user:implement-plan-parallel
   ```

## Summary Output

```
✅ Plan Validation Complete
✅ Parallelization Analysis Complete

Plan: Authentication System Implementation
Tasks: 25 total
Parallelizable: 18 tasks (72%)
Sequential Required: 7 tasks (28%)

Execution Strategy:
- Agents: 3 specialized
- Stages: 4 with checkpoints
- Speedup: 2.3x (14h → 6h)
- Risk Level: Medium (3 coordination points)

Generated Files:
- project-plan.md (enhanced)
- .claude/parallel-execution.json
- .claude/agent-launch.sh

Ready for parallel execution!
Run: /user:implement-plan-parallel project-plan.md
```

<rules>

- MUST complete standard validation before parallelization
- MUST identify all task dependencies (explicit and implicit)
- MUST detect resource conflicts and file collisions
- MUST create stages that respect dependencies
- MUST add coordination metadata to plan
- MUST generate execution manifest
- SHOULD optimize for maximum parallelization
- SHOULD assign tasks based on agent specialization
- SHOULD identify and mitigate parallel execution risks
- SHOULD provide time estimates for parallel vs sequential
- SHOULD create synchronization checkpoints
- SHOULD generate agent launch commands
- MAY suggest alternative parallelization strategies
- MAY recommend sequential execution for high-risk tasks
- MAY create visualizations of task dependencies

</rules>