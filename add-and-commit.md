Intelligently group and commit changes from the current chat session.

1. Analyze all modified files from the current session:
   - Run `git status` to see all changes
   - Run `git diff --name-only` to list modified files
   - Run `git diff --cached --name-only` to see staged files

2. Group related files into logical commits:
   - Files in the same directory/module
   - Files with similar functionality (e.g., component + its tests)
   - Config files with their related code changes
   - Keep groups reasonably sized (3-8 files per commit typically)
   - Avoid mixing unrelated changes (e.g., feature code with unrelated refactoring)

3. For each group:
   - Stage the files: `git add <files>`
   - Generate a descriptive commit message based on:
     * The type of change (feat/fix/refactor/test/docs/chore)
     * The scope/area affected
     * A brief description of what changed
   - Create the commit

4. Show me the commit plan before executing:
   - List each proposed commit with its files
   - Show the proposed commit message
   - Ask for confirmation or adjustments

5. Execute the commits in order

Example grouping logic:
- Group 1: Component files + tests + styles
- Group 2: API endpoints + related models
- Group 3: Configuration changes
- Group 4: Documentation updates