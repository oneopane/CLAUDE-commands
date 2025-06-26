Analyze GitHub issue #$ARGUMENTS and create a detailed implementation plan through discussion.

1. Fetch the issue details
2. Identify affected components and files
3. List potential edge cases and risks
4. Estimate complexity (simple/medium/complex)

Before creating the plan, engage in discussion:
- Ask clarifying questions about ambiguous requirements
- Confirm understanding of the feature's purpose
- Discuss architectural decisions and trade-offs
- Verify assumptions about existing code patterns
- Clarify any performance or security constraints

After discussion is complete and we agree on the approach:
5. Create a step-by-step implementation plan
6. Define test strategy:
   - Unit tests needed (with specific scenarios)
   - Integration tests required
   - Edge cases to cover
   - Performance tests if applicable
7. Save plan to .claude/plans/issue-$ARGUMENTS.md

If the issue is too vague or complex, explain why and request clarification.
