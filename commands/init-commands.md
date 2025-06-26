---
allowed-tools: DesktopCommander(*), Bash(mkdir)
description: Initialize project for Claude Code commands
---

Initialize your project with Claude Code command structure and starter commands.

## Pre-flight Check

1. Check if already initialized:
   - Look for existing `.claude/commands/` directory
   - If exists, ask if user wants to reinitialize

## Initialization Process

1. **Create directory structure**
   ```bash
   mkdir -p .claude/commands/{git-workflow,code-analysis,development,documentation,utility}
   ```

2. **Create README**
   ```markdown
   # Project Claude Commands
   
   This directory contains project-specific Claude Code commands.
   
   ## Usage
   Commands are invoked with: `/project:<category>:<command-name>`
   
   Example: `/project:git-workflow:prepare-release`
   
   ## Categories
   - **git-workflow**: Version control and collaboration
   - **code-analysis**: Code quality and analysis  
   - **development**: Build, test, and development workflows
   - **documentation**: Documentation generation and updates
   - **utility**: Helper commands and tools
   
   ## Creating New Commands
   Use `/user:create-command` to interactively create new commands.
   ```

3. **Create starter command**
   ```markdown
   # .claude/commands/utility/list-commands.md
   ---
   allowed-tools: Bash(find), Bash(head)
   description: List all project commands
   ---
   
   List all available project-specific commands.
   
   !`find .claude/commands -name "*.md" -type f | while read f; do
     echo "- /project:$(basename $(dirname $f)):$(basename $f .md)"
     head -n 3 $f | grep "description:" | sed 's/description: /  /'
   done`
   ```

4. **Add to .gitignore** (if needed)
   ```
   # Claude Code state files
   .claude/state/
   .claude/locks/
   .claude/cache/
   .claude/*.log
   ```

5. **Success message**
   ```
   ✅ Claude Code commands initialized!
   
   Created structure:
   .claude/
   └── commands/
       ├── README.md
       ├── git-workflow/
       ├── code-analysis/
       ├── development/
       ├── documentation/
       └── utility/
           └── list-commands.md
   
   Next steps:
   1. Create your first command: /user:create-command
   2. List project commands: /project:utility:list-commands
   3. Commit the .claude directory to version control
   ```

<rules>

- MUST create standard category directories
- MUST include helpful README
- MUST check for existing setup
- SHOULD create a starter command
- SHOULD update .gitignore appropriately
- MAY offer to create example commands

</rules>