import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def forecast_next_days(
        filename,
        date_column,
        value_column,
        future_days=30
):

    file_path = f"uploads/{filename}"

    if filename.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    df[date_column] = pd.to_datetime(df[date_column])

    df = df.sort_values(date_column)

    df["day_index"] = range(len(df))

    x = df[["day_index"]]
    y = df[value_column]

    model = LinearRegression()
    model.fit(x, y)

    future_indexes = np.arange(
        len(df),
        len(df) + future_days
    ).reshape(-1, 1)

    predictions = model.predict(
        future_indexes
    )

    future_dates = pd.date_range(
        start=df[date_column].max(),
        periods=future_days + 1
    )[1:]

    result = []

    for date, prediction in zip(
            future_dates,
            predictions
    ):

        result.append({
            "date": str(date.date()),
            "predicted_value": float(prediction)
        })

    return result
