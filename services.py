from scraper import scrape_linkedin_page
from store import pages_collection

def get_page(page_id: str):
    # Try fetching page from MongoDB
    page = pages_collection.find_one({"page_id": page_id})
    if page:
        page.pop("_id", None)  # Remove MongoDB _id before returning
        return page

    # If not in DB, scrape LinkedIn
    data = scrape_linkedin_page(page_id)
    pages_collection.insert_one(data)
    return data
