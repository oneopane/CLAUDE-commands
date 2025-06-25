Update a CLAUDE.md file based on recent code changes.

1. Ask which CLAUDE.md file to update (or path to it)
2. Read the current content of that CLAUDE.md file
3. Check when it was last modified:
   git log -1 --format="%ci" -- [path/to/CLAUDE.md]

4. Find all code changes since that date:
   - List commits since the CLAUDE.md update
   - Identify modified files in the same directory/component
   - Look for new patterns, dependencies, or architectural changes
   - Check for new test files or testing patterns
   - Find any new configuration or environment variables

5. Analyze gaps between documentation and current code:
   - New functions/methods not documented
   - Changed interfaces or parameters
   - New dependencies or integrations
   - Updated conventions or patterns
   - Performance optimizations or gotchas

6. Discuss findings with me:
   - Show what's potentially outdated
   - Highlight significant changes
   - Ask which updates are important to document

7. Update the CLAUDE.md file:
   - Preserve existing valuable context
   - Add new sections for recent changes
   - Update outdated information
   - Add timestamp comment: <!-- Last updated: YYYY-MM-DD -->

8. Commit the updated documentation:
   git add [path/to/CLAUDE.md]
   git commit -m "docs: Update CLAUDE.md with recent changes. <PREVIOUS UPDATE DATE> -> <CURRENT UPDATE DATE>"
