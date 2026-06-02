# def generate_suggestions(analysis):
#
#     numeric_columns = analysis.get(
#         "numeric_columns",
#         []
#     )
# 
#     categorical_columns = analysis.get(
#         "categorical_columns",
#         []
#     )
#
#     suggestions = []
#
#     if categorical_columns and numeric_columns:
#
#         suggestions.append(
#             f"Show total {numeric_columns[0]} by {categorical_columns[0]}"
#         )
#
#         suggestions.append(
#             f"Which {categorical_columns[0]} has the highest {numeric_columns[0]}?"
#         )
#
#     if len(numeric_columns) > 1:
#
#         suggestions.append(
#             f"Compare {numeric_columns[0]} and {numeric_columns[1]}"
#         )
#
#     suggestions.append(
#         "Show top 5 records"
#     )
#
#     return suggestions