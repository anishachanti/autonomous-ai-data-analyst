import pandas as pd
from fastapi import HTTPException

from services.duckdb_service import (
   load_dataset,
   run_query
)

from utils.sql_prompt_builder import (
   build_sql_prompt
)

from services.llm_service import ask_ai

from utils.sql_cleaner import clean_sql
from utils.sql_validator import validate_sql


def execute_nl_query(
        filename,
        question
):
    table_name = "dataset_table"

    file_path = f"uploads/{filename}"

    # Load dataset into DuckDB
    load_dataset(file_path, table_name)

    # Read dataframe
    if filename.endswith(".csv"):

        df = pd.read_csv(file_path)

    elif filename.endswith(".xlsx"):

        df = pd.read_excel(file_path)

    else:

        raise HTTPException(
            status_code=400,
            detail="Unsupported file"
        )

    columns = list(df.columns)

    # Build SQL prompt
    prompt = build_sql_prompt(
        question,
        columns,
        table_name
    )

    # Generate SQL using Groq
    sql_query = ask_ai(prompt)

    # Clean SQL response
    sql_query = clean_sql(sql_query)

    print("\nGenerated SQL:")
    print(sql_query)

    validate_sql(sql_query)

    # Execute SQL
    results = run_query(sql_query)

    return {
        "generated_sql": sql_query,
        "results": results
    }






