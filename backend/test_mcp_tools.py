from backend.services.dataset_service import analyze_dataset_logic
from backend.services.query_service import execute_nl_query

print("\nTesting Dataset Analysis...\n")

result = analyze_dataset_logic(
    "sample_sales_report.csv"
)

print(result)

print("\nTesting Query...\n")

query_result = execute_nl_query(
    "sample_sales_report.csv",
    "Which product has highest revenue?"
)

print(query_result)