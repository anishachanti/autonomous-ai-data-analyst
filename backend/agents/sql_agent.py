
from mcp_client.client import call_tool


def run_sql_agent(filename, question):

    question_lower = question.lower()

    if (
        "predict" in question_lower
        or "forecast" in question_lower
    ):

        forecast_results = call_tool(
            "forecast_dataset",
            {
                "filename": filename,
                "date_column": "Date",
                "value_column": "Total Revenue",
                "future_days": 7
            }
        )

        return {
            "forecast": forecast_results
        }


    elif (
            "chart" in question_lower
            or "graph" in question_lower
            or "plot" in question_lower
            or "visualize" in question_lower
    ):

        query_result = call_tool(
            "query_dataset",
            {
                "filename": filename,
                "question": question
            }
        )

        chart = call_tool(
            "create_chart",
            {
                "results": query_result["results"]
            }
        )

        return {
            "results": query_result["results"],
            "chart": chart
        }

    return call_tool(
        "query_dataset",
        {
            "filename": filename,
            "question": question
        }
    )