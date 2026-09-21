from fastapi import APIRouter, Depends, Query

from app.api.deps import get_timestamp
from app.api.schemas import ItemEnvelope, ItemList

router = APIRouter(prefix="/items", tags=["items"])

ITEMS = [
    {"id": 1, "name": "Sample Item 1", "value": 100},
    {"id": 2, "name": "Sample Item 2", "value": 200},
    {"id": 3, "name": "Sample Item 3", "value": 300},
]


@router.get("/", response_model=ItemList, summary="List sample items")
def read_items(
    offset: int = Query(default=0, ge=0, description="Number of items to skip"),
    limit: int = Query(default=20, ge=1, le=100, description="Maximum items to return"),
    timestamp: str = Depends(get_timestamp),
) -> ItemList:
    return ItemList(data=ITEMS[offset : offset + limit], total=len(ITEMS), offset=offset, limit=limit, timestamp=timestamp)


@router.get("/{item_id}", response_model=ItemEnvelope, summary="Get one sample item")
def read_item(item_id: int, timestamp: str = Depends(get_timestamp)) -> ItemEnvelope:
    item = next((candidate for candidate in ITEMS if candidate["id"] == item_id), None)
    if item is None:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Item not found")
    return ItemEnvelope(item=item, timestamp=timestamp)
