# Claude Code Tools

This directory contains additional CLI tools and utilities that extend Claude Code's capabilities.

## Overview

These tools are designed to be used by Claude Code commands to perform specialized tasks that require dedicated implementations. They can be written in any language and are invoked as standalone executables.

## Structure

```
tools/
├── README.md           # This file
├── [tool-name]/       # Individual tool directories
│   ├── README.md      # Tool documentation
│   ├── [source files] # Implementation files
│   └── [executable]   # Compiled/ready-to-run tool
└── bin/               # Symlinks to executable tools (optional)
```

## Creating New Tools

When adding a new tool:

1. Create a directory with the tool name
2. Include a README.md with:
   - Purpose and functionality
   - Usage examples
   - Installation/build instructions
   - Dependencies
3. Implement the tool
4. Ensure it's executable and callable from Claude Code

## Tool Guidelines

- **Single Purpose**: Each tool should do one thing well
- **CLI Interface**: Accept arguments via command line
- **Error Handling**: Return appropriate exit codes
- **Output Format**: Support both human-readable and machine-parseable output
- **Cross-Platform**: Consider compatibility across macOS, Linux, and Windows

## Usage in Commands

Tools can be invoked from Claude Code commands using the Bash tool:

```bash
# Example in a command
~/.claude/tools/my-tool/my-tool --option value
```

## Available Tools

(Tools will be listed here as they are added)