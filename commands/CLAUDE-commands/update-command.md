---
allowed-tools: DesktopCommander(*), Bash(find), Bash(grep), Bash(head), Bash(diff)
description: Analyze and update existing commands to follow best practices
---

Analyze an existing Claude Code command and interactively update it to follow best practices.

This command helps modernize older commands or improve commands that were created without following the patterns in:
@/Users/ojash/.claude/commands/CLAUDE-commands/COMMAND-BEST-PRACTICES.md

## How It Works

1. **Select** - Choose a command to update (search or browse)
2. **Analyze** - Get a detailed report on what follows/needs best practices
3. **Review** - See specific improvements with examples
4. **Apply** - Interactively choose which updates to make
5. **Verify** - Test the updated command works correctly

Common improvements include:
- Adding `<rules>` sections
- Improving error handling
- Adding structured output formats
- Implementing progress tracking
- Adding usage examples
- Creating troubleshooting guides

## Phase 1: Command Selection

1. **Find the command to update**
   ```
   How would you like to specify the command?
   
   1. Search by name
   2. Browse by category
   3. Enter full command name (e.g., analyze-code)
   4. Enter file path
   
   Choice [1-4]:
   ```

2. **Locate and verify**
   - Search both user and project directories
   - Show matches if multiple found
   - Confirm the correct command
   - Display current location and usage

## Phase 2: Command Analysis

Analyze the selected command against best practices:

### Structure Analysis
- [ ] Has proper frontmatter with `allowed-tools` and `description`
- [ ] Uses minimal tool permissions (least privilege)
- [ ] Has clear phase/section organization
- [ ] Includes `<rules>` section with MUST/SHOULD/MAY
- [ ] Documents expected inputs/outputs
- [ ] Has usage examples

### Pattern Analysis
- [ ] Error handling for missing arguments
- [ ] Progress indicators for long operations
- [ ] Interactive confirmations for destructive operations
- [ ] Structured output format
- [ ] State management for resumability
- [ ] Proper argument validation

### Quality Checks
- [ ] Clear, action-oriented command name
- [ ] Descriptive section headers
- [ ] Consistent formatting
- [ ] No hardcoded paths
- [ ] Handles edge cases
- [ ] Includes troubleshooting section

Note: If command name doesn't follow best practices (e.g., "pr" instead of "prepare-pr"), 
the update process will suggest renaming and handle the file move.

## Phase 3: Generate Update Report

```
Analysis Report for: /user:analyze-code

✅ Good Practices Found:
- Proper frontmatter structure
- Clear phase organization
- Parallel execution pattern
- Progress tracking

🔧 Improvements Needed:
1. Missing <rules> section
   - Should add MUST/SHOULD/MAY requirements
   
2. No structured output format defined
   - Should specify JSON or markdown output structure
   
3. Error handling could be improved
   - Add validation for missing arguments
   - Handle tool failures gracefully
   
4. No usage examples
   - Should add 2-3 common usage patterns

5. State management missing
   - Add checkpoint/resume capability for long operations

📊 Best Practices Score: 7/10
```

## Phase 4: Interactive Updates

For each improvement, offer options:

```
1. Missing <rules> section

Current: No rules section found

Suggested addition:
<rules>
- MUST validate input directory exists
- MUST use structured output format
- MUST handle analysis failures gracefully
- SHOULD provide progress updates
- SHOULD support incremental analysis
- MAY cache results for performance
</rules>

Options:
a) Apply suggested rules
b) Modify suggested rules
c) Write custom rules
d) Skip this improvement

Choice [a/b/c/d]:
```

## Phase 5: Apply Updates

1. **Create backup**
   ```bash
   BACKUP_FILE="[original-file].backup-$(date +%Y%m%d-%H%M%S)"
   cp [original-file] "$BACKUP_FILE"
   echo "Backup saved: $BACKUP_FILE"
   ```

2. **Show diff preview**
   ```diff
   + <rules>
   + - MUST validate input directory exists
   + - MUST use structured output format
   + </rules>
   +
     ## Phase 1: Pre-flight Checks
   ```

3. **Apply changes**
   - Update file with improvements
   - Preserve command's core functionality
   - Maintain any custom patterns

4. **Verify updates**
   - Re-analyze to show improved score
   - Test command still works
   - Show before/after comparison

5. **Recovery option**
   ```
   If issues are found after update:
   - Restore from backup: cp [backup-file] [original-file]
   - Or use: /user:update-command --restore [command-name]
   ```

## Phase 6: Additional Enhancements

After basic updates, offer optional enhancements:

1. **Add advanced features**
   - Parallel execution with sub-agents
   - State persistence and checkpointing  
   - Caching for expensive operations
   - Integration with other commands

2. **Improve user experience**
   - Better progress indicators
   - More helpful error messages
   - Interactive mode improvements
   - Dry-run capability

3. **Add testing support**
   - Example test scenarios
   - Mock data for testing
   - Validation commands

## Update Patterns

### Adding Rules Section
```markdown
<rules>
- MUST [critical requirements based on command type]
- MUST NOT [critical restrictions]
- SHOULD [recommended practices]
- MAY [optional enhancements]
</rules>
```

### Improving Error Handling
```bash
# Before:
DIRECTORY=$ARGUMENTS

# After:
DIRECTORY=${ARGUMENTS:-}
if [ -z "$DIRECTORY" ]; then
    echo "ERROR: No directory specified"
    echo "Usage: /user:command-name <directory>"
    exit 1
fi

if [ ! -d "$DIRECTORY" ]; then
    echo "ERROR: Directory '$DIRECTORY' does not exist"
    exit 1
fi
```

### Adding Progress Tracking
```bash
# For countable operations
TOTAL_FILES=$(find "$DIR" -type f | wc -l)
PROCESSED=0

process_file() {
    PROCESSED=$((PROCESSED + 1))
    echo "Progress: $PROCESSED/$TOTAL_FILES files ($(($PROCESSED * 100 / $TOTAL_FILES))%)"
}

# For timed operations
START_TIME=$(date +%s)
echo "Analysis started at $(date)"
# ... operation ...
END_TIME=$(date +%s)
echo "Completed in $((END_TIME - START_TIME)) seconds"
```

### Adding Output Structure
```markdown
## Output Format

<output-format>
{
  "summary": {
    "total_analyzed": 0,
    "issues_found": 0,
    "critical": 0,
    "warnings": 0
  },
  "issues": [
    {
      "file": "path/to/file",
      "line": 0,
      "type": "error|warning|info",
      "message": "description"
    }
  ],
  "recommendations": []
}
</output-format>
```

## Example Update Session

```
Updating: /user:cleanup-commits

Analysis complete! Found 5 improvements needed.

1. Add <rules> section? [Y/n]: Y
   ✓ Added standard rules for git workflow commands

2. Improve error handling? [Y/n]: Y
   ✓ Added validation for missing arguments
   ✓ Added check for valid branch

3. Add structured output? [Y/n]: Y
   ✓ Added JSON output format specification

4. Add progress tracking? [Y/n]: n
   ⤳ Skipped (not needed for this command)

5. Add usage examples? [Y/n]: Y
   ✓ Added 3 usage examples

Update Summary:
- Original score: 5/10
- New score: 9/10
- Backup saved: cleanup-commits.md.backup-20240115-143022

Test the updated command? [Y/n]:
```

## Summary

The `/user:update-command` helps maintain command quality over time by:

1. **Analyzing** existing commands against current best practices
2. **Suggesting** specific, actionable improvements
3. **Applying** updates interactively with user control
4. **Preserving** the command's core functionality
5. **Testing** to ensure updates don't break anything

Works together with:
- `/user:create-command` - Creates new commands with best practices built in
- `/user:search-commands` - Finds commands that might need updating
- `COMMAND-BEST-PRACTICES.md` - Defines the standards to follow

Perfect for:
- Modernizing older commands
- Adding missing error handling
- Improving command structure
- Standardizing output formats
- Adding progress tracking
- Implementing state management

<rules>

- MUST create backup before any modifications
- MUST preserve core functionality of the command
- MUST show diff preview before applying changes
- MUST validate updated command still works
- MUST reference COMMAND-BEST-PRACTICES.md for patterns
- SHOULD analyze all aspects of best practices
- SHOULD provide specific, actionable improvements
- SHOULD allow skipping any suggested change
- SHOULD maintain command's unique patterns if valid
- SHOULD offer both automatic and manual update options
- MAY suggest advanced enhancements
- MAY offer to test the updated command

</rules>