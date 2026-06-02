from mcp.server.fastmcp import FastMCP
from services.chart_service import generate_chart
from services.query_service import execute_nl_query
from services.forecast_service import forecast_next_days


mcp = FastMCP("Data Analyst MCP")

@mcp.tool()
def health_check():

    return "MCP server working"

@mcp.tool()
def query_dataset( filename: str,question: str):
    return execute_nl_query(filename,question)


@mcp.tool()
def create_chart(results: list):
    return generate_chart(results)

@mcp.tool()
def forecast_dataset(filename: str,date_column: str,value_column: str,future_days: int = 30):
    return forecast_next_days(filename,date_column,value_column,future_days)




if __name__ == "__main__":
    print("Starting MCP Server...")
    print("Registered Tools:")
    print("- health_check")
    print("- query_dataset")
    print("- forecast_dataset")
    print("- create_chart")

    mcp.run()