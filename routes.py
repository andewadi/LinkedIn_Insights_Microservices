from fastapi import APIRouter
from services import get_page  

router = APIRouter() 

@router.get("/page/{page_id}")
def fetch_page(page_id: str):
    """
    Get LinkedIn page details by Page ID.
    """
    return get_page(page_id)
