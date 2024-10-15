# TODO: Aca iria todas las operaciones directas sobre la DB
from fastapi import Depends
from typing import Annotated
from app.models.character import CharacterModel
from app.schemas.character import Character
from app.db.db import get_db, engine
from sqlalchemy.orm import Session


class CharacterRepository:
    def __init__(self):
        self.db = Session(engine)  ##Annotated[Session, Depends(get_db)]

    def getCharacter(self, Id: int):
        result = self.db.query(CharacterModel).filter_by(id=Id).first()
        return result

    def getAllCharacters(self):
        result = self.db.query(CharacterModel).all()
        return result

    def createCharacter(self, character: Character):
        new_character = CharacterModel(
            id=character.id,
            name=character.name,
            height=character.height,
            mass=character.mass,
            hair_color=character.hair_color,
            skin_color=character.skin_color,
            eye_color=character.eye_color,
            birth_year=character.birth_year,
        )
        self.db.add(new_character)
        self.db.commit()
        return character

    def deleteCharacter(self, character: Character):
        self.db.delete(character)
        self.db.commit()
        return f"Id {character.id} was deleted"
