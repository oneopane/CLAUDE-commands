# Linear Workflow Commands

A comprehensive workflow for managing Linear initiatives, projects, and issues with living documents and dependency graphs.

## Core Concepts

### 1. **Living Documents**
Plans start as stubs and progressively elaborate as you work. Each level (initiative → project → issue) inherits context from its parent.

### 2. **Dependency Graph**
A dual-system with JSON for data and Mermaid for visualization. The graph tracks relationships and enables smart context loading.

### 3. **Progressive Elaboration**
Start with high-level plans and add detail as you progress. Knowledge propagates both up and down the hierarchy.

## Command Naming Convention

Commands are numbered to indicate typical workflow order:
- **1x** - Planning & Analysis (create → analyze at each level)
- **2x** - Working & Elaboration
- **3x** - Daily Operations & Maintenance
- **4x** - (Reserved for future commands)

## Command Overview

### Group 1: Planning & Analysis
- `linear-1a-init-initiative.md` - Create full initiative structure with stubs
- `linear-1b-analyze-initiative.md` - High-level initiative planning
- `linear-1c-init-project.md` - Add project to existing initiative
- `linear-1d-analyze-project.md` - Detailed project breakdown
- `linear-1e-analyze-issue.md` - Implementation planning

### Group 2: Working & Elaboration
- `linear-2a-elaborate-plan.md` - Progressively add detail to any plan
- `linear-2b-work-context.md` - Load smart context (2 graph hops)

### Group 3: Daily Operations
- `linear-3a-daily-check.md` - Daily planning assistant
- `linear-3b-update-graph.md` - Manage dependency relationships
- `linear-3c-sync-plans.md` - Synchronize plans across hierarchy
- `linear-3d-impact-analysis.md` - Analyze change impacts
- `linear-3e-show-graph.md` - Visualize dependencies

## Typical Workflow

1. **Start Initiative**
   ```bash
   @linear/linear-1a-init-initiative
   @linear/linear-1b-analyze-initiative
   ```
   Create initiative structure and analyze scope.

2. **Create Projects**
   ```bash
   @linear/linear-1c-init-project
   @linear/linear-1d-analyze-project
   ```
   Add projects and break down into issues.

3. **Plan Implementation**
   ```bash
   @linear/linear-1e-analyze-issue
   @linear/linear-2a-elaborate-plan
   ```
   Detail implementation plans.

4. **Daily Work**
   ```bash
   @linear/linear-3a-daily-check
   @linear/linear-2b-work-context
   ```
   Get focused context and priorities.

5. **Maintain & Track**
   ```bash
   @linear/linear-3b-update-graph
   @linear/linear-3c-sync-plans
   @linear/linear-3e-show-graph
   ```
   Keep plans and dependencies current.

## Data Structure

```
.claude/linear/
├── initiatives/
│   └── {id}/
│       ├── plan.md
│       ├── graph.json
│       └── projects/
├── context/
│   └── current.json
└── graphs/
    └── visualizations/
```

## Graph Visualization

Use the Python script to generate Mermaid diagrams:
```bash
python scripts/graph_visualizer.py graph.json --view full
```

View options: full, critical, status

## Best Practices

1. **Start with Stubs** - Don't over-plan initially
2. **Elaborate as Needed** - Add detail when you need it
3. **Update the Graph** - Keep dependencies current
4. **Sync Regularly** - Propagate learnings
5. **Check Daily** - Use daily-check for focus

## Requirements

- Linear MCP server configured
- Python 3.x for graph visualization
- Access to Linear workspace