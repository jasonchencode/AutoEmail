import os
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url = "https://groq.com/openai/v1"
)

def identify_sponsorship_angle(company, research):
    prompt = f"""
    You are helping QHacks identify the strongest sponsorship outreach angle for a company.
    
    Company: {company}
    Research: {research}
    
    Your task is to identify ONE strongest sponsorship angle.
    Evaluate potential angles based on:
    1. Relevance to QHacks and university students
    2. Relevance to the company's current priorities
    3. Specificity
    4. Timeliness
    5. Sponsorship potential
    6. Whether the connection feels natural rather than forced
    
    NOTE: Do not invent facts. Only use information supported by hte provided research.

    Return: 
    - angle
    - reasoning
    - evidence
    - qhacks_connection
    - confidence

    Return the results as JSON.
    """
    
    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b"
    )

    return response

def generate_email(company, research, angle, examples):
    pass
