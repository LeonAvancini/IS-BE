from sqlalchemy import Column, String, Enum, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship
from app.schemas.card_schemas import ActionType

Base = declarative_base()


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, comment="Card title", nullable=False)
    description = Column(String, comment="Card description", nullable=True)

    actions = relationship("Action", backref="card", cascade="all, delete-orphan", lazy="joined")

    class Config:
        orm_mode = True


class Action(Base):
    __tablename__ = "actions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)
    value = Column(String, comment="Action value", nullable=False)
    type = Column(Enum(ActionType), comment="Action type")
    external_url = Column(String, comment="External URL")
    img_url = Column(String, comment="Image URL")
