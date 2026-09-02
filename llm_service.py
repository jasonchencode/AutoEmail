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

def generate_email(company, contact_name, research, angle, examples):
    pass
    prompt = f"""
    You are writing a sponsorship outreach email on behalf of QHacks, Queen's University's student-run hackathon.

    Your job is to write a concise, personalized sponsorship email.

    Company: {company}
    Contact: {contact_name}
    Company Research: {research}
    Identified Sponsorship Angle: {angle}
    Past Email Examples: {examples}

    INSTRUCTIONS:
    1. Use the identified sponsorship angle as the central reason for reaching out.
    2. Personalize the email specifically to {company}.
    3. Only make claims that are supported by the provided research. Do not invent company initiatives, partnerships, products, or facts.
    4. Use the past emails as examples of tone, structure, and writing style. Do not copy their wording.
    5. Keep the email concise and natural.
    6. The email should sound like it was written by a university student reaching out personally, not like an automated marketing campaign.
    7. Clearly explain why a partnership with QHacks could be valuable to the company.
    8. End with a simple call to action, such as asking whether they would be open to a quick conversation 
    9. Do not overuse buzzwords or generic statements about innovation, community, or technology.
    10. Do not mention that AI, Exa, Qdrant, or any automated system was used to create the email.

    OUTPUT:
    Return only the email body. Do not include a subject line.
    """
