# Claude Code Planning Commands

This directory contains custom Claude Code commands for managing and executing markdown-based project plans.

## ⚠️ Important: Path Configuration

These commands reference a shared requirements specification located at:
```
/Users/ojash/.claude/docs/PLANNING-REQUIREMENTS.md
```

**If you're using these commands on a different machine or have a different username**, you'll need to update this path in:
- `validate-plan.md`
- `validate-plan-and-parallelize.md`

Look for lines containing `@/Users/ojash/...` and update them to your local path.

## Commands Overview

### Planning Requirements
- **File**: `PLANNING-REQUIREMENTS.md`
- **Purpose**: Authoritative specification for what constitutes a valid planning document
- **Usage**: Referenced by validation commands to ensure consistency

### Validation Commands
- **`/user:validate-plan`**: Validates a plan document against requirements and interactively fixes issues
- **`/user:validate-plan-and-parallelize`**: Validates a plan and analyzes it for parallel execution opportunities

### Execution Commands
- **`/user:implement-plan`**: Executes tasks from a validated plan sequentially
- **`/user:implement-plan-parallel`**: Executes tasks using multiple coordinated sub-agents
## Quick Start

1. Create a markdown plan document with tasks
2. Run `/user:validate-plan myplan.md` to ensure it meets requirements
3. (Optional) Run `/user:validate-plan-and-parallelize myplan.md` for parallel execution
4. Execute with `/user:implement-plan myplan.md` or `/user:implement-plan-parallel myplan.md`

## Plan Document Structure

Plans must include:
- Branch specification
- Title and metadata (Created, Status, Type)
- At least one checkbox task
- (Recommended) Progress tracking section

See `PLANNING-REQUIREMENTS.md` for full specification.

## Contributing

When updating requirements:
1. Edit `PLANNING-REQUIREMENTS.md` 
2. Ensure both validation commands still reference it correctly
3. Test that validation behaves as expected

## Future Improvements

- [ ] Make path references relative or configurable
- [ ] Add environment variable support for base path
- [ ] Create installation script that updates paths automatically