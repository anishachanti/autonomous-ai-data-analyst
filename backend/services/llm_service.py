from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(prompt, system_prompt=None):


    if not system_prompt:
        system_prompt = (
            "You are a professional AI data analyst."
        )

    response = client.chat.completions.create(

        model = "llama-3.3-70b-versatile",

        messages=[
            {
                "role":"system",
                "content": system_prompt
            },
            {
                "role":"user",
                "content": prompt

            }
        ]

    )

    return response.choices[0].message.content