from scraper import scrape_linkedin_page
from store import pages_collection

def get_page(page_id: str):

    page = pages_collection.find_one({"page_id": page_id})
    if page:
        page.pop("_id", None) 
        return page

    data = scrape_linkedin_page(page_id)
    pages_collection.insert_one(data)
    return data
