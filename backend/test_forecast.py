from services.forecast_service import (
    forecast_next_days
)

result = forecast_next_days(
    "sample_sales_report.csv",
    "Date",
    "Total Revenue",
    7
)

print(result)