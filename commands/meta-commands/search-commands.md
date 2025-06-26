---
allowed-tools: Bash(find), Bash(grep), Bash(head), Bash(sort), Bash(sed), DesktopCommander(read_file)
description: Search and discover available Claude Code commands
---

Search, list, and discover Claude Code commands with filtering and categorization.

## Usage Examples
- `/user:search-commands` - Interactive menu
- `/user:search-commands analyze` - Find commands with "analyze" in name
- `/user:search-commands --category linear` - List all Linear commands
- `/user:search-commands --description "test"` - Find commands that mention testing

## Search Process

### 1. Parse Arguments
```bash
# No arguments = interactive mode
# Single word = name search
# --category = filter by directory
# --description = search in descriptions
```

### 2. Build Command Index
```bash
# Find all command files
USER_COMMANDS_DIR="$HOME/.claude/commands"
PROJECT_COMMANDS_DIR=".claude/commands"

# Scan both user and project commands
find "$USER_COMMANDS_DIR" "$PROJECT_COMMANDS_DIR" -name "*.md" -type f 2>/dev/null | while read cmd; do
    # Extract command name from path
    NAME=$(basename "$cmd" .md)
    
    # Extract description from frontmatter
    DESC=$(grep "^description:" "$cmd" | sed 's/description: //')
    
    # Determine category from directory
    CATEGORY=$(dirname "$cmd" | xargs basename)
    
    # Determine prefix (user or project)
    if [[ "$cmd" == "$PROJECT_COMMANDS_DIR"* ]]; then
        PREFIX="project"
    else
        PREFIX="user"
    fi
    
    # Output formatted entry with prefix
done
```

### 3. Display Results

#### For Name Search:
```
Found 3 commands matching 'analyze':

📋 /user:analyze-code
   Location: User commands
   Category: CLAUDE-commands
   Description: Analyze codebase for complexity and improvements
   
📋 /user:analyze-issue  
   Location: User commands
   Category: CLAUDE-commands
   Description: Analyze GitHub issue and create implementation plan
   
📋 /project:code-analysis:analyze-dependencies
   Location: Project commands
   Category: code-analysis
   Description: Check for outdated and vulnerable dependencies
```

#### For Category List:
```
Linear Commands (13 total):
├── linear-1a-init-initiative     Initialize new Linear initiative
├── linear-1b-analyze-initiative  Analyze initiative structure
├── linear-1c-init-project       Initialize Linear project
└── [more...]

Use '/user:search-commands <name>' to see details
```

### 4. Show Command Details
When a single match is found or user selects a command:
```
Command: /project:code-analysis:analyze-dependencies
Location: Project commands (.claude/commands/)
Category: code-analysis
Description: Check for outdated and vulnerable dependencies

Allowed Tools:
- Bash: npm, pip, bundler
- DesktopCommander: read operations

Usage:
/project:code-analysis:analyze-dependencies [package-file]

Summary:
This command scans package files to identify outdated dependencies,
security vulnerabilities, and unused packages. Supports npm, pip,
and bundler ecosystems.

First 10 lines:
---
[Show frontmatter and beginning of command]
---
```

### 5. Interactive Menu
If no arguments provided:
```
🔍 Claude Code Command Explorer

What would you like to do?

1. Browse all commands by category
2. Search by command name  
3. Search by description/purpose
4. Show recently modified commands
5. Show commands by type (analysis/workflow/etc)
6. Show command statistics

Enter choice [1-6] or command name: 
```

## Output Formats

### Compact List
```
add-and-commit         - Intelligently group and commit changes
analyze-code          - Analyze codebase for improvements  
analyze-issue         - Analyze GitHub issue #$ARGUMENTS
```

### Detailed View
```
╭─ Command: analyze-code ─────────────────────────────╮
│ Category: CLAUDE-commands                           │
│ Type: Analysis Tool                                 │
│ Uses: Bash (12 tools), DesktopCommander            │
│ Features: ✓ Parallel execution ✓ Progress tracking │
│ Arguments: Optional directory path                   │
╰────────────────────────────────────────────────────╯
```

### Statistics View
```
📊 Command Statistics

User Commands: 27
Project Commands: 5
Total: 32

By Location:
  User (~/.claude/commands/):
    - CLAUDE-commands: 9
    - linear: 13  
    - planning: 5
  
  Project (.claude/commands/):
    - git-workflow: 2
    - code-analysis: 1
    - utility: 2

By Type:
  - Analysis: 8
  - Workflow: 10
  - Integration: 6
  - Utility: 3

Most Complex: implement-plan-parallel (397 lines)
Most Recent: analyze-dependencies (today)
```

<rules>

- MUST search both user (~/.claude/commands) and project (.claude/commands) directories
- MUST handle missing directories gracefully  
- MUST extract descriptions from frontmatter
- MUST show correct invocation prefix (user: or project:)
- SHOULD provide multiple search methods
- SHOULD categorize commands logically
- SHOULD show usage examples for commands
- MAY implement fuzzy matching for names
- MAY cache command index for performance

</rules>