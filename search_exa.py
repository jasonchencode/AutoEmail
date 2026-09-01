import os
from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()

exa = Exa(os.getenv("EXA_API_KEY"))

def research_efficient(company):
    all_research = {}
    queries = {
        "recent": f"""
            What is the most recent notable development at {company} that would make a good personalized opening for a sponsorship outreach email?
        """,
        "technical_fit": f"""
            What products, technologies, developer tools, APIs, platforms, or research from {company} would be genuinely interesting for university students to build with at a technical hackathon?
        """,
        "hackathon": f"""
            Has {company} previously sponsored, partnered with, mentored, judged, or provided prizes or technology for university hackathons or student developer events?
        """,
        "student": f"""
            How does {company} engage with university students or early-career technical talent through internships, university recruiting, student programs, mentorship, or educational initiatives?
        """
    }

    # 1 search per category/query
    for category, query in queries.items():
        results = exa.search(
            query=query,
            num_results=3,
            type="auto",
            contents = {
               "highlights": {
                   "max_characters": 500
                }
            }
        )

        all_research[category] = [
            {
                "title": r.title,
                "url": r.url,
                "highlight": r.highlights[0] if r.highlights else "" # in case there are no valid highlights
            }
            for r in results.results
        ]

    return all_research
research_efficient("Ada CX")

# category: "company",
# results for queries: 5, 5, 3, 3
