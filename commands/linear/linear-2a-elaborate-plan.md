Progressively elaborate on any Linear plan (initiative, project, or issue).

## Process:
1. Identify current work item and plan level
2. Load existing plan (may be just a stub)
3. Based on level, gather context:
   - Initiative: High-level goals, constraints, success metrics
   - Project: Architecture, phases, technical decisions
   - Issue: Implementation details, test strategy, edge cases
4. Interactive elaboration:
   - Ask clarifying questions
   - Suggest additions based on context
   - Identify missing information
   - Consider dependencies from graph
5. Update the plan while preserving structure
6. Propagate relevant decisions:
   - Downward: Update child stubs with new constraints
   - Upward: Flag if changes affect parent assumptions
   - Sideways: Update dependent items if needed

## Key Features:
- Plans evolve from rough to detailed
- Maintains consistency across levels
- Learns from similar completed work
- Suggests what to elaborate based on gaps

## Output:
- Enhanced plan with new details
- List of stubs that need updates
- Dependency impacts identified
- Next elaboration suggestions