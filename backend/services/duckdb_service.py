import duckdb
import pandas as pd
import numpy as np

connection = duckdb.connect()


def load_dataset(file_path, table_name):

    try:

        if file_path.endswith(".csv"):

            df = pd.read_csv(file_path)

        elif file_path.endswith(".xlsx"):

            df = pd.read_excel(file_path)

        else:
            raise Exception("Unsupported file format")


        connection.register(table_name, df)

        return True

    except Exception as e:

        raise Exception(str(e))


def run_query(query):

    try:

        result = connection.execute(query).fetchdf()

        result = result.replace(
            [np.nan, np.inf, -np.inf],
            None
        )

        return result.to_dict(orient="records")

    except Exception as e:

        raise Exception(str(e))