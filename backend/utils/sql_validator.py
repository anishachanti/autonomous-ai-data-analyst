def validate_sql(sql_query):

    forbidden_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    sql_upper = sql_query.upper()

    for keyword in forbidden_keywords:

        if keyword in sql_upper:

            raise Exception(
                f"Forbidden SQL operation detected: {keyword}"
            )

    return True