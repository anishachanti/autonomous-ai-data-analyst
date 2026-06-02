import re

def clean_sql(sql_query):

    # Remove markdown
    sql_query = (
        sql_query
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    # Convert MySQL backticks to DuckDB double quotes
    sql_query = re.sub(
        r'`([^`]*)`',
        r'"\1"',
        sql_query
    )

    return sql_query