#!/usr/bin/env python3
"""
MCP Server for FastAPI Tools
This server provides tools for mathematical operations and greetings.
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

# MCP Protocol Models
class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"
    id: Optional[str] = None
    method: str
    params: Optional[Dict[str, Any]] = None

class MCPResponse(BaseModel):
    jsonrpc: str = "2.0"
    id: Optional[str] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None

class MCPTool(BaseModel):
    name: str
    description: str
    inputSchema: Dict[str, Any]

class MCPToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]

# Available tools
TOOLS = [
    MCPTool(
        name="calculate_sum",
        description="Calculate the sum of two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    ),
    MCPTool(
        name="greet_user",
        description="Generate a greeting message for a user",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name of the person to greet"}
            },
            "required": ["name"]
        }
    )
]

class MCPServer:
    def __init__(self):
        self.tools = {tool.name: tool for tool in TOOLS}
    
    async def handle_request(self, request: MCPRequest) -> MCPResponse:
        """Handle MCP protocol requests"""
        try:
            if request.method == "initialize":
                return MCPResponse(
                    id=request.id,
                    result={
                        "protocolVersion": "2024-11-05",
                        "capabilities": {
                            "tools": {}
                        },
                        "serverInfo": {
                            "name": "fastapi-mcp-server",
                            "version": "1.0.0"
                        }
                    }
                )
            
            elif request.method == "tools/list":
                return MCPResponse(
                    id=request.id,
                    result={
                        "tools": [
                            {
                                "name": tool.name,
                                "description": tool.description,
                                "inputSchema": tool.inputSchema
                            }
                            for tool in TOOLS
                        ]
                    }
                )
            
            elif request.method == "tools/call":
                if not request.params or "name" not in request.params:
                    return MCPResponse(
                        id=request.id,
                        error={"code": -32602, "message": "Invalid params"}
                    )
                
                tool_name = request.params["name"]
                arguments = request.params.get("arguments", {})
                
                result = await self.execute_tool(tool_name, arguments)
                return MCPResponse(
                    id=request.id,
                    result={"content": [{"type": "text", "text": str(result)}]}
                )
            
            else:
                return MCPResponse(
                    id=request.id,
                    error={"code": -32601, "message": f"Method not found: {request.method}"}
                )
        
        except Exception as e:
            return MCPResponse(
                id=request.id,
                error={"code": -32603, "message": f"Internal error: {str(e)}"}
            )
    
    async def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Execute the specified tool with given arguments"""
        if tool_name == "calculate_sum":
            a = arguments.get("a", 0)
            b = arguments.get("b", 0)
            result = a + b
            return f"The sum of {a} and {b} is {result}"
        
        elif tool_name == "greet_user":
            name = arguments.get("name", "World")
            return f"Hello, {name}! Welcome to our MCP server!"
        
        else:
            raise ValueError(f"Unknown tool: {tool_name}")

async def main():
    """Main MCP server loop"""
    server = MCPServer()
    
    print("MCP Server started. Listening for requests...", file=sys.stderr)
    
    try:
        while True:
            line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
            if not line:
                break
            
            try:
                request_data = json.loads(line.strip())
                request = MCPRequest(**request_data)
                response = await server.handle_request(request)
                print(json.dumps(response.dict(exclude_none=True)))
                sys.stdout.flush()
            except json.JSONDecodeError:
                continue
            except Exception as e:
                error_response = MCPResponse(
                    id=None,
                    error={"code": -32700, "message": f"Parse error: {str(e)}"}
                )
                print(json.dumps(error_response.dict(exclude_none=True)))
                sys.stdout.flush()
    
    except KeyboardInterrupt:
        print("MCP Server shutting down...", file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(main())
