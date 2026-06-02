import pandas as pd
import matplotlib.pyplot as plt
import uuid
import os


def generate_chart(results):

    df = pd.DataFrame(results)

    if len(df.columns) < 2:
        return {
            "error": "Need at least 2 columns"
        }

    x = df.columns[0]
    y = df.columns[1]

    os.makedirs("charts", exist_ok=True)

    chart_name = f"chart_{uuid.uuid4().hex}.png"

    chart_path = f"charts/{chart_name}"

    plt.figure(figsize=(8,5))
    plt.bar(df[x], df[y])

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return {
        "chart_path": chart_path
    }