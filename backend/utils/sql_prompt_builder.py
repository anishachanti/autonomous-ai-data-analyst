def build_sql_prompt(question, columns, table_name):

    prompt = f"""

    You are an expert DuckDB SQL analyst.

    Table Name:
    {table_name}

    Available Columns:
    {columns}

    IMPORTANT RULES:
    - Generate ONLY SQL query
    - Do NOT explain anything
    - Do NOT use markdown
    - Use DuckDB SQL syntax
    - NEVER use backticks
    - Use double quotes for columns with spaces
    - Use LIMIT instead of TOP
    - Use only available columns
    - When using aggregate functions like SUM, MAX, MIN, AVG:
      all non-aggregated columns MUST appear in GROUP BY
    - Use LOWER() for case-insensitive text matching

    User Question:
    {question}

    """

    return prompt