# Claude Code Global Configuration

This repository contains the global Claude Code configuration, commands, and utilities.

## Overview

This is the global `.claude` directory that stores:
- Personal Claude Code commands available across all projects
- Global configuration and settings
- Command best practices and documentation
- Session data and task tracking

## Command Creation System

### Overview

The `/user:create-command` command provides an interactive way to create new Claude Code commands following established best practices and patterns. It acts as a "command generator" that builds properly structured commands based on your requirements.

You can choose to create commands in either:
- **Project directory** (`.claude/commands/`) - Version controlled, project-specific
- **User directory** (`~/.claude/commands/`) - Personal tools, available across all projects

### Quick Reference

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
```

### Command Prefixes

- `/user:` - Commands in `~/.claude/commands/`
- `/project:` - Commands in `.claude/commands/`

The prefix is determined by where the command is located, not where it was created.

### Command Types

#### 1. Simple Action
Single-purpose tasks that execute a specific operation
- Examples: `add-and-commit`, `update-claude-md`
- Best for: Quick operations with clear inputs/outputs

#### 2. Analysis Tool  
Examines code or data and generates reports
- Examples: `analyze-code`, `analyze-issue`
- Best for: Code quality checks, dependency analysis, metrics

#### 3. Interactive Workflow
Multi-step processes with user confirmation
- Examples: `create-feature-issue`, `create-command`
- Best for: Complex operations requiring user decisions

#### 4. Automation Script
Executes planned tasks, possibly in parallel
- Examples: `implement-plan-parallel`, `cleanup-commits`
- Best for: Multi-step workflows, CI/CD operations

#### 5. Integration Tool
Interfaces with external services
- Examples: Linear commands suite
- Best for: API interactions, service synchronization

#### 6. Utility Function
Helper tools and support functions
- Examples: `validate-plan`, `search-commands`
- Best for: Tooling, maintenance, meta-operations

### Creating Your First Command

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

### Updating Existing Commands

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

### Command System Overview

- **`/user:init-commands`** - Initialize project with command structure
- **`/user:create-command`** - Interactive wizard that generates new commands
- **`/user:update-command`** - Analyze and update existing commands to follow best practices
- **`/user:search-commands`** - Find and explore existing commands  
- **`docs/COMMAND-BEST-PRACTICES.md`** - Reference guide for patterns and principles

### Key Points

1. **Choose location** when creating commands:
   - Project (`.claude/commands/`) - Version controlled, project-specific
   - User (`~/.claude/commands/`) - Personal tools, cross-project utilities
2. **Full paths shown** during creation to avoid confusion
3. **Correct prefix** automatically determined (`/project:` or `/user:`)
4. **Best practices** are referenced directly by create-command to stay in sync

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

## Repository Structure

```
~/.claude/                       # Global Claude Code configuration
├── README.md                    # This file
├── CLAUDE.md                    # User's private global instructions
├── settings.json                # Claude Code settings
├── docs/                        # Documentation
│   ├── COMMAND-BEST-PRACTICES.md   # Best practices guide
│   └── PLANNING-REQUIREMENTS.md    # Plan validation spec
├── commands/                    # Global command collection
│   ├── linear/                  # Linear workflow commands
│   │   └── README.md           # Linear documentation
│   ├── planning/               # Planning commands
│   │   └── README.md          # Planning documentation
│   └── [various command files]
├── tools/                       # CLI tools and utilities
│   └── README.md               # Tools documentation
├── projects/                    # Project session data
├── statsig/                     # Analytics data
└── todos/                       # Task tracking data
```