from app.database.client import db_client
from app.schemas.card_schemas import Cards, Card, Action, ActionType, CardCreate, ActionCreate
import app.database.models as models


def get_cards() -> Cards:
    def format_action(action: Action):
        return Action(
            id=action.id,
            value=action.value,
            type=ActionType(action.type),
            external_url=action.external_url,
            img_url=action.img_url
        )

    cards = db_client.get_cards()
    response = []
    for card in cards:
        actions = [format_action(action) for action in card.actions]
        response.append(Card(
            id=card.id,
            title=card.title,
            description=card.description,
            actions=actions
        ))

    return Cards(cards=response)


def get_card_by_id(card_id: int) -> Card:
    card = db_client.get_card_by_id(card_id)
    return card


def delete_card_by_id(card_id: int) -> bool:
    response = db_client.delete_card_by_id(card_id)
    return response


def create_card(card: CardCreate):
    # Create a new Card instance
    new_card = models.Card(
        title=card.title,
        description=card.description,
        actions=[]
    )

    # Iterate through the actions in the CardCreate schema and create Action instances
    for action_data in card.actions:
        new_action = models.Action(
            value=action_data.value,
            type=action_data.type,
            external_url=action_data.external_url,
            img_url=action_data.img_url,
            card=new_card  # Associate the action with the new card
        )
        new_card.actions.append(new_action)

    # Add the new card to the database
    db_client.add_card(new_card)
