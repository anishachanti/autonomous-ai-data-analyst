
import pandas as pd
from fastapi import HTTPException


def analyze_dataset_logic(filename):

        file_path = f"uploads/{filename}"

        if filename.endswith(".csv"):
            df = pd.read_csv(file_path)

        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file format"
            )

        analysis = {
            "shape": {
                "rows": df.shape[0],
                "columns": df.shape[1]
            },

            "columns": list(df.columns),

            "dtypes": {
                column: str(dtype)
                for column, dtype in df.dtypes.items()
            },

            "missing_values": {
                column: int(df[column].isnull().sum())
                for column in df.columns
            },

            "numeric_columns": list(
                df.select_dtypes(include='number').columns
            ),

            "categorical_columns": list(
                df.select_dtypes(include='object').columns
            )

        }

        return analysis