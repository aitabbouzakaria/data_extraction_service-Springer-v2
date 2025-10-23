from fastapi import APIRouter

router = APIRouter(prefix="/scan", tags=["scan"]) 

@router.post("/")
async def start_scan(target: str):
    """Start a scan for the given target (placeholder).

    Request JSON: {"target": "example.com"}
    """
    # Placeholder implementation
    return {"status": "started", "target": target}
