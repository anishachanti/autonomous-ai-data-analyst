from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from services.llm_service import ask_ai

from services.dataset_service import (
    analyze_dataset_logic
)
from utils.prompt_builder import build_prompt
from services.query_service import (
    execute_nl_query
)
from services.forecast_service import (
    forecast_next_days
)

from agents.analyst_agent import run_sql_agent
import shutil
import os
import pandas as pd

app = FastAPI()

app.mount(
    "/charts",
    StaticFiles(directory="charts"),
    name="charts"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message" : "Backend Running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{
        "success": True,
        "filename": file.filename,
    }

@app.get("/preview/{filename}")
def preview_data(filename: str):

    file_path = f"uploads/{filename}"

    df = pd.read_csv(file_path)

    return {
        "columns": list(df.columns),
        "rows": df.head(5).to_dict(orient="records")
    }

@app.get("/analyze/{filename}")
def analyze_dataset(
        filename: str
):

    try:

        return analyze_dataset_logic(
            filename
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.post("/chat/{filename}")
def chat_with_dataset(filename: str, body: dict):

    try:

        user_question = body.get("question")

        file_path = f"uploads/{filename}"

        if filename.endswith(".csv"):
            df = pd.read_csv(file_path)

        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file"
            )

        analysis = {

            "shape": {
                "rows": df.shape[0],
                "columns": df.shape[1]
            },

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

        prompt = build_prompt(
            user_question,
            analysis
        )

        response = ask_ai(prompt)

        return{
            "response": response
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



@app.post("/query/{filename}")
def query_dataset(
        filename: str,
        body: dict
):

    try:

        question = body.get(
            "question"
        )

        return execute_nl_query(
            filename,
            question
        )

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/agent-query/{filename}")
def agent_query(
    filename: str,
    body: dict
):

    question = body.get(
        "question"
    )

    return run_sql_agent(
        filename,
        question
    )




