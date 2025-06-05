Implement issue #$ARGUMENTS following .claude/plans/issue-$ARGUMENTS.md

1. Create feature branch: feature/issue-$ARGUMENTS
2. For each major section in the plan:
   a. Implement the component/feature
   b. Run existing tests to check for regressions
   c. Commit with descriptive message: "feat(#$ARGUMENTS): [component name] - [what it does]"
   d. Show me the implementation and wait for feedback
   e. Make any requested changes and amend commit if needed
3. Document any deviations from the original plan
4. Update plan file if approach changes significantly
5. Create a final commit summarizing all changes if multiple commits exist

Commit message format:
- feat(#$ARGUMENTS): Add new functionality
- fix(#$ARGUMENTS): Fix specific bug
- refactor(#$ARGUMENTS): Restructure code
- test(#$ARGUMENTS): Add tests
- docs(#$ARGUMENTS): Update documentation
