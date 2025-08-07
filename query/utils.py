import os
from pathlib import Path
import re
from django.db.utils import settings
from google import genai
from google.genai import types
from google.genai.types import Part
from openai import OpenAI

PROMPT_PATH = Path(__file__).resolve().parent / "prompt.txt"

def generate_prompt(user, product, dossier):
    prompt_template = PROMPT_PATH.read_text(encoding='utf-8')
    return prompt_template.format(user=user, product=product, dossier=dossier)

def query(user, product, dossier):
    '''
    prompt = generate_prompt(user, product, dossier)
    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text
    '''
    prompt = generate_prompt(user, product, dossier)
    client = OpenAI(api_key=settings.API_KEY)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            }
        ]
        },
    ],
        max_tokens=300,
    )
    return response.choices[0].message.content

