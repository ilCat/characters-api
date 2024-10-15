from app.models.character import CharacterModel
from app.schemas.character import Character
from app.db.db import engine
from sqlalchemy.orm import Session


class CharacterRepository:
    """
    Class repository with CRUD operations
    """

    def __init__(self):
        self.__db = Session(engine)

    def getCharacter(self, Id: int):
        result = self.__db.query(CharacterModel).filter_by(id=Id).first()
        return result

    def getAllCharacters(self):
        result = self.__db.query(CharacterModel).all()
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
        self.__db.add(new_character)
        self.__db.commit()
        return character

    def deleteCharacter(self, character: Character):
        self.__db.delete(character)
        self.__db.commit()
        return f"Character {character.name} with Id {character.id} was deleted"
