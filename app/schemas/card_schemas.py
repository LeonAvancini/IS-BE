from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class ActionType(Enum):
    modal = "Modal"
    redirect = "Redirect"
    image = "Image"
    other = "Other"


class ActionContent(BaseModel):
    external_url: Optional[str] = ""
    img_url: Optional[str] = ""


class Action(BaseModel):
    id: int
    value: str
    type: ActionType
    # content: ActionContent TODO: Add this property instead have all on this object
    external_url: Optional[str]
    img_url: Optional[str]


class Card(BaseModel):
    id: int
    title: str
    description: Optional[str]
    actions: List[Action]


class Cards(BaseModel):
    cards: List[Card]
