from app.database.client import db_client
from app.schemas.card_schemas import Cards, Card, Action, ActionType


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
