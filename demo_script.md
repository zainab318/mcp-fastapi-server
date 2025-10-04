# Screen Recording Demo Script

## Pre-Recording Setup
1. Close all unnecessary applications
2. Open a clean terminal/command prompt
3. Navigate to your project directory
4. Start screen recording software

## Recording Steps (5-7 minutes total)

### Step 1: Show Project Structure (30 seconds)
```bash
# Show the project files
dir
# or
ls -la
```

### Step 2: Start FastAPI Server (1 minute)
```bash
# Install dependencies (if needed)
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload --port 8000
```

**Say**: "Here I'm starting the FastAPI server on port 8000"

### Step 3: Show API Documentation (1 minute)
- Open browser to http://localhost:8000/docs
- Show the interactive API documentation
- Test the `/sum` endpoint with values like a=5, b=3
- Test the `/greet` endpoint with name="Demo"

**Say**: "This is the FastAPI server running with interactive API documentation. I can test the endpoints directly here."

### Step 4: Stop FastAPI Server (30 seconds)
- Press Ctrl+C to stop the server
- Open a new terminal window

### Step 5: Test MCP Server (1 minute)
```bash
# Test the MCP server directly
python mcp_server.py
```

**Say**: "Now I'm testing the MCP server directly to ensure it works with the MCP protocol."

### Step 6: Configure Gemini CLI (1 minute)
```bash
# Show the MCP configuration
type mcp_config.json
# or
cat mcp_config.json

# Copy configuration to Gemini CLI directory
copy mcp_config.json %APPDATA%\gemini\mcp_config.json
```

**Say**: "I'm configuring Gemini CLI to use our MCP server by copying the configuration file."

### Step 7: Demonstrate Gemini CLI Integration (2 minutes)
```bash
# List available MCP tools
gemini mcp list

# Use the calculate_sum tool
gemini mcp call calculate_sum --a 15 --b 25

# Use the greet_user tool
gemini mcp call greet_user --name "Professor"

# Show another calculation
gemini mcp call calculate_sum --a 100 --b 200
```

**Say**: "Now I'm using Gemini CLI to interact with our MCP server. You can see it lists our tools and successfully executes them."

### Step 8: Wrap Up (30 seconds)
- Show the GitHub repository URL
- Mention the screen recording is included
- End recording

## Key Points to Emphasize

1. **FastAPI Server**: Show it's a real web server with documentation
2. **MCP Protocol**: Demonstrate the MCP server works independently
3. **Gemini CLI Integration**: Show seamless integration with CLI
4. **Tool Functionality**: Both tools work correctly
5. **Professional Setup**: Clean code, documentation, and configuration

## Troubleshooting Tips

- If Gemini CLI isn't installed: `pip install google-generativeai`
- If MCP commands don't work: Check the configuration file path
- If server doesn't start: Check if port 8000 is available
- If tools don't respond: Verify the MCP server is running correctly

## Recording Quality Tips

- Use a clear, readable font in terminal
- Speak clearly and at moderate pace
- Show the actual output of commands
- Keep the recording focused and concise
- Test everything before recording
