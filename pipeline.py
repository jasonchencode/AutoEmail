from search_exa import research_efficient
from qdrant_service import retrieve_email_examples

def run_pipeline(data):
    company = data["companyName"]

    # 1. Exa Research
    research = research_efficient(company)

    print(len(research))

    # 2. Identify Sponsorship Angle
    angle = "" # placeholder

    # 3. Qdrant RAG
    examples = retrieve_email_examples(angle, limit=5)

    # 4. Generate Email
    email = "" # placeholder

    return {
        "company": company, 
        "angle": angle, 
        "email": email
    }

