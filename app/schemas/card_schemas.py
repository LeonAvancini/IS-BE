from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class ActionType(Enum):
    modal = "Modal"
    redirect = "Redirect"
    image = "Image"
    other = "Other"


#
# class ActionContent(BaseModel):
#     external_url: Optional[str] = ""
#     img_url: Optional[str] = ""


class ActionCreate(BaseModel):
    value: str
    type: ActionType
    external_url: Optional[str] = ""
    img_url: Optional[str] = ""
    # content: ActionContent  # Add a content property for the ActionContent


class ActionBase(BaseModel):
    value: str
    type: ActionType
    external_url: Optional[str] = ""
    img_url: Optional[str] = ""


# content: ActionContent  # Add the content property here


class Action(ActionBase):
    id: int


class CardBase(BaseModel):
    title: str
    description: Optional[str]


class CardCreate(CardBase):
    actions: List[ActionCreate]  # Use ActionCreate for creating actions


class Card(CardBase):
    id: int
    actions: List[Action]  # Use Action for existing actions


class Cards(BaseModel):
    cards: List[Card]
