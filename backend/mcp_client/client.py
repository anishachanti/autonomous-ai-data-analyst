import asyncio
import json
import sys

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)

from mcp import ClientSession


async def execute_tool(tool_name, params):

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "mcp_server.server"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                params
            )

            print("\nRAW MCP RESULT:")
            print(result)

            print("\nCONTENT:")
            for item in result.content:
                print(item)

            if result.content:

                parsed_results = []

                for item in result.content:

                    if hasattr(item, "text"):

                        try:
                            parsed_results.append(
                                json.loads(item.text)
                            )

                        except json.decoder.JSONDecodeError:

                            parsed_results.append(
                                {"result": item.text}
                            )

                if len(parsed_results) == 1:
                    return parsed_results[0]

                return parsed_results

            return {}




def call_tool(tool_name, params):

    print(f"\nCalling MCP Tool: {tool_name}")

    return asyncio.run(
        execute_tool(tool_name, params)
    )