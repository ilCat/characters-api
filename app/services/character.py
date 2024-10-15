from app.crud.character import CharacterRepository
from app.schemas.character import Character, ReadAllCharacters


class CharacterService(CharacterRepository):
    """
    Class Sevices based  on repository
    It is necessary to handle the business logic and operate over the data that comes from the DB
    """

    def __init__(self):
        self.__repo = CharacterRepository()

    def getAll(self):
        return map(
            CharacterMapper.ReadAllCharactersMapper, self.__repo.getAllCharacters()
        )

    def getById(self, id):
        return self.__repo.getCharacter(id)

    def save(self, item):
        return self.__repo.createCharacter(character=item)

    def delete(self, item):
        return self.__repo.deleteCharacter(character=item)


class CharacterMapper:
    def ReadAllCharactersMapper(character: Character):
        return ReadAllCharacters(
            id=character.id,
            name=character.name,
            height=character.height,
            mass=character.mass,
            eye_color=character.eye_color,
            birth_year=character.birth_year,
        )
