import os
from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()

exa = Exa(os.getenv("EXA_API_KEY"))

result = exa.search(
    "blog post about artificial intelligence",
    num_results = 5,
    type = "auto",
    contents = {
        "highlights": True
    }
)

print(result)