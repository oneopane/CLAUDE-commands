# Claude Code Command Best Practices

This document defines best practices for Claude Code commands. Use `/user:update-command` to analyze existing commands against these practices.

## Command Design Principles

### 1. Clarity and Purpose
- Each command should solve one specific problem well
- Command names should be descriptive and action-oriented
- Avoid overloading commands with too many features

### 2. Predictability
- Commands should behave consistently
- Similar operations should follow similar patterns
- Outputs should be structured and parseable

### 3. Safety First
- Destructive operations require confirmation
- Always provide dry-run options
- Create backups before modifications
- Use atomic operations (all-or-nothing)

### 4. User Experience
- Provide clear progress indicators
- Give meaningful error messages
- Allow graceful interruption
- Show what will happen before doing it

## Structural Patterns

### Command Metadata
```markdown
---
allowed-tools: [ONLY_WHAT_YOU_NEED]
description: [CONCISE_ONE_LINE_DESCRIPTION]
---
```

### Standard Sections
1. **Overview** - Brief explanation of what the command does
2. **Rules** - MUST/MUST NOT/SHOULD/MAY requirements
3. **Pre-flight Checks** - Validation before main operation
4. **Main Process** - Core functionality in phases
5. **Output** - Clear description of results

### Parameter Handling
- Use `$ARGUMENTS` for simple single parameters
- For complex inputs, use interactive prompts
- Validate inputs early and fail fast
- Provide sensible defaults where appropriate

## Common Patterns

### 1. Progress Tracking
```bash
# Simple counter
echo "Processing file 1 of 10..."

# Percentage-based
echo "Progress: 45% (9/20 files)"

# Time estimates
echo "Analyzing... (estimated 2 minutes remaining)"
```

### 2. Error Handling
```bash
# Check prerequisites
if ! command -v npm &> /dev/null; then
    echo "ERROR: npm is required but not installed"
    exit 1
fi

# Validate inputs
if [ -z "$ARGUMENTS" ]; then
    echo "ERROR: No issue number provided"
    echo "Usage: /user:command <issue-number>"
    exit 1
fi
```

### 3. Interactive Workflows
```markdown
Confirm the following actions:
- Action 1: Description
- Action 2: Description

Proceed? [Y/n]: 

[If no, ask what to modify]
```

### 4. State Management
```bash
# For resumable operations
STATE_FILE=".claude/state/command-$TIMESTAMP.json"

# Save progress
save_state() {
    echo "{\"step\":\"$1\",\"data\":$2}" > "$STATE_FILE"
}

# Check for existing state
if [ -f "$STATE_FILE" ]; then
    echo "Found incomplete operation. Resume? [Y/n]"
fi
```

### 5. Parallel Execution
```markdown
## Agent Distribution Plan
- Agent 1: Tasks [1, 2, 3] - Focus area
- Agent 2: Tasks [4, 5, 6] - Focus area

Coordination:
- Shared state in .claude/coordination/
- Lock files for resource access
- Progress aggregation every 30 seconds
```

## Tool Usage Guidelines

### Bash Commands
- Prefer specific tools over generic ones (e.g., `rg` over `grep`)
- Always specify allowed commands in frontmatter
- Use command existence checks before execution
- Capture and handle command failures

### File Operations
- Use DesktopCommander for file operations when possible
- Always use absolute paths for reliability
- Check file existence before operations
- Create parent directories as needed

### External Integrations
- Handle API failures gracefully
- Implement retry logic with backoff
- Cache responses when appropriate
- Provide offline fallbacks

## Output Formats

### Structured Data
```json
{
  "status": "success|failure",
  "summary": "Brief description",
  "details": {},
  "next_steps": []
}
```

### Human-Readable Reports
```markdown
## Summary
- Total items: X
- Successful: Y
- Failed: Z

## Details
[Organized sections with findings]

## Recommendations
1. High priority action
2. Medium priority action
```

### Progress Updates
```
[Phase 1/3] Analyzing files...
├── Scanning: src/components/ [████████░░] 80%
├── Found: 42 components
└── Issues: 3 potential problems

[Phase 2/3] Generating report...
```

## Testing Your Commands

### Manual Testing
1. Test with missing arguments
2. Test with invalid inputs
3. Test interruption (Ctrl+C)
4. Test on empty/minimal projects
5. Test on large/complex projects

### Edge Cases to Consider
- Empty directories
- Files with special characters
- Very large files
- Concurrent execution
- Permission issues
- Missing dependencies

### Documentation
- Include usage examples
- Document all parameters
- Explain output format
- Note any prerequisites
- Add troubleshooting section

## Command Categories

### Git Workflow Commands
- Focus on atomic commits
- Preserve git history
- Validate branch state
- Handle merge conflicts

### Analysis Commands
- Provide actionable insights
- Support incremental analysis
- Cache expensive operations
- Generate visual reports

### Development Commands
- Follow project conventions
- Integrate with existing tools
- Generate working code
- Include appropriate tests

### Planning Commands
- Validate plan structure
- Track progress
- Support parallelization
- Enable resumability

### Integration Commands
- Handle authentication
- Respect rate limits
- Sync state properly
- Provide offline modes