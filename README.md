# AI Agent

## Project Overview
**AI Agent** is an intelligent automation tool built with Google's Generative AI (Gemini 2.5 Flash) that intelligently interacts with the file system and executes code. It functions as an AI-powered coding assistant capable of understanding natural language requests and performing complex file operations and Python executions.

## Core Purpose
The project demonstrates autonomous agent capabilities where users can issue natural language commands, and the AI agent autonomously:
- Analyzes file structures and retrieves file contents
- Executes Python scripts dynamically
- Creates and modifies files programmatically
- Makes intelligent decisions about which operations to perform based on user requests

## Architecture & Components

### Main Application (`main.py`)
- **Entry Point**: Orchestrates the AI agent interaction loop
- **Key Features**:
  - Integrates with Google Generative AI SDK (Gemini 2.5 Flash model)
  - Implements a multi-turn conversation loop (max 20 iterations)
  - Manages function calling and response handling
  - Supports verbose mode for debugging and monitoring
  - Processes user prompts via command-line arguments
  - Handles API key management through environment variables

### Function System (`call_function.py`)
Implements a function-calling mechanism that bridges natural language requests to actual system operations:
- **Available Functions**:
  - `get_files_info` - List and inspect directory contents
  - `get_file_content` - Read file contents with full text extraction
  - `write_file` - Create or overwrite files with specified content
  - `run_python_file` - Execute Python scripts with optional arguments

- **Function Mapping**: Routes AI-generated function calls to appropriate handlers
- **Sandboxing**: All operations are restricted to the `./calculator` working directory for security

### System Prompt (`prompts.py`)
Defines the AI agent's behavior and capabilities:
- Instructs the model to act as a "helpful AI coding agent"
- Establishes available operations and their scope
- Clarifies that relative paths are used (working directory is injected automatically)

### Calculator Module
A practical implementation showcasing the agent's capabilities:
- `calculator/main.py` - Entry point for calculator operations
- Integrates with `pkg.calculator` and `pkg.render` modules
- Evaluates mathematical expressions and formats JSON output
- Demonstrates how the agent can execute delegated tasks

## Technology Stack
- **Runtime**: Python 3.13+
- **AI Model**: Google Generative AI (Gemini 2.5 Flash)
- **Key Dependencies**:
  - `google-genai` (1.12.1) - Google AI SDK
  - `python-dotenv` (1.1.0) - Environment variable management
- **Package Manager**: UV (modern Python package manager)

## How It Works

1. **User Input**: User provides a natural language request via CLI
2. **AI Processing**: Gemini model analyzes the request and determines needed operations
3. **Function Execution**: The agent calls appropriate functions (file ops, code execution)
4. **Agentic Loop**: Results are fed back to the model for further analysis (up to 20 iterations)
5. **Final Response**: Model generates a natural language response with results

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anandki1209/aiagent.git
   cd aiagent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using UV:
   ```bash
   uv sync
   ```

3. Set up environment variables:
   ```bash
   export GEMINI_API_KEY="your-google-api-key"
   ```

## Usage

Run the AI Agent with a natural language request:

```bash
python main.py "your task or question"
```

### Examples
```bash
# List files in calculator directory
python main.py "What files are in the calculator directory?"

# Run calculator operations
python main.py "Calculate 5 plus 3"

# Create or modify files
python main.py "Create a new Python file with a hello world function"
```

### Verbose Mode
Enable detailed output for debugging:
```bash
python main.py "your task" --verbose
```

This displays token usage, function calls, and intermediate results.

## Project Structure
```
aiagent/
├── main.py                    # Main application entry point
├── call_function.py          # Function calling mechanism
├── prompts.py                # System prompt definitions
├── config.py                 # Configuration management
├── pyproject.toml            # Project metadata and dependencies
├── calculator/               # Calculator module
│   ├── main.py              # Calculator entry point
│   └── pkg/                 # Calculator implementation
├── functions/               # Function implementations
│   ├── get_files_info.py    # File listing functionality
│   ├── get_file_content.py  # File reading functionality
│   ├── write_file.py        # File writing functionality
│   └── run_python_file.py   # Python execution functionality
└── README.md                # This file
```

## Key Design Patterns

### Agentic Loop
The application implements a feedback loop where:
- Model generates function calls based on user requests
- Functions execute and return results
- Results are fed back to model for further processing
- Loop continues until model provides final answer or iteration limit reached

### Security Sandboxing
- All file operations confined to `./calculator` directory
- Working directory automatically injected for safety
- Prevents arbitrary file system access

### Extensibility
The function system is designed for easy extension:
- New functions can be added by creating schema definitions
- Functions are registered in the `function_map` dictionary
- Follows consistent pattern for integration with Gemini API

## Development Notes
- Follow coding standards for maintainability
- Keep documentation synchronized with code changes
- Use meaningful commit messages describing changes
- Test agentic loops thoroughly with various prompts
- Monitor token usage in verbose mode for cost optimization

## Future Enhancements
- Add more specialized function modules beyond calculator
- Implement persistent conversation history
- Add error recovery and retry mechanisms
- Create CLI interface improvements
- Support for multiple AI models
- Persistent state management across sessions

## License
This project is open source and available for educational and commercial use.

## Contributing
Contributions are welcome! Please follow the coding standards and update documentation accordingly.

For more information or questions, please reach out to the project maintainers.