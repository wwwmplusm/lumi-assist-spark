from fastapi import APIRouter
from .. import schemas
from ..services import ai_service

router = APIRouter(prefix="/api/ai", tags=["AI"])


@router.post("/generate-blocks", response_model=schemas.AIGenerateResponse)
def handle_generate_blocks(request: schemas.AIGenerateRequest):
    blocks = ai_service.generate_blocks_from_text_stub(
        source_text=request.source_text, prompt=request.prompt
    )
    return {"blocks": blocks}
