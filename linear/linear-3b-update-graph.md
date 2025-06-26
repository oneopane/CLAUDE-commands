Update the dependency graph for Linear items and regenerate visualizations.

## Operations:
1. Add/remove nodes (initiatives, projects, issues)
2. Add/remove edges (dependencies, blocks, enables)
3. Update node metadata (status, priority, phase)
4. Validate graph integrity

## Process:
1. Load current graph.json
2. Fetch latest state from Linear MCP
3. Interactive updates:
   - "What depends on this?"
   - "What does this block?"
   - "Add dependency between X and Y"
   - "Remove obsolete connection"
4. Validate changes:
   - No circular dependencies at same level
   - All nodes have Linear IDs
   - Edges make logical sense
5. Update graph.json with changes
6. Regenerate Mermaid visualization
7. Run impact analysis on changes

## Graph Edge Types:
- contains: Parent-child relationship
- blocks: Must complete before
- enables: Allows but doesn't block
- relates: Relevant connection
- shares: Shares code/resources

## Output:
- Updated graph.json
- New Mermaid diagram
- Impact analysis of changes
- Suggested graph optimizations