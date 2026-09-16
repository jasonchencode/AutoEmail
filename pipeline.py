from search_exa import research_efficient
from qdrant_service import retrieve_email_examples
from llm_service import identify_sponsorship_angle, generate_email

def run_pipeline(data):
    company = data["companyName"]
    contact_name = data["referContact"] # refer to them as

    # 1. Exa Research
    research = research_efficient(company)

    print(len(research))

    # 2. Identify Sponsorship Angle
    angle = identify_sponsorship_angle(company, research)

    # 3. Qdrant RAG
    examples = retrieve_email_examples(angle, limit=5) # fix parameters

    # 4. Generate Email
    email = generate_email(company, contact_name, angle, examples) # fix parameters as needed

    return {
        "company": company, 
        "angle": angle, 
        "email": email
    }

