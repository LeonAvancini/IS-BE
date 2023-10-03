from fastapi_sqlalchemy import db
from app.database.models import Card
from typing import List


class DBClient:

    @staticmethod
    def get_cards() -> List[Card]:
        with db():
            cards = db.session.query(Card).all()
            if cards:
                return cards
            raise

    @staticmethod
    def get_card_by_id(id: int) -> List[Card]:
        with db():
            response = db.session.query(Card).get(id)
            if response:
                return response
            raise

        # @staticmethod

    @staticmethod
    def delete_card_by_id(id: int) -> bool:
        with db():
            card = db.session.query(Card).filter_by(id=id).first()
            if card:
                db.session.delete(card)
                db.session.commit()
                return True
            raise

        # def save_person(person: Persons):


#     with db():
#         db.session.add(person)
#         db.session.commit()


db_client = DBClient()
