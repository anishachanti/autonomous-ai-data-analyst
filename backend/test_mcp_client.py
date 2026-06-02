import asyncio

from mcp.client.stdio import stdio_client,StdioServerParameters
from mcp import ClientSession


async def main():
    server_params = StdioServerParameters(
        command=r"E:\Projects\autonomous-ai-data-analyst\.venv\Scripts\python.exe",
        args=["-m","mcp_server.server"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # tools = await session.list_tools()
            #
            # print(tools)

            # result = await session.call_tool(
            #     "health_check",
            #     {}
            # )

            result = await session.call_tool(
                "analyze_dataset",
                {
                    "filename": "sample_sales_report.csv"
                }
            )

            print(result)


asyncio.run(main())

