from fastapi import APIRouter


router = APIRouter(prefix="/health", tags=["health"])


@router.get("/check")
async def health_check() -> bool:
    return True
