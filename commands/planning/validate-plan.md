---
allowed-tools: Bash(grep), Bash(sed), Bash(head), Bash(tail), DesktopCommander(*)
description: Validate plan documents and ensure they meet requirements for automated implementation
---

Validate that a markdown plan document meets all requirements for automated implementation, and interactively fix any issues.

Requirements are defined in: @/Users/ojash/.claude/docs/PLANNING-REQUIREMENTS.md

## Required Plan Format

A valid plan document must contain:

1. **Branch Specification** (required)
   ```markdown
   Branch: feature/descriptive-name
   ```

2. **Title** (required)
   ```markdown
   # Plan Title
   ```

3. **Metadata Section** (required)
   ```markdown
   Created: YYYY-MM-DD
   Status: active|completed|paused
   Type: refactor|feature|bugfix|migration|other
   ```

4. **Checkboxes** (required)
   - At least one `- [ ]` or `- [x]` item
   - Properly formatted markdown lists

5. **Progress Tracking** (recommended)
   ```markdown
   ## Progress
   - Overall: 0/10 tasks (0%)
   - Phase 1: 0/5 tasks
   - Phase 2: 0/5 tasks
   ```

6. **Task Structure** (recommended)
   - Clear sections/phases
   - Consistent formatting
   - File references where applicable

## Validation Process

### Phase 1: Initial Analysis

1. **Load Document**
   - Read the specified plan file
   - Check if file exists and is readable
   - Verify it's a markdown file

2. **Run Validation Checks**
   ```
   Validating plan document: project-plan.md
   
   ✓ File exists and readable
   ✓ Markdown format detected
   ✗ Missing: Branch specification
   ✗ Missing: Metadata section
   ✓ Found: 15 checkbox tasks
   ⚠ Warning: No progress tracking section
   ✓ Found: Clear section headers
   
   Status: 3 errors, 1 warning
   ```

### Phase 2: Interactive Fixes

For each missing required element:

1. **Branch Specification**
   ```
   ERROR: No branch specification found.
   
   This plan needs a branch name for version control.
   Suggested branch name based on title: feature/implement-auth-system
   
   Options:
   1. Use suggested name
   2. Enter custom branch name
   3. Skip (not recommended)
   
   Choice: 
   ```

2. **Metadata Section**
   ```
   ERROR: No metadata section found.
   
   Let's add plan metadata:
   - Created date: 2024-01-15 (today)
   - Status: active
   - Type: [feature/refactor/bugfix/migration/other]
   
   Select type:
   ```

3. **Progress Tracking**
   ```
   WARNING: No progress tracking found.
   
   Found 15 tasks across 3 sections. Would you like to add progress tracking?
   
   Suggested structure:
   ## Progress
   - Overall: 0/15 tasks (0%)
   - Setup: 0/3 tasks
   - Implementation: 0/8 tasks  
   - Testing: 0/4 tasks
   
   Add progress tracking? [Y/n]:
   ```

### Phase 3: Structure Improvements

1. **Task Formatting**
   - Check for consistent checkbox formatting
   - Suggest fixes for malformed checkboxes
   - Ensure proper list indentation

2. **Section Organization**
   ```
   SUGGESTION: Found tasks without section headers.
   
   Ungrouped tasks:
   - [ ] Update dependencies
   - [ ] Configure linting
   
   Would you like to:
   1. Create new section "Setup Tasks"
   2. Move to existing section
   3. Leave as-is
   ```

3. **Task Details**
   ```
   SUGGESTION: Some tasks lack implementation details.
   
   Task: "Implement user authentication"
   
   Add details? [Y/n]:
   - Estimated time: [e.g., 2h, 1d]
   - Files affected: [e.g., auth.js, user.model.js]
   - Dependencies: [other tasks that must complete first]
   ```

### Phase 4: Apply Updates

1. **Preview Changes**
   ```
   Preview of updates to project-plan.md:
   
   + Branch: feature/implement-auth-system
   + 
   + Created: 2024-01-15
   + Status: active
   + Type: feature
   + 
     # Authentication System Implementation
   + 
   + ## Progress
   + - Overall: 0/15 tasks (0%)
   + - Setup: 0/3 tasks
   + - Implementation: 0/8 tasks
   + - Testing: 0/4 tasks
   
   Apply these changes? [Y/n]:
   ```

2. **Write Updates**
   - Create backup: `project-plan.md.backup`
   - Apply all accepted changes
   - Preserve existing content

### Phase 5: Final Validation

1. **Re-run Checks**
   ```
   Final validation: project-plan.md
   
   ✓ Branch specification: feature/implement-auth-system
   ✓ Metadata section: complete
   ✓ Checkbox tasks: 15 found
   ✓ Progress tracking: configured
   ✓ Structure: well-organized
   
   Status: Ready for implementation! ✅
   ```

2. **Generate Summary**
   ```
   Plan Summary:
   - Branch: feature/implement-auth-system
   - Total tasks: 15 (0 completed)
   - Sections: 3
   - Estimated effort: 24 hours
   
   You can now run: /user:implement-plan project-plan.md
   ```

## Additional Validations

1. **Dependency Checking**
   - Look for "depends on" or "requires" mentions
   - Suggest explicit dependency notation

2. **Time Estimates**
   - Check for consistent time format
   - Calculate total estimated effort

3. **File References**
   - Validate mentioned files exist
   - Suggest adding file paths where missing

4. **Completion Consistency**
   - Ensure completed tasks have dates
   - Check parent/child task consistency

<rules>

- MUST validate all required elements (branch, title, metadata, checkboxes)
- MUST create backup before modifying plan
- MUST preserve all existing content when adding elements
- MUST interactively confirm all changes with user
- SHOULD suggest improvements for warnings
- SHOULD add progress tracking if missing
- SHOULD organize ungrouped tasks into sections
- SHOULD validate file references if present
- MAY suggest task detail enhancements
- MAY add time estimates and dependencies

</rules>