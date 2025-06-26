---
allowed-tools: Bash(*), DesktopCommander(*), SubAgent(*)
description: Execute tasks from a parallelized plan using multiple coordinated sub-agents
---

Execute tasks from a parallelized markdown plan file using multiple sub-agents working in parallel, with automatic coordination, progress tracking, and merge management.

## Phase 1: Initialize Parallel Execution

### Pre-flight Checks

1. **Verify Parallelized Plan**
   ```
   Checking plan: project-plan.md
   
   ✓ Standard validation passed
   ✓ Parallelization metadata present  
   ✓ Execution manifest found
   ✓ Agent assignments defined
   ✓ Stage definitions complete
   
   Parallel execution ready!
   ```

2. **Load Execution Context**
   ```json
   {
     "agents": 3,
     "stages": 4,
     "total_tasks": 25,
     "coordination_dir": ".claude/",
     "branch_strategy": "feature-branches",
     "merge_points": [1, 2, 4]
   }
   ```

3. **Initialize Coordination Infrastructure**
   ```bash
   # Create coordination directories
   mkdir -p .claude/{status,locks,interfaces,logs}
   
   # Initialize status board
   echo '{"agents":{},"stages":{},"tasks":{}}' > .claude/status/board.json
   
   # Create agent branches
   git checkout -b feature/auth-agent-backend
   git checkout -b feature/auth-agent-frontend
   git checkout -b feature/auth-agent-infra
   ```

## Phase 2: Agent Orchestration

### Launch Sub-Agents

1. **Agent Configuration**
   ```yaml
   backend-agent:
     id: backend
     branch: feature/auth-agent-backend
     specialization: ["models", "api", "database"]
     tasks: [1, 4, 5, 8, 12]
     stage: 1
   
   frontend-agent:
     id: frontend  
     branch: feature/auth-agent-frontend
     specialization: ["ui", "components", "styles"]
     tasks: [2, 6, 9, 13, 14]
     stage: 1
   ```

2. **Sub-Agent Invocation**
   ```
   Launching parallel agents...
   
   [Agent:Backend] Starting on branch feature/auth-agent-backend
   [Agent:Frontend] Starting on branch feature/auth-agent-frontend
   [Agent:Infra] Starting on branch feature/auth-agent-infra
   
   Monitoring dashboard: .claude/status/dashboard.html
   ```

3. **Agent Instructions Template**
   ```markdown
   ## Sub-Agent Brief: ${AGENT_ID}
   
   You are Agent ${AGENT_ID} working on Stage ${STAGE}.
   
   Your tasks:
   ${TASK_LIST}
   
   Coordination protocol:
   - Update status: .claude/status/${AGENT_ID}.json
   - Check locks before file access: .claude/locks/
   - Post interfaces: .claude/interfaces/
   - Log progress: .claude/logs/${AGENT_ID}.log
   
   Work on branch: ${AGENT_BRANCH}
   Commit prefix: [${AGENT_ID}]
   ```

## Phase 3: Coordination Protocol

### Real-time Monitoring

1. **Status Tracking**
   ```json
   // .claude/status/backend.json
   {
     "agent": "backend",
     "status": "active",
     "current_task": "Create user model",
     "completed_tasks": [1, 4],
     "stage": 1,
     "last_update": "2024-01-15T10:30:00Z",
     "blockers": []
   }
   ```

2. **Lock Management**
   ```bash
   # Agent acquires lock
   echo "backend:2024-01-15T10:30:00Z" > .claude/locks/src-models-user.js.lock
   
   # Check lock before access
   if [ -f .claude/locks/src-models-user.js.lock ]; then
     OWNER=$(cat .claude/locks/src-models-user.js.lock)
     echo "File locked by $OWNER, waiting..."
   fi
   
   # Release lock after task
   rm .claude/locks/src-models-user.js.lock
   ```

3. **Interface Sharing**
   ```typescript
   // .claude/interfaces/user-model.ts
   export interface User {
     id: string;
     email: string;
     name: string;
     createdAt: Date;
   }
   
   // Posted by: backend-agent
   // Timestamp: 2024-01-15T10:45:00Z
   // Consumers: frontend-agent, test-agent
   ```

## Phase 4: Progress Aggregation

### Central Progress Monitor

1. **Task Completion Tracking**
   ```
   Stage 1 Progress:
   ├─ Backend:  ████████░░ 80% (4/5 tasks)
   ├─ Frontend: ██████░░░░ 60% (3/5 tasks)  
   └─ Infra:    ██████████ 100% (3/3 tasks)
   
   Overall: 10/13 tasks (77%)
   Estimated completion: 45 minutes
   ```

2. **Update Plan Progress**
   ```javascript
   // Atomic progress update
   async function updateProgress(agentId, taskId, status) {
     const lockFile = '.claude/locks/plan-update.lock';
     await acquireLock(lockFile);
     
     try {
       // Read current plan
       const plan = await readFile('project-plan.md');
       
       // Update task status
       const updated = updateTaskInPlan(plan, taskId, status);
       
       // Recalculate progress
       const progress = calculateProgress(updated);
       
       // Write atomically
       await writeFile('project-plan.md', updated);
       await updateStatusBoard(agentId, taskId, progress);
       
     } finally {
       await releaseLock(lockFile);
     }
   }
   ```

## Phase 5: Stage Synchronization

### Checkpoint Management

1. **Stage Completion Check**
   ```
   Checking Stage 1 completion...
   
   ✓ Backend: All tasks complete
   ✓ Frontend: All tasks complete
   ⏳ Infra: 1 task remaining
   
   Waiting for all agents to complete Stage 1...
   ```

2. **Merge Coordination**
   ```bash
   Stage 1 Complete! Starting merge process...
   
   1. Testing agent branches:
      - feature/auth-agent-backend: 8 commits, tests ✓
      - feature/auth-agent-frontend: 6 commits, tests ✓
      - feature/auth-agent-infra: 4 commits, tests ✓
   
   2. Merging to integration branch:
      git checkout -b feature/auth-integration-stage1
      git merge feature/auth-agent-backend
      git merge feature/auth-agent-frontend  
      git merge feature/auth-agent-infra
   
   3. Resolving conflicts:
      - package.json: Merged dependencies
      - config/app.js: Combined settings
   
   4. Integration tests: PASSED
   
   5. Updating main feature branch:
      git checkout feature/implement-auth-system
      git merge feature/auth-integration-stage1
   ```

3. **Next Stage Launch**
   ```
   Stage 2 Ready!
   
   Reassigning tasks to agents:
   - Backend: Tasks [15, 16, 19, 20]
   - Frontend: Tasks [17, 18, 21]
   - Infra: Tasks [22, 23]
   
   Launching Stage 2 execution...
   ```

## Phase 6: Error Recovery

### Handling Agent Failures

1. **Failure Detection**
   ```
   WARNING: Agent 'frontend' unresponsive
   Last update: 15 minutes ago
   Current task: "Build user dashboard"
   
   Recovery options:
   1. Wait longer (agent may be working)
   2. Restart agent from last checkpoint
   3. Reassign tasks to other agents
   4. Investigate agent logs
   ```

2. **Task Redistribution**
   ```
   Redistributing frontend tasks...
   
   Unfinished tasks: [18, 21]
   
   Available agents:
   - Backend: 75% capacity
   - Infra: 50% capacity
   
   Reassignment:
   - Task 18 → Backend agent
   - Task 21 → New frontend-recovery agent
   ```

## Phase 7: Completion and Cleanup

### Final Convergence

1. **All Tasks Complete**
   ```
   🎉 Parallel Execution Complete!
   
   Summary:
   - Total time: 5.5 hours (vs 14h sequential)
   - Speedup achieved: 2.5x
   - Agents used: 3
   - Merge conflicts resolved: 4
   - Tests passed: 142/142
   
   Task distribution:
   - Backend: 10 tasks (6 hours work)
   - Frontend: 8 tasks (4.5 hours work)
   - Infra: 7 tasks (3 hours work)
   ```

2. **Final Merge**
   ```bash
   Final merge to feature branch...
   
   git checkout feature/implement-auth-system
   git merge --squash feature/auth-integration-final
   git commit -m "feat: Complete authentication system
   
   Implemented via parallel execution:
   - 3 agents working simultaneously  
   - 25 tasks completed
   - All tests passing
   
   Co-authored-by: backend-agent
   Co-authored-by: frontend-agent
   Co-authored-by: infra-agent"
   ```

3. **Cleanup**
   ```bash
   Cleaning up parallel execution artifacts...
   
   1. Archive execution logs → .claude/archives/
   2. Remove lock files
   3. Delete agent branches
   4. Generate execution report
   
   Report saved: .claude/reports/parallel-execution-2024-01-15.md
   ```

## Coordination Features

### Live Dashboard

```html
<!-- .claude/status/dashboard.html -->
<h1>Parallel Execution Monitor</h1>

<div id="agents">
  <div class="agent" id="backend">
    <h3>Backend Agent</h3>
    <div class="progress">████████░░ 80%</div>
    <div class="current">Working on: Create API endpoints</div>
    <div class="eta">ETA: 15 minutes</div>
  </div>
</div>

<div id="timeline">
  <!-- Live timeline of task completions -->
</div>

<div id="conflicts">
  <!-- Real-time conflict alerts -->
</div>
```

### Communication Protocols

1. **Inter-agent Messaging**
   ```json
   // .claude/messages/frontend-to-backend.json
   {
     "from": "frontend",
     "to": "backend",
     "type": "interface_request",
     "content": "Need User interface definition",
     "priority": "blocking",
     "timestamp": "2024-01-15T11:00:00Z"
   }
   ```

2. **Broadcast Updates**
   ```bash
   # Agent broadcasts completion
   echo '{"event":"task_complete","task":15,"agent":"backend"}' \
     >> .claude/events/stream.jsonl
   ```

<rules>

- MUST verify plan has parallelization metadata
- MUST initialize coordination infrastructure before starting
- MUST create separate branches for each agent
- MUST implement atomic progress updates
- MUST enforce file locking for shared resources  
- MUST synchronize at stage checkpoints
- MUST merge agent work systematically
- MUST handle agent failures gracefully
- MUST track progress across all agents
- MUST maintain audit trail of all operations
- SHOULD optimize agent task distribution
- SHOULD detect and resolve conflicts automatically
- SHOULD provide real-time monitoring dashboard
- SHOULD implement inter-agent communication
- SHOULD generate comprehensive execution reports
- MAY redistribute tasks on agent failure
- MAY spawn additional agents for load balancing
- MAY use AI to resolve merge conflicts

</rules>