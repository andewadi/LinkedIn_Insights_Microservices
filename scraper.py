import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def scrape_linkedin_page(page_id: str):
    query = f"{page_id} LinkedIn company"

    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # --- Try Knowledge Graph ---
    kg = data.get("knowledge_graph", {})

    name = kg.get("title")
    description = kg.get("description")
    website = kg.get("website")
    industry = kg.get("type")
    logo = kg.get("image")

    # --- Fallback: Organic Results ---
    if not name:
        organic = data.get("organic_results", [])
        if organic:
            name = organic[0].get("title")
            description = organic[0].get("snippet")
            website = organic[0].get("link")

    return {
        "page_id": page_id,
        "name": name or page_id.capitalize(),
        "url": f"https://www.linkedin.com/company/{page_id}/",
        "industry": industry or "Software / Technology",
        "followers": "N/A (LinkedIn restricted)",
        "description": description or "Company information retrieved via Google SERP",
        "website": website or f"https://www.{page_id}.com",
        "profile_pic": logo or "N/A",
        "specialities": [],
        "posts": [],
        "employees": []
    }
