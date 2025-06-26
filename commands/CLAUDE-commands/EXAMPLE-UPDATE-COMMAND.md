# Example: Updating an Older Command

This example shows how `/user:update-command` improves an older command.

## Original Command

```markdown
---
allowed-tools: Bash(git), Bash(gh)
description: prepare pr for review
---

Prepare a pull request for issue #$ARGUMENTS

Run these commands:
- git status
- git diff
- gh pr create --title "Fix issue $ARGUMENTS"
```

## After Running `/user:update-command`

### Analysis Report
```
Analysis Report for: /user:prepare-pr

✅ Good Practices Found:
- Has frontmatter structure
- Uses minimal tool permissions

🔧 Improvements Needed:
1. Missing <rules> section
2. No error handling for missing arguments  
3. No validation checks
4. Command name not descriptive enough
5. No structured phases
6. Missing usage examples

📊 Best Practices Score: 3/10
```

### Updated Command

```markdown
---
allowed-tools: Bash(git), Bash(gh), DesktopCommander(read_file)
description: Prepare pull request for issue with validation and checks
---

Prepare a comprehensive pull request for the specified issue.

<rules>
- MUST validate issue number provided
- MUST check for uncommitted changes
- MUST verify on feature branch
- MUST generate PR from template
- SHOULD include test summary
- SHOULD check CI status
- MAY auto-assign reviewers
</rules>

## Phase 1: Pre-flight Checks

1. **Validate arguments**
   ```bash
   ISSUE_NUMBER=${ARGUMENTS:-}
   if [ -z "$ISSUE_NUMBER" ]; then
       echo "ERROR: No issue number provided"
       echo "Usage: /user:prepare-pr <issue-number>"
       exit 1
   fi
   ```

2. **Check git status**
   - Ensure no uncommitted changes
   - Verify on correct branch
   - Check for merge conflicts

## Phase 2: Generate PR Content

1. **Fetch issue details**
   ```bash
   ISSUE_TITLE=$(gh issue view $ISSUE_NUMBER --json title -q .title)
   ISSUE_BODY=$(gh issue view $ISSUE_NUMBER --json body -q .body)
   ```

2. **Generate PR description**
   - Link to issue
   - Summary of changes
   - Test results
   - Breaking changes

## Phase 3: Create Pull Request

1. **Create PR with template**
   ```bash
   gh pr create \
     --title "feat: $ISSUE_TITLE (#$ISSUE_NUMBER)" \
     --body "$PR_BODY" \
     --assignee @me
   ```

2. **Post-creation tasks**
   - Add labels
   - Request reviews
   - Update issue status

## Usage Examples

```bash
# Basic usage
/user:prepare-pr 123

# After implementing feature for issue 456
/user:prepare-pr 456
```

## Troubleshooting

- If "not on a feature branch" error: Create branch first
- If "uncommitted changes" error: Commit or stash changes
- If "issue not found" error: Verify issue number exists
```

## Key Improvements Made

1. **Added Structure**
   - Clear phases with descriptive headers
   - Logical flow from validation to execution

2. **Error Handling**
   - Validates arguments exist
   - Checks git state
   - Provides helpful error messages

3. **Best Practices**
   - `<rules>` section defines behavior
   - Usage examples show common scenarios
   - Troubleshooting helps users recover

4. **Enhanced Functionality**
   - Fetches issue details automatically
   - Generates better PR titles
   - Handles edge cases

5. **Better Documentation**
   - Clear description
   - Step-by-step process
   - Expected outcomes

The updated command is more robust, user-friendly, and maintainable!