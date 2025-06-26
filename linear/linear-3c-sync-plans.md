Synchronize plans across the hierarchy based on updates and learnings.

## Sync Operations:
1. **Downward Propagation** - Parent changes affect children
   - New constraints from initiative
   - Architecture decisions from project
   - API changes affecting issues
2. **Upward Propagation** - Child learnings update parents
   - Actual time vs estimates
   - Discovered dependencies
   - Technical decisions made
3. **Lateral Propagation** - Peer items share knowledge
   - Shared component changes
   - Common patterns discovered
   - Dependency updates

## Process:
1. Identify what has changed:
   - Compare with last sync timestamp
   - Check Linear MCP for updates
   - Scan for plan modifications
2. Determine propagation needs:
   - What stubs need updates?
   - What estimates need revision?
   - What dependencies changed?
3. Update affected plans:
   - Preserve local details
   - Add new constraints/decisions
   - Update estimates based on actuals
   - Flag conflicts for review
4. Update graph if needed:
   - New dependencies discovered
   - Relationships changed
   - Status updates

## Output:
- List of updated plans
- Conflicts requiring attention
- Graph changes made
- Sync timestamp updated