---
allowed-tools: DesktopCommander(*), Bash(find), Bash(grep), Bash(head)
description: Interactively create a new Claude Code command following best practices
---

Create a new Claude Code command through guided interactive process.

This command helps you create well-structured commands following the established best practices defined in:
@/Users/ojash/.claude/docs/COMMAND-BEST-PRACTICES.md

You'll be asked to choose whether to create the command in:
- Project directory (`.claude/commands/`) for project-specific commands
- User directory (`~/.claude/commands/`) for personal cross-project tools

## Phase 1: Command Planning

Let's design your new command together:

1. **Basic Information**
   - Command name (kebab-case, descriptive)
   - Brief description (one line)
   - Category: [git-workflow|code-analysis|development|documentation|linear|planning|utility|other]

2. **Command Location**
   ```
   Current project directory: !`pwd`
   User commands directory: !`echo $HOME/.claude/commands/`
   
   Where should this command be created?
   
   1. Project directory: .claude/commands/
      - Full path: !`pwd`/.claude/commands/[category]/[name].md
      - Usage: /project:[category]:[name]
      - Best for: project-specific workflows, team-shared commands
      - Version controlled with your project
   
   2. User directory: ~/.claude/commands/
      - Full path: !`echo $HOME/.claude/commands/`[category]/[name].md
      - Usage: /user:[category]:[name]
      - Best for: personal tools, cross-project utilities
      - Available in all your projects
   
   Choose location [1/2]:
   ```

3. **Command Type**
   ```
   What type of command are you creating?
   
   1. Simple Action - Single-purpose task (like add-and-commit)
   2. Analysis Tool - Examines code/data and reports (like analyze-code)
   3. Interactive Workflow - Multi-step with user input (like create-feature-issue)
   4. Automation Script - Executes planned tasks (like implement-plan)
   5. Integration Tool - Works with external services (like linear commands)
   6. Utility Function - Helper/support tool (like update-claude-md)
   ```

4. **Requirements Gathering**
   - What problem does this solve?
   - What inputs does it need?
   - What outputs should it produce?
   - What tools/permissions required?
   - Any dangerous operations?
   - Should it be idempotent?

## Phase 2: Best Practices Checklist

Based on your command type, I'll ensure it follows these patterns:

@/Users/ojash/.claude/docs/COMMAND-BEST-PRACTICES.md

### Universal Best Practices
- [ ] Clear frontmatter with allowed-tools and description
- [ ] Uses $ARGUMENTS for parameter passing
- [ ] Descriptive phase/section headers
- [ ] Handles missing arguments gracefully
- [ ] Provides clear user feedback
- [ ] Documents expected inputs/outputs

### For Action Commands
- [ ] Pre-flight validation checks
- [ ] Dry-run capability for destructive operations
- [ ] Atomic operations (all-or-nothing)
- [ ] Rollback plan for failures
- [ ] Success/failure reporting

### For Analysis Commands
- [ ] Progress indicators for long operations
- [ ] Structured output format (JSON/Markdown)
- [ ] Caching strategy for expensive operations
- [ ] Incremental analysis option
- [ ] Summary statistics

### For Interactive Commands
- [ ] Clear prompts with examples
- [ ] Input validation
- [ ] Confirmation before significant actions
- [ ] Option to abort at any step
- [ ] Review-before-execute pattern

### For Automation Commands
- [ ] State management/checkpointing
- [ ] Parallel execution consideration
- [ ] Lock files for shared resources
- [ ] Progress tracking
- [ ] Detailed logging

### For Integration Commands
- [ ] Authentication handling
- [ ] Rate limiting awareness
- [ ] Error handling for API failures
- [ ] Offline fallback options
- [ ] Data synchronization strategy

## Phase 3: Command Structure Template

Based on your inputs, I'll generate a command following this structure:

```markdown
---
allowed-tools: [TOOLS_BASED_ON_REQUIREMENTS]
description: [YOUR_DESCRIPTION]
---

[BRIEF_COMMAND_OVERVIEW]

<rules>
[GENERATED_BASED_ON_COMMAND_TYPE]
- MUST [critical requirements]
- MUST NOT [critical restrictions]
- SHOULD [best practices]
- MAY [optional enhancements]
</rules>

## Phase 1: Pre-flight Checks
[VALIDATION_BASED_ON_INPUTS]

## Phase 2: [MAIN_ACTION_NAME]
[CORE_FUNCTIONALITY]

## Phase 3: [COMPLETION_PHASE]
[CLEANUP_AND_REPORTING]

[ADDITIONAL_PHASES_AS_NEEDED]
```

## Phase 4: Implementation Patterns

### Pattern Library to Choose From:

1. **Progress Tracking**
   ```bash
   # For long operations
   TOTAL_STEPS=10
   CURRENT_STEP=0
   
   update_progress() {
     CURRENT_STEP=$((CURRENT_STEP + 1))
     echo "Progress: $CURRENT_STEP/$TOTAL_STEPS ($(($CURRENT_STEP * 100 / $TOTAL_STEPS))%)"
   }
   ```

2. **State Persistence**
   ```bash
   STATE_DIR=".claude/state/[command-name]"
   mkdir -p "$STATE_DIR"
   
   # Save checkpoint
   echo "$CURRENT_STATE" > "$STATE_DIR/checkpoint.json"
   ```

3. **Atomic Operations**
   ```bash
   # Create backup before modifications
   cp target.file target.file.backup
   
   # Apply changes with error handling
   if ! apply_changes; then
     mv target.file.backup target.file
     echo "ERROR: Rolled back changes"
   fi
   ```

4. **Interactive Confirmations**
   ```markdown
   Show planned changes:
   - Change 1: [description]
   - Change 2: [description]
   
   Proceed with these changes? [Y/n]:
   ```

5. **Structured Output**
   ```markdown
   <output-format>
   ## Summary
   - Total items processed: X
   - Issues found: Y
   - Time taken: Z seconds
   
   ## Details
   [SPECIFIC_FINDINGS]
   </output-format>
   ```

6. **File Locking**
   ```bash
   LOCK_FILE=".claude/locks/${OPERATION}.lock"
   if [ -f "$LOCK_FILE" ]; then
     echo "Operation in progress by another process"
     exit 1
   fi
   echo "$$" > "$LOCK_FILE"
   trap "rm -f $LOCK_FILE" EXIT
   ```

## Phase 5: Generate Command

After gathering all requirements, I'll:

1. **Create the command file**
   ```bash
   # Based on location choice
   if [ "$LOCATION" = "project" ]; then
       COMMAND_PATH=".claude/commands/[category]/[name].md"
       COMMAND_PREFIX="project"
   else
       COMMAND_PATH="$HOME/.claude/commands/[category]/[name].md"
       COMMAND_PREFIX="user"
   fi
   
   mkdir -p "$(dirname "$COMMAND_PATH")"
   ```

2. **Write the command content**
   - Include all relevant patterns
   - Add comprehensive documentation
   - Include example usage

3. **Validate the generated command**
   - Check syntax
   - Verify tool permissions
   - Test with sample inputs

4. **Create companion files** (if needed)
   - README.md for the category
   - Test data/fixtures
   - Helper scripts

5. **Show usage instructions**
   ```
   Command created successfully!
   
   Location: [CHOSEN_PATH]
   
   Usage: /[PREFIX]:[category]:[name] [arguments]
   
   Example: /[PREFIX]:[category]:[name] example-argument
   
   Next steps:
   - Test the command with sample data
   - Add to your workflow documentation
   - Consider creating related commands
   - Review docs/COMMAND-BEST-PRACTICES.md for additional patterns
   - [If project] Commit the new command to version control
   ```

## Interactive Example Flow

```
Let's create a new command!

1. Command name: analyze-dependencies
2. Description: Analyze project dependencies for updates and vulnerabilities

3. Category? 
   > code-analysis

4. Command location?
   
   Current project directory: /Users/ojash/myproject
   User commands directory: /Users/ojash/.claude/commands/
   
   Where should this command be created?
   
   1. Project directory: .claude/commands/
      - Full path: /Users/ojash/myproject/.claude/commands/code-analysis/analyze-dependencies.md
      - Usage: /project:code-analysis:analyze-dependencies
      - Best for: project-specific workflows, team-shared commands
      - Version controlled with your project
   
   2. User directory: ~/.claude/commands/
      - Full path: /Users/ojash/.claude/commands/code-analysis/analyze-dependencies.md
      - Usage: /user:code-analysis:analyze-dependencies
      - Best for: personal tools, cross-project utilities
      - Available in all your projects
   > 1

5. Command type?
   > 2 (Analysis Tool)

6. What should this command analyze?
   > npm/pip/gem dependencies for updates, security issues, and unused packages

7. Required tools?
   > npm, pip, bundler, git

8. Should it modify files?
   > No, analysis only with recommendations

Based on your inputs, I'll create a command that:
- Scans package files (package.json, requirements.txt, Gemfile)
- Checks for outdated dependencies
- Identifies security vulnerabilities
- Finds unused dependencies
- Generates upgrade recommendations

This will be created in: /Users/ojash/myproject/.claude/commands/code-analysis/analyze-dependencies.md
Usage will be: /project:code-analysis:analyze-dependencies

Proceed with creation? [Y/n]:
```

<rules>

- MUST follow naming convention (kebab-case)
- MUST include comprehensive error handling
- MUST document all parameters and outputs
- MUST validate inputs before processing
- MUST use appropriate tool permissions (least privilege)
- MUST include usage examples
- MUST ask user to choose between project and user directory
- MUST show full paths when asking for location choice
- SHOULD follow established patterns from existing commands
- SHOULD include progress tracking for long operations
- SHOULD provide dry-run mode for destructive operations
- SHOULD generate commands that are testable
- SHOULD consider command composability
- MAY include advanced features based on use case
- MAY suggest related commands to create

</rules>