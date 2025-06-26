Intelligently group and commit changes from the current chat session.

<rules>

- MUST NOT use `git add .` or `git add -A`
- MUST add specific files for each commit group
- MUST keep each commit atomic and focused on a single logical change
- MUST review all changes before staging to ensure no unintended files are included
- MUST NOT commit files with merge conflict markers
- MUST ensure no sensitive data (API keys, passwords) in commits
- SHOULD group database migrations in separate commits
- SHOULD commit lock files with their package changes

</rules>

## Pre-flight Checks:
- Check for uncommitted work in progress or unstaged changes
- Validate current branch (warn if on main/master)
- Check for merge conflicts
- Scan for sensitive data patterns
- Verify file sizes are within limits

## Analysis Phase:

1. Analyze all modified files from the current session:
   - Run `git status` to see all changes
   - Run `git diff --name-only` to list modified files
   - Run `git diff --cached --name-only` to see staged files
   - Analyze actual diff content for better commit messages
   - Extract branch name for potential issue numbers

2. Intelligent grouping of related files:
   - Files in the same directory/module
   - Files with similar functionality (e.g., component + its tests)
   - Source files with their lock/build files
   - Database migrations (separate commits)
   - Config files with their related code changes
   - Keep groups reasonably sized (3-8 files per commit typically)
   - Consider dependency order (commit dependencies first)

3. For each group:
   - Auto-detect scope from file paths
   - Determine commit type from changes (feat/fix/refactor/test/docs/chore)
   - Stage files explicitly: `git add <specific-files>`
   - Generate detailed commit message analyzing the actual changes
   - Include issue numbers if found in branch name
   - Flag any breaking changes

4. Show me the commit plan before executing:

<output-format>

Pre-flight Status:
- Branch: <current-branch>
- Warnings: <any-warnings>

---

Commit 1: <type>(<scope>): <brief-description>

Files: (<total-insertions>+/<total-deletions>-)
- path/to/file1.js (+45/-12)
- path/to/file2.test.js (+120/-0)

Commit Description: <detailed-description-of-changes>
Related Issues: #<issue-numbers>
Breaking Changes: <yes/no>

---

Commit 2: <type>(<scope>): <brief-description>

Files: (<total-insertions>+/<total-deletions>-)
- path/to/file3.js (+23/-5)
- path/to/file4.css (+50/-10)

Commit Description: <detailed-description-of-changes>
Related Issues: #<issue-numbers>
Breaking Changes: <yes/no>

</output-format>

5. Interactive review:
   - Confirm the commit plan
   - Options to reorder, merge, or split commits
   - Exclude specific files if needed
   - Modify commit messages if desired

6. Execute the commits in order with progress indication