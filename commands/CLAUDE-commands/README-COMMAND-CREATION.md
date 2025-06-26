# Claude Code Command Creation System

## Overview

The `/user:create-command` command provides an interactive way to create new Claude Code commands following established best practices and patterns. It acts as a "command generator" that builds properly structured commands based on your requirements.

You can choose to create commands in either:
- **Project directory** (`.claude/commands/`) - Version controlled, project-specific
- **User directory** (`~/.claude/commands/`) - Personal tools, available across all projects

## Quick Reference

```bash
# Initialize project for commands (first time)
/user:init-commands

# Create a new command (interactive wizard)
/user:create-command

# Update existing command to follow best practices
/user:update-command

# Search existing commands
/user:search-commands
/user:search-commands analyze
/user:search-commands --category linear

# View best practices
cat ~/.claude/commands/CLAUDE-commands/COMMAND-BEST-PRACTICES.md
```

## Command Prefixes

- `/user:` - Commands in `~/.claude/commands/`
- `/project:` - Commands in `.claude/commands/`

The prefix is determined by where the command is located, not where it was created.

## Command Types

### 1. Simple Action
Single-purpose tasks that execute a specific operation
- Examples: `add-and-commit`, `update-claude-md`
- Best for: Quick operations with clear inputs/outputs

### 2. Analysis Tool  
Examines code or data and generates reports
- Examples: `analyze-code`, `analyze-issue`
- Best for: Code quality checks, dependency analysis, metrics

### 3. Interactive Workflow
Multi-step processes with user confirmation
- Examples: `create-feature-issue`, `create-command`
- Best for: Complex operations requiring user decisions

### 4. Automation Script
Executes planned tasks, possibly in parallel
- Examples: `implement-plan-parallel`, `cleanup-commits`
- Best for: Multi-step workflows, CI/CD operations

### 5. Integration Tool
Interfaces with external services
- Examples: Linear commands suite
- Best for: API interactions, service synchronization

### 6. Utility Function
Helper tools and support functions
- Examples: `validate-plan`, `search-commands`
- Best for: Tooling, maintenance, meta-operations

## File Structure

```
.claude/commands/              # Project-specific commands
├── code-analysis/            # Created by /user:create-command when
├── git-workflow/             # you choose "project directory"
├── development/              # Version controlled with your project
└── utility/

~/.claude/commands/            # Personal commands  
└── CLAUDE-commands/          # Command management toolkit
    ├── create-command.md     # Interactive command creator
    ├── update-command.md     # Update commands to best practices
    ├── search-commands.md    # Find and explore commands
    ├── init-commands.md      # Initialize project structure
    ├── COMMAND-BEST-PRACTICES.md
    ├── README-COMMAND-CREATION.md
    └── EXAMPLE-UPDATE-COMMAND.md  # Shows before/after example
```

## Best Practices Summary

### Universal Requirements
- ✅ Clear frontmatter with minimal tool permissions
- ✅ Descriptive naming (kebab-case)
- ✅ Comprehensive error handling
- ✅ Progress indicators for long operations
- ✅ Structured output formats

### Safety Features
- 🔒 Confirmation for destructive operations  
- 🔒 Dry-run mode where applicable
- 🔒 Atomic operations with rollback
- 🔒 File locking for concurrent access

### User Experience
- 💬 Interactive prompts with examples
- 💬 Clear error messages with solutions
- 💬 Progress tracking and time estimates
- 💬 Resumable operations for long tasks

## Creating Your First Command

1. **Run the creator**: `/user:create-command`

2. **Answer the prompts**:
   - Name: `check-pr-readiness`
   - Description: "Validate PR is ready for review"
   - Category: `git-workflow`
   - Location: Choose between:
     - Project: `/Users/you/current-project/.claude/commands/`
     - User: `/Users/you/.claude/commands/`
   - Type: `Analysis Tool`

3. **Define requirements**:
   - Checks: tests passing, no conflicts, PR template filled
   - Output: checklist with status indicators
   - Tools needed: git, gh CLI

4. **Review and confirm** the generated command

5. **Test your command**: 
   - If project: `/project:git-workflow:check-pr-readiness`
   - If user: `/user:git-workflow:check-pr-readiness`

## Updating Existing Commands

The `/user:update-command` helps modernize existing commands:

1. **Select a command** to update (search or browse)
2. **Get analysis report** showing what follows/needs best practices
3. **Choose improvements** to apply interactively
4. **Preview changes** before applying
5. **Test updated command** to ensure it still works

Example improvements:
- Add missing `<rules>` sections
- Improve error handling
- Add progress tracking
- Define structured output formats
- Add usage examples
- Implement state management

### When to Use Each Command

**Use `/user:create-command` when:**
- Starting fresh with a new command
- You want best practices built in from the start
- Creating standard command types (analysis, workflow, etc.)

**Use `/user:update-command` when:**
- You have existing commands that need improvement
- Commands were created before best practices were established  
- You want to modernize legacy commands
- Adding advanced features to simple commands

## How create-command Works

The `/user:create-command` command:

1. **Gathers requirements** through interactive prompts
2. **Asks for location** with full paths for both options
3. **Selects patterns** based on your command type (analysis, workflow, etc.)
4. **Generates structure** with appropriate sections:
   - Frontmatter with minimal tool permissions
   - Rules section with MUST/SHOULD/MAY requirements  
   - Pre-flight validation checks
   - Main operation phases
   - Output format specifications
5. **Applies best practices** automatically:
   - Error handling templates
   - Progress tracking for long operations
   - State management for resumability
   - Proper argument validation
6. **Creates the file** in your chosen location with correct prefix

## Advanced Features

### Command Composition
Chain commands together for complex workflows:
```bash
/user:analyze-code && /user:write-tests && /user:add-and-commit
```

### State Management
Commands can save and resume state:
```bash
# Long running command interrupted
/user:analyze-code src/
# Ctrl+C

# Resume where it left off
/user:analyze-code --resume
```

### Parallel Execution
Some commands support parallel sub-agents:
```bash
/user:implement-plan-parallel complex-plan.md
# Spawns multiple agents working simultaneously
```

## Contributing

When adding new patterns or improving the system:

1. Update `COMMAND-BEST-PRACTICES.md` with new patterns
2. Add examples to `command-template.md` if applicable
3. Test the pattern in a real command
4. Update `create-command.md` to include the pattern

## Troubleshooting

### Command not found
- Check the command exists: `ls ~/.claude/commands/`
- Verify correct syntax: `/user:command-name`

### Permission errors
- Ensure tools are listed in `allowed-tools`
- Check file permissions in project directory

### Execution failures
- Run with verbose output: Add debugging echo statements
- Check prerequisites are installed
- Verify argument format matches expectations

## Next Steps

- Create your first command with `/user:create-command`
- Review existing commands for inspiration
- Read `COMMAND-BEST-PRACTICES.md` for detailed patterns
- Share your commands with the team

## Summary

### Command System Overview

- **`/user:init-commands`** - Initialize project with command structure
- **`/user:create-command`** - Interactive wizard that generates new commands
- **`/user:update-command`** - Analyze and update existing commands to follow best practices
- **`/user:search-commands`** - Find and explore existing commands  
- **`COMMAND-BEST-PRACTICES.md`** - Reference guide for patterns and principles
- **This README** - Overview of the command creation system

### Key Points

1. **Choose location** when creating commands:
   - Project (`.claude/commands/`) - Version controlled, project-specific
   - User (`~/.claude/commands/`) - Personal tools, cross-project utilities
2. **Full paths shown** during creation to avoid confusion
3. **Correct prefix** automatically determined (`/project:` or `/user:`)
4. **Best practices** are referenced directly by create-command to stay in sync

The `create-command` has all template logic built in - no separate template file needed!

### Usage Examples

```bash
# Create a project-specific command
/user:create-command
> Name: check-tests
> Category: development
> Location: 1 (project: /Users/you/myproject/.claude/commands/)
# Creates: .claude/commands/development/check-tests.md
# Usage: /project:development:check-tests

# Create a personal utility
/user:create-command
> Name: format-json
> Category: utility
> Location: 2 (user: /Users/you/.claude/commands/)
# Creates: ~/.claude/commands/utility/format-json.md
# Usage: /user:utility:format-json

# Update an older command to follow best practices
/user:update-command
> Search: analyze-code
# Shows analysis report and guides through improvements

# Find all analysis commands
/user:search-commands analyze
```

### Command Lifecycle

1. **Initialize** - `/user:init-commands` sets up project structure
2. **Create** - `/user:create-command` generates new commands with best practices
3. **Discover** - `/user:search-commands` helps find existing commands
4. **Update** - `/user:update-command` modernizes older commands
5. **Iterate** - Commands evolve with your project needs