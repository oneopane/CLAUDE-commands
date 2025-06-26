---
allowed-tools: Bash(date), Bash(pwd)
description: Interactively create a detailed implementation plan from a feature description following planning requirements
---

Create a comprehensive implementation plan from a feature description that follows all planning requirements defined in:

@/Users/ojash/.claude/docs/PLANNING-REQUIREMENTS.md

This command will guide you through creating a properly structured plan document with all mandatory sections, recommended organization, and optional metadata for enhanced tracking.

Current directory: !`pwd`
Today's date: !`date +%Y-%m-%d`

## Phase 1: Feature Analysis & Scope Definition

**Feature to plan:** $ARGUMENTS

Let's analyze and scope this feature:

1. **Feature Understanding**
   - What problem does this feature solve?
   - Who are the primary users/stakeholders?
   - What are the core functionalities required?
   - What are the acceptance criteria for completion?

2. **Technical Scope**
   - What components/systems will be affected?
   - Are there any external dependencies?
   - What's the estimated complexity level (Simple/Medium/Complex)?
   - Any integration requirements?

3. **Constraints & Considerations**
   - Timeline constraints?
   - Resource limitations?
   - Technical debt considerations?
   - Breaking changes or migration needs?

## Phase 2: Plan Metadata Configuration

I'll help you configure the required metadata for your plan:

### Branch Specification
What type of work is this?
1. `feature/` - New functionality
2. `bugfix/` - Fixing existing issues  
3. `refactor/` - Code improvement without behavior changes
4. `chore/` - Maintenance, migrations, tooling

Choose type [1-4]: 

### Plan Classification
- **Type**: [feature|bugfix|refactor|migration|other]
- **Status**: active (starting new plan)
- **Created**: !`date +%Y-%m-%d`

### Branch Naming
Based on the feature, suggest a descriptive branch name:
- Pattern: `<type>/<feature-description-kebab-case>`
- Example: `feature/user-authentication-system`

Your branch name: 

## Phase 3: Interactive Implementation Scoping

Now let's interactively scope out exactly what needs to be implemented. I'll ask targeted questions to understand the full requirements before breaking down into tasks.

### Core Functionality Deep Dive

**Let's start with the main user journey:**

1. **User Flow Analysis**
   - Walk me through the complete user flow from start to finish
   - What are the key user actions at each step?
   - What happens when things go wrong (error states)?
   - Are there different user types with different flows?

2. **Data Requirements**
   - What data does this feature create, read, update, or delete?
   - What's the data structure/schema needed?
   - Where does the data come from? (user input, APIs, calculations, etc.)
   - How long should data be retained?
   - Any data validation or transformation requirements?

3. **Interface Requirements**
   - What UI components are needed? (forms, lists, modals, etc.)
   - What information needs to be displayed to users?
   - Any specific design/styling requirements?
   - Mobile responsive considerations?
   - Accessibility requirements?

4. **Business Logic**
   - What are the core business rules?
   - Any calculations or processing logic?
   - What validation rules apply?
   - Any conditional logic based on user type/permissions?

### Integration & Dependencies Analysis

**Let's identify all the moving pieces:**

5. **System Integration**
   - What existing systems/APIs does this integrate with?
   - Are there any external services involved?
   - Database changes needed?
   - Authentication/authorization requirements?

6. **Performance Considerations**
   - Expected usage volume/load?
   - Any caching requirements?
   - Real-time vs. batch processing needs?
   - Response time requirements?

7. **Edge Cases & Error Handling**
   - What could go wrong with this feature?
   - How should errors be handled and displayed?
   - What happens with invalid input?
   - Network failures, timeouts, etc.?

### Technical Architecture Questions

**Let's define the technical approach:**

8. **Component Architecture**
   - Frontend: What major components/pages are needed?
   - Backend: What API endpoints are required?
   - Database: What tables/collections need changes?
   - Are there any new services/modules to create?

9. **State Management**
   - What application state needs to be managed?
   - Where should state live? (local, global, server, cache)
   - Any real-time state synchronization needs?

10. **Configuration & Setup**
    - Any new environment variables or config?
    - New dependencies or packages needed?
    - Database migrations required?
    - Any deployment considerations?

### Quality & Testing Strategy

**Let's plan for quality:**

11. **Testing Requirements**
    - What should be unit tested?
    - Integration test scenarios?
    - End-to-end test cases?
    - Any performance/load testing needed?

12. **Documentation Needs**
    - API documentation updates?
    - User documentation/help text?
    - Developer documentation?
    - Configuration/setup docs?

### Risk Assessment & Validation

**Let's identify potential blockers:**

13. **Technical Risks**
    - Any unknown/complex technical challenges?
    - Dependencies on other teams/systems?
    - New technologies or patterns being used?
    - Potential performance bottlenecks?

14. **Implementation Validation**
    Based on everything we've discussed:
    - Does the scope feel complete and well-defined?
    - Are there any gaps or unclear areas?
    - Any assumptions that need validation?
    - Should anything be broken into separate features/phases?

### Scope Summary & Confirmation

Before moving to task breakdown, I'll provide a comprehensive scope summary:

```
## Implementation Scope Summary

### Core Components
- [List all major components identified]

### User Flows  
- [List all user journeys mapped out]

### Technical Requirements
- [List all technical specifications]

### Dependencies & Integrations
- [List all external dependencies]

### Quality Requirements
- [List testing and documentation needs]

### Risk Factors
- [List identified risks and mitigation approaches]
```

**Scope Confirmation**: Does this capture the complete implementation scope? Any additions or modifications needed?

## Phase 4: Task Breakdown & Organization

Let's break down the feature into actionable tasks:

### Task Identification Process
1. **High-Level Phases**: What are the major phases? (e.g., Setup, Core Development, Integration, Testing)
2. **Task Granularity**: Aim for tasks that take 0.5-4 hours each
3. **Dependencies**: Which tasks depend on others?
4. **Parallel Work**: What can be done simultaneously?

### Task Categories to Consider
- **Setup & Configuration**
  - Environment setup
  - Dependencies installation
  - Configuration files
  
- **Backend/API Development**
  - Data models
  - API endpoints
  - Business logic
  - Database changes
  
- **Frontend Development**
  - UI components
  - State management
  - User interactions
  - Styling
  
- **Integration & Testing**
  - API integration
  - Unit tests
  - Integration tests
  - E2E tests
  
- **Documentation & Deployment**
  - Code documentation
  - User documentation
  - Deployment scripts
  - Monitoring setup

For each task, I'll help you define:
- **Clear description**: What exactly needs to be done?
- **Time estimate**: How long will this take? [30min|1h|2h|4h|1day]
- **File references**: What files will be created/modified?
- **Dependencies**: What must be done first?
- **Priority**: Critical/High/Medium/Low

## Phase 5: Plan Structure Generation

Based on your inputs, I'll generate a plan following this structure:

```markdown
Branch: <type>/<descriptive-name>

# <Feature Title>

Created: <YYYY-MM-DD>
Status: active
Type: <feature|bugfix|refactor|migration|other>

## Overview
<Brief description of the feature and its purpose>

## Progress
- Overall: 0/<total> tasks (0%)
- Phase 1: 0/<phase1_count> tasks
- Phase 2: 0/<phase2_count> tasks
- Phase N: 0/<phaseN_count> tasks

## Phase 1: <Phase Name>

- [ ] <Task description> [<time_estimate>]
  - file: <file_path>
  - depends_on: ["<dependency_task>"]
  - priority: <HIGH|MEDIUM|LOW>

- [ ] <Next task>

## Phase 2: <Next Phase>

<Continue pattern...>

## Additional Metadata (if complex)

### File Impact Analysis
- **New files**: List of files to be created
- **Modified files**: List of files to be changed
- **Dependencies**: External packages/services

### Risk Assessment
- **Technical risks**: Potential implementation challenges
- **Timeline risks**: Dependencies that could cause delays
- **Integration risks**: Potential conflicts with existing code

### Success Criteria
- [ ] <Measurable outcome 1>
- [ ] <Measurable outcome 2>
- [ ] <Performance/quality criteria>
```

## Phase 6: Plan Validation & Creation

### Pre-Creation Validation
I'll verify your plan meets all requirements:

**Mandatory Elements ✓**
- [ ] Branch specification (correct format)
- [ ] Document title (H1 heading)
- [ ] Metadata section (Created, Status, Type)
- [ ] At least one checkbox task

**Quality Checks ✓**  
- [ ] All tasks are actionable (no TBD/TODO)
- [ ] Time estimates are reasonable
- [ ] Dependencies are clear
- [ ] File references are valid paths
- [ ] Proper markdown formatting

### Plan Location
Where should this plan be saved?

Current project structure:
```
!`find . -name "*.md" -path "./planning/*" 2>/dev/null | head -5`
```

Suggested locations:
1. `./planning/plans/<feature-name>-plan.md` - For project-specific plans
2. `./docs/implementation/<feature-name>.md` - For documentation-focused projects
3. `./PLANNING.md` - For simple projects (single plan)

Choose location: 

### Plan Creation
I'll create the plan file with:
- Proper formatting and structure
- All required metadata
- Your defined tasks and organization
- Validation against planning requirements

### Next Steps Guidance
After creation, I'll provide:
- Plan file location and usage instructions
- Suggested implementation commands:
  - `/user:planning:implement-plan` - Sequential implementation
  - `/user:planning:validate-plan-and-parallelize` - For parallel execution
- Integration with Linear (if using Linear integration)
- Version control recommendations

<rules>

- MUST collect all mandatory metadata (Branch, Title, Created, Status, Type)
- MUST ensure at least one actionable checkbox task
- MUST validate branch naming follows pattern: `<type>/<descriptive-name>`
- MUST use today's date for Created field
- MUST generate properly formatted markdown
- MUST validate plan against PLANNING-REQUIREMENTS.md before creation
- SHOULD break features into 0.5-4 hour tasks
- SHOULD organize tasks into logical phases
- SHOULD include time estimates for better tracking
- SHOULD identify task dependencies
- SHOULD suggest file paths for implementation tasks
- MAY include parallel execution metadata for complex features
- MAY suggest related Linear issues or documentation needs
- MAY recommend additional planning commands for complex features

</rules>