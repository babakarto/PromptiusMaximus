# LTX-2 MCP Server — Project Specification

## Goal
Create an MCP (Model Context Protocol) server in Python with FastMCP that wraps the LTX-2 (Lightricks) cloud API, allowing video generation directly from the Claude chat (Claude Code or Claude Desktop).

## Architecture

```
User prompt in Claude
        ↓
   Claude calls the MCP tool
        ↓
   MCP Server (Python/FastMCP)
        ↓
   POST to LTX-2 API (cloud, on Lightricks servers)
        ↓
   Wait for synchronous response (~1-3 min)
        ↓
   Response = direct MP4 file → save to local folder
        ↓
   Return video path to Claude
```

## Tech Stack
- **Python 3.12+**
- **FastMCP** (`pip install fastmcp`)
- **httpx** for async HTTP calls
- **python-dotenv** to manage the API key
- Video is generated on LTX cloud servers (H100), NOT on local GPU

## MCP Tools to Expose

### 1. `text_to_video`
Generates a video from a text prompt.
- **Parameters:**
  - `prompt` (str, required): Scene description
  - `model` (str, default "ltx-2-fast"): "ltx-2-fast" or "ltx-2-pro"
  - `resolution` (str, default "1920x1080"): "1920x1080", "2560x1440", "3840x2160"
  - `duration` (int, default 6): Duration in seconds (6-20)
  - `fps` (int, default 25): Frame rate (25 or 50)
  - `seed` (int, optional): Seed for reproducibility
- **Returns:** Local path of the downloaded video + download URL

### 2. `image_to_video`
Animates a static image.
- **Parameters:**
  - `prompt` (str, required): Description of the movement/animation
  - `image_path` (str, required): Local path of the input image
  - `model` (str, default "ltx-2-fast"): "ltx-2-fast" or "ltx-2-pro"
  - `resolution` (str, default "1920x1080")
  - `duration` (int, default 6)
  - `fps` (int, default 25)
  - `seed` (int, optional)
- **Returns:** Local path of the video + URL

### 3. `audio_to_video`
Generates video synchronized to audio.
- **Parameters:**
  - `prompt` (str, required): Visual description
  - `audio_path` (str, required): Local path of the audio file
  - `model` (str, default "ltx-2-pro"): Only "ltx-2-pro" supported
  - `resolution` (str, default "1920x1080")
- **Returns:** Local path of the video + URL

### 4. `check_status`
Checks the status of an ongoing generation.
- **Parameters:**
  - `task_id` (str, required)
- **Returns:** Current task status

## Configuration

### `.env` File
```
LTXV_API_KEY=your_api_key_here
LTX_OUTPUT_DIR=./outputs
```

### Folder Structure
```
ltxintegration/
├── PROJECT_SPEC.md          # This spec
├── API_REFERENCE.md          # LTX-2 API documentation
├── CLAUDE_CODE_INSTRUCTIONS.md  # Instructions for Claude Code
├── src/
│   └── ltx_mcp_server.py    # The main MCP server
├── .env.example              # Template for environment variables
├── requirements.txt          # Python dependencies
├── outputs/                  # Folder where generated videos are saved
└── README.md                 # Usage documentation
```

## Generation Flow (Detail)

**IMPORTANT: The API is SYNCHRONOUS** — it returns the MP4 file directly in the HTTP response body.
There is no polling, no task_id. The connection stays open until the video is ready (typically 1-3 minutes).

1. The user asks Claude to generate a video
2. Claude invokes the appropriate MCP tool (e.g., `text_to_video`)
3. The MCP server:
   a. Validates the parameters
   b. Sends a POST to `https://api.ltx.video/v1/text-to-video` with Bearer token
   c. Waits for the response (300-second timeout) — the API directly returns the MP4 file
   d. Saves the video in `outputs/` with the name `ltx_{timestamp}.mp4`
   e. Returns to Claude: local path + metadata (duration, resolution, estimated cost)

## Error Handling
- HTTP timeout after 5 minutes → error with clear message
- Missing API key → immediate error with instructions
- Rate limit (429) → retry with exponential backoff
- Failed generation → report the API error

## Integration with Claude Code
Once built, the server should be registered in Claude Code with:
```bash
claude mcp add ltx-video -- python src/ltx_mcp_server.py
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

## Pricing Reminder
| Model | 1080p | 1440p | 4K |
|-------|-------|-------|-----|
| ltx-2-fast | $0.04/s | $0.08/s | $0.16/s |
| ltx-2-pro | $0.06/s | $0.12/s | $0.24/s |
| audio-to-video | $0.10/s | — | — |

Example: 10s video 1080p fast = $0.40
