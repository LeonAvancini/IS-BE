from fastapi import APIRouter, Path, HTTPException, Body
from app.schemas.card_schemas import Cards, Card, CardCreate
from app.services.card_service import get_cards, get_card_by_id, delete_card_by_id, create_card
from typing import Annotated

router = APIRouter()


@router.get("/cards", tags=['All cards'], response_model=Cards)
def cards() -> Cards:
    return get_cards()


@router.get("/cards/{id}", tags=['Card by ID'], response_model=Card)
def card(id: int = Path(title="The ID of the card to get")) -> Card:
    try:
        return get_card_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Card with ID value {id} not found")


@router.delete("/cards/{id}", tags=['Delete card by ID'])
def delete(id: int = Path(title="The ID of the card to get")):
    try:
        delete_card_by_id(id)
        return f"Card with ID value {id} was deleted successfully"
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Card with ID value {id} not found")


@router.post("/cards", tags=['Create card'])
def create(card: Annotated[CardCreate, Body(embed=True)]):
    try:
        return create_card(card)
    except Exception as e:
        print('ERROR', e)
        raise HTTPException(status_code=400, detail="A problem occurs creating the Card")
