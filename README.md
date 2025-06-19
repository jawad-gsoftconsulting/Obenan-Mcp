# Obenan-MCP (Hello World MCP Tool)

A simple Model Context Protocol (MCP) tool that returns "Hello World Tool is called" when invoked.

## Overview

This is a minimal MCP tool implementation that demonstrates how to create, install, and use MCP tools with Windsurf. The tool responds to calls with a simple text message.

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (for cloning the repository)

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone git@github.com:jawad-gsoftconsulting/Obenan-Mcp.git
   cd Obenan-Mcp/hello-mcp
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

3. **Verify installation**:
   ```bash
   # Test if the command-line tool is available
   which hello-mcp
   ```

## Usage

### Direct Command-Line Usage

You can test the MCP tool directly from the command line:

```bash
echo '{"tool":"hello_world","args":{}}' | hello-mcp
```

This should return: `Hello World Tool is called`

### Windsurf Integration

To use this MCP tool with Windsurf:

1. **Create or update your mcp_config.json file**:
   ```json
   {
     "mcpServers": {
       "hello_world": {
         "command": "hello-mcp",
         "args": []
       }
     }
   }
   ```

2. **Place this file in the appropriate Windsurf configuration directory**:
   - On macOS: `~/.codeium/windsurf/mcp_config.json`
   - On Linux: `~/.codeium/windsurf/mcp_config.json`
   - On Windows: `%APPDATA%\Codeium\windsurf\mcp_config.json`

3. **Restart Windsurf** to pick up the configuration changes.

4. **Test the tool** by calling the `hello_world` tool from Windsurf.

## Server Setup

To deploy this MCP tool on a server:

1. **Clone the repository on your server**:
   ```bash
   git clone git@github.com:jawad-gsoftconsulting/Obenan-Mcp.git
   cd Obenan-Mcp/hello-mcp
   ```

2. **Install the package**:
   ```bash
   pip install -e .
   ```

3. **Create a systemd service** (Optional, for Linux servers):
   
   Create a file at `/etc/systemd/system/hello-mcp.service`:
   ```
   [Unit]
   Description=Hello World MCP Service
   After=network.target

   [Service]
   User=<your-server-user>
   WorkingDirectory=/path/to/Obenan-Mcp/hello-mcp
   ExecStart=/usr/local/bin/hello-mcp
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

4. **Start and enable the service** (if using systemd):
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start hello-mcp
   sudo systemctl enable hello-mcp
   ```

5. **Configure your clients** to point to the server where this MCP tool is running.

## Development

To modify the tool's behavior:

1. Edit the source files in `src/hello_mcp/`
2. Reinstall the package with `pip install -e .` to reflect changes
3. Test your changes

## Project Structure

- `src/hello_mcp/server.py`: Contains the main implementation of the MCP tool.
- `src/hello_mcp/__init__.py`: Package initialization and entrypoint.
- `pyproject.toml`: Project metadata and dependencies.

## License

This project is open source and available under the [MIT License](LICENSE).
