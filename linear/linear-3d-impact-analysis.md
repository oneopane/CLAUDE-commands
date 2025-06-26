Analyze the impact of changes to current work item using the dependency graph.

## Analysis Types:
1. **Forward Impact** - What this change affects
   - Direct dependents
   - Indirect impacts (2+ hops)
   - Timeline implications
   - Risk propagation
2. **Backward Impact** - What affects this
   - Blocking dependencies
   - Required prerequisites
   - Assumption changes
   - Constraint violations
3. **Lateral Impact** - Peer relationships
   - Shared resources
   - Common components
   - Parallel work conflicts

## Process:
1. Identify the change:
   - Status change
   - Scope change
   - Timeline change
   - Technical approach change
2. Traverse the graph:
   - Find all connected nodes
   - Calculate impact distance
   - Identify critical paths
3. Analyze each impact:
   - Severity (high/medium/low)
   - Type (blocks/delays/invalidates)
   - Mitigation options
4. Generate recommendations:
   - Items to update
   - Teams to notify
   - Plans to revise
   - Risks to monitor

## Output:
- Impact visualization (Mermaid)
- Sorted impact list by severity
- Recommended actions
- Risk assessment
- Notification list