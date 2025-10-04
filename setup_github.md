# GitHub Setup Instructions

## 1. Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Repository name: `mcp-fastapi-server`
5. Description: "MCP Server built with FastAPI and integrated with Gemini CLI"
6. Make it **Public**
7. Don't initialize with README (we already have one)
8. Click "Create repository"

## 2. Push Your Code to GitHub

Run these commands in your project directory:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit the files
git commit -m "Initial commit: MCP FastAPI Server with Gemini CLI integration"

# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mcp-fastapi-server.git

# Push to GitHub
git push -u origin main
```

## 3. Screen Recording Requirements

You need to create a screen recording that shows:

1. **MCP Server Running**: Show the FastAPI server running on localhost:8000
2. **Gemini CLI MCP List**: Run `gemini mcp list` command
3. **MCP Tools Usage**: Demonstrate using the MCP tools through Gemini CLI

### Recording Script:

1. Start screen recording software (OBS Studio, Bandicam, or built-in Windows Game Bar)
2. Open terminal/command prompt
3. Show the project files
4. Run: `uvicorn main:app --reload --port 8000`
5. Open browser to http://localhost:8000/docs
6. Show the API documentation
7. Test endpoints in the browser
8. Stop the FastAPI server
9. Configure Gemini CLI with the MCP server
10. Run: `gemini mcp list`
11. Run: `gemini mcp call calculate_sum --a 10 --b 5`
12. Run: `gemini mcp call greet_user --name "Student"`
13. Stop recording

## 4. Upload Screen Recording

1. Upload your screen recording to YouTube (unlisted) or GitHub Releases
2. Add the link to your README.md file
3. Update the README with the video link

## 5. Final Repository Structure

Your GitHub repository should contain:
- `main.py` - FastAPI web server
- `mcp_server.py` - MCP protocol server
- `mcp_config.json` - Gemini CLI configuration
- `requirements.txt` - Python dependencies
- `README.md` - Documentation with video link
- `.gitignore` - Git ignore file
- Screen recording (link or file)

## 6. Submission Checklist

- [ ] GitHub repository created and public
- [ ] All code files pushed to GitHub
- [ ] Screen recording created and uploaded
- [ ] README.md updated with video link
- [ ] Repository is properly documented
- [ ] All requirements from assignment are met
