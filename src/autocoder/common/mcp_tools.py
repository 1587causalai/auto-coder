from typing import Dict, Any
from byzerllm import prompt

@prompt()
def mcp_prompt() -> Dict[str, Any]:
    """
    ## use_mcp_tool
    Description: Request to use a tool provided by a connected MCP server. Each MCP server can provide multiple tools with different capabilities. Tools have defined input schemas that specify required and optional parameters.
    Parameters:
    - server_name: (required) The name of the MCP server providing the tool
    - tool_name: (required) The name of the tool to execute
    - arguments: (required) A JSON object containing the tool's input parameters, following the tool's input schema
    Usage:
    <use_mcp_tool>
    <server_name>server name here</server_name>
    <tool_name>tool name here</tool_name>
    <arguments>
    {
      "param1": "value1",
      "param2": "value2"
    }
    </arguments>
    </use_mcp_tool>

    ## access_mcp_resource
    Description: Request to access a resource provided by a connected MCP server. Resources represent data sources that can be used as context, such as files, API responses, or system information.
    Parameters:
    - server_name: (required) The name of the MCP server providing the resource
    - uri: (required) The URI identifying the specific resource to access
    Usage:
    <access_mcp_resource>
    <server_name>server name here</server_name>
    <uri>resource URI here</uri>
    </access_mcp_resource>
    """
    return {}