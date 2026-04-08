# Instructions for Claude Code

## What Claude Code Should Do

Read `PROJECT_SPEC.md` and `API_REFERENCE.md` in the same folder FIRST — they contain all the project and LTX-2 API specifications.

Then build a Python MCP server using FastMCP that wraps the LTX-2 cloud API to generate video from the Claude chat.

## Steps

### 1. Environment Setup
```bash
cd path/to/ltxintegration/
python -m venv .venv
.venv\Scripts\activate
pip install fastmcp httpx python-dotenv
```

### 2. Create the MCP Server (`src/ltx_mcp_server.py`)

The server must expose 4 tools:
- `text_to_video` — generates video from a text prompt
- `image_to_video` — animates an image (supports local path → converts to base64)
- `audio_to_video` — generates video from audio
- `check_balance` — (optional) shows remaining credits if endpoint is available

**CRITICAL DETAIL:** The LTX-2 API is **SYNCHRONOUS**. The HTTP response directly contains the MP4 file in the body. There is no task_id, no polling. Use an HTTP timeout of at least 300 seconds.

**Flow for each tool:**
1. Read the API key from env `LTXV_API_KEY`
2. Validate parameters (model, resolution, duration must be supported combinations — see API_REFERENCE.md)
3. POST to `https://api.ltx.video/v1/{endpoint}` with header `Authorization: Bearer {key}`
4. Wait for the response (can take 1-3 minutes)
5. Save the response bytes as `.mp4` in the `outputs/` folder
6. Return to Claude the saved file path + useful metadata (duration, model, resolution, estimated cost)

**For image_to_video with a local image:**
- If `image_path` is a local path (not a URL), read the file and convert it to a base64 data URI
- Format: `data:image/{ext};base64,{base64_data}`
- Pass it as the `image_uri` field in the API request

### 3. Error Handling
- If the API key is not set → clear error with instructions
- If the response is not 200 → parse the error JSON and return a readable message
- If timeout → message explaining that generation failed due to timeout
- Estimated cost calculation: `duration * cost_per_second` based on model and resolution

### 4. Registration in Claude Code
Once the server is complete, register it with:
```bash
claude mcp add ltx-video -- python ./src/ltx_mcp_server.py
```

Or for Claude Desktop, add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ltx-video": {
      "command": "python",
      "args": ["./src/ltx_mcp_server.py"],
      "env": {
        "LTXV_API_KEY": "your_key_here"
      }
    }
  }
}
```

### 5. Test
Test with:
```
"Generate a 6-second video of an eagle flying over mountains at sunset, fast model, 1080p"
```

## Reference Files in the Folder
- `PROJECT_SPEC.md` — Full project specification
- `API_REFERENCE.md` — LTX-2 API documentation with all endpoints, parameters, and error codes
- `.env.example` — Template for environment variables
- `requirements.txt` — Python dependencies
