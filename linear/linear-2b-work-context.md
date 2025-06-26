Load smart context for current Linear work item based on dependency graph.

## Context Loading Strategy:

### For Issues:
1. Load the issue plan and details from Linear
2. Load parent project (architecture decisions, constraints)
3. Load grandparent initiative (goals, success criteria)
4. Load sibling issues in same project
5. Load dependencies (1 hop in graph)
6. Load dependents (1 hop in graph)

### For Projects:
1. Load the project plan and details
2. Load parent initiative
3. Load all child issues (as summaries)
4. Load related projects (dependencies + dependents)
5. Load projects within 2 graph hops

### For Initiatives:
1. Load initiative plan
2. Load all projects (summary view)
3. Load related initiatives (if any)
4. Show progress metrics

## Process:
1. Detect current work item from context/current.json
2. Use Linear MCP to fetch latest state
3. Load graph.json to find relationships
4. Gather all relevant plans based on rules above
5. Present consolidated context
6. Update current.json with loaded context

## Output Format:
- Current focus and its status
- Key decisions from parent levels
- Dependencies that might block
- Related work to consider
- Suggested next actions based on graph