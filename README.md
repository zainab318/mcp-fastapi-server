# MCP FastAPI Server 🚀

This is a sample MCP Server built using **FastAPI** and integrated with **Gemini CLI**.

## Features
- **FastAPI Web Server** with REST endpoints
- **MCP Protocol Server** for Gemini CLI integration
- **Mathematical Operations** (sum calculation)
- **Greeting Service** (personalized greetings)

## Project Structure
```
mcp_fastapi_server/
├── main.py              # FastAPI web server
├── mcp_server.py        # MCP protocol server
├── mcp_config.json      # Gemini CLI configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run FastAPI Server
```bash
uvicorn main:app --reload --port 8000
```
The server will be available at: http://localhost:8000
API Documentation: http://localhost:8000/docs

### 3. Test MCP Server
```bash
python mcp_server.py
```

### 4. Configure Gemini CLI
Copy the `mcp_config.json` to your Gemini CLI configuration directory:
```bash
# On Windows
copy mcp_config.json %APPDATA%\gemini\mcp_config.json

# On macOS/Linux
cp mcp_config.json ~/.config/gemini/mcp_config.json
```

## Available Endpoints

### FastAPI Endpoints
- `GET /` - Server status
- `POST /sum` - Calculate sum of two numbers
- `POST /greet` - Generate greeting message

### MCP Tools
- `calculate_sum` - Calculate sum of two numbers
- `greet_user` - Generate personalized greeting

## Usage Examples

### FastAPI Usage
```bash
# Test sum endpoint
curl -X POST "http://localhost:8000/sum" \
     -H "Content-Type: application/json" \
     -d '{"a": 5, "b": 3}'

# Test greet endpoint
curl -X POST "http://localhost:8000/greet" \
     -H "Content-Type: application/json" \
     -d '{"name": "World"}'
```

### Gemini CLI Usage
```bash
# List available MCP tools
gemini mcp list

# Use MCP tools
gemini mcp call calculate_sum --a 5 --b 3
gemini mcp call greet_user --name "Alice"
```

## Screen Recording
This repository includes a screen recording demonstrating:
1. MCP server running
2. Gemini CLI MCP list command
3. Usage of MCP tools through Gemini CLI
