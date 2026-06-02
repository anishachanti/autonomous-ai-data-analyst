def build_prompt(user_question, analysis):

    prompt = f"""
    
    You are analyzing a dataset.
    
    Dataset Shape:
    Rows: {analysis['shape']['rows']}
    Columns: {analysis['shape']['columns']}
    
    Column Types:
    {analysis['dtypes']}
    
    Missing Values:
    {analysis['missing_values']}
    
    Numeric Columns:
    {analysis['numeric_columns']}
    
    Categorical Columns:
    {analysis['categorical_columns']}
    
    User Question:
    {user_question}
    
    Provide detailed business insights.
    """

    return prompt