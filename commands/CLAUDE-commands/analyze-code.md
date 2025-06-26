---
allowed-tools: Bash(git ls-files), Bash(git log), Bash(git diff), Bash(git blame), Bash(sg), Bash(rg), Bash(find), Bash(grep), Bash(wc), Bash(cloc), Bash(tokei), Bash(jq), Bash(sort), Bash(uniq), Bash(head), Bash(tail), Bash(tee), Bash(mkdir), Bash(echo)
description: Analyze codebase for complexity, duplication, and improvement opportunities
---

Perform comprehensive code analysis by intelligently distributing work across parallel sub-agents.

## Phase 1: Codebase Scan

1. **Gather File Inventory**
   - Run `git ls-files` to get all tracked files
   - Use `tokei` or `cloc` to get language statistics
   - Count files per directory to understand structure
   - Check for previous analysis cache in `.claude-analysis/`

2. **Identify Hotspots**
   - Use `git log --format=format: --name-only` to find frequently changed files
   - Find large files that may need special attention
   - Identify core directories vs peripheral code
   - For incremental analysis: `git diff --name-only HEAD~${COMMITS:-10}`

3. **Analyze Patterns**
   - Group files by purpose (controllers, models, views, utils, tests)
   - Identify language boundaries if multi-language project
   - Note framework-specific structures
   - Detect common dependency patterns

## Phase 2: Create Distribution Plan

Based on the scan, create a sub-agent distribution plan that:

1. **Groups Related Files**
   - Keep files that import each other together
   - Group by architectural layer or domain
   - Maintain language consistency per agent
   - Consider shared dependencies

2. **Balances Workload**
   - Aim for similar file counts per agent (±20%)
   - Consider file sizes and complexity, not just count
   - Factor in analysis complexity for different file types
   - Account for analysis depth level (quick/standard/deep)

3. **Assigns Clear Objectives**
   - Each agent should have 2-3 specific analysis goals
   - Provide specific `sg` patterns for the language/framework
   - Include known false positive patterns to skip
   - Define severity thresholds

4. **Presents the Plan**
   - Show number of sub-agents proposed
   - List files/directories each will analyze
   - State primary objectives for each
   - Estimate runtime for each
   - Show analysis depth level
   - Ask for user confirmation with options to adjust

## Phase 3: Define Sub-Agent Tasks

For each sub-agent, create detailed instructions including:

1. **Input Specification**
   - Exact list of files to analyze
   - Language-specific AST patterns for `sg`
   - Security vulnerability patterns for the context
   - Performance anti-patterns to detect

2. **Analysis Patterns**
   ```bash
   # Example patterns each agent should use:
   # Dead code: sg -p 'function $FUNC($$$) { $$$ }' --filter 'not used'
   # Complexity: sg -p 'if ($$$) { if ($$$) { if ($$$) { $$$ } } }'
   # Security: rg -U 'query\(.*\$\{.*\}' --type js
   ```

3. **Coordination Protocol**
   - Write findings to shared `findings.jsonl` with file locking
   - Mark files needing cross-agent analysis
   - Report progress to `progress.log`

4. **Output Format**
   ```json
   {
     "agent_id": "string",
     "file": "path/to/file",
     "line_start": 10,
     "line_end": 20,
     "type": "dead-code|complexity|security|performance|duplication",
     "severity": "critical|high|medium|low",
     "description": "string",
     "code_snippet": "string",
     "fix_suggestion": "string",
     "fix_example": "string",
     "effort_hours": 0.5,
     "requires_cross_agent": false
   }
   ```

## Phase 4: Execute Analysis

After user approves the distribution:

1. **Initialize Environment**
   ```bash
   mkdir -p .claude-analysis/{agents,results,cache}
   touch .claude-analysis/findings.jsonl
   touch .claude-analysis/progress.log
   ```

2. **Launch Sub-Agents**
   - Each analyzes assigned files independently
   - Continuously append to shared findings file
   - Cache partial results for failure recovery
   - Log progress for monitoring

3. **Monitor & Coordinate**
   - Track completion via progress.log
   - Show real-time stats: "Agent 1: 45/127 files, found 23 issues"
   - Redistribute work if agent fails
   - Allow checking preliminary results

## Phase 5: Synthesize Results

1. **Process Findings**
   - Parse complete findings.jsonl
   - Deduplicate similar issues
   - Cross-reference related problems
   - Apply severity adjustments based on context

2. **Generate Visualizations**
   - Create file-based heat map of issues
   - Generate dependency graph for circular dependencies
   - Show complexity trends over time

3. **Create Roadmap**
   - Group fixes by type and architectural layer
   - Include before/after code examples
   - Add markdown checkboxes for tracking completion
   - Estimate total effort and impact
   - Suggest implementation phases
   - Include progress tracking section
   - Output to `plans/refactor/refactor-roadmap-$(date +%Y%m%d-%H%M%S).md`

4. **Roadmap Format**
   ```markdown
   # Refactoring Roadmap - [Date]
   
   ## Progress Overview
   - [ ] Phase 1: Critical Issues (0/5 completed)
   - [ ] Phase 2: Architecture (0/12 completed)
   - [ ] Phase 3: Code Quality (0/23 completed)
   
   ## Phase 1: Critical Issues (1-2 weeks)
   
   ### 🔴 Security Vulnerabilities
   - [ ] **SQL Injection in UserService** [2h]
     - File: `src/services/UserService.js:45-52`
     - Fix: Use parameterized queries
   - [ ] **XSS in Template Engine** [1h]
     - File: `src/views/renderer.js:102`
     - Fix: Escape HTML entities
   
   ### 🔴 Performance Bottlenecks
   - [ ] **N+1 Query in API** [3h]
     - File: `src/api/products.js:78-92`
     - Fix: Add eager loading
   ```

5. **Export Options**
   - Generate pre-commit configuration to prevent new issues

## Analysis Depth Levels

- **Quick** (5-10 min): File counts, obvious patterns, basic metrics
- **Standard** (15-30 min): Full pattern matching, moderate depth
- **Deep** (45-60 min): Call graphs, data flow, architectural analysis

## Recovery & Caching

- Save state every 50 files analyzed
- Cache results in `.claude-analysis/cache/`
- Allow resuming with `--resume` flag
- Incremental mode analyzes only changed files

<rules>

- MUST scan codebase before creating distribution plan
- MUST present plan for user approval before executing
- MUST assign each file to exactly one primary agent
- MUST provide language-specific patterns for each agent
- MUST use structured JSON output format
- MUST implement progress tracking and monitoring
- MUST handle agent failures gracefully
- SHOULD create 3-8 sub-agents based on codebase size
- SHOULD include code examples in findings
- SHOULD cache results for incremental analysis
- SHOULD provide visual outputs when helpful
- MAY allow cross-agent coordination for complex issues

</rules>