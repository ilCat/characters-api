# TODO: no se si lo voy a ausar per aca podria usarse la logica
from app.crud.character import CharacterRepository
from app.schemas.character import Character, ReadAllCharacters


class CharacterService(CharacterRepository):
    def __init__(self):
        self.repo = CharacterRepository()

    def getAll(self):
        return map(
            CharacterMapper.ReadAllCharactersMapper, self.repo.getAllCharacters()
        )

    def getById(self, id):
        return self.repo.getCharacter(id)

    def save(self, item):
        return self.repo.createCharacter(character=item)

    def delete(self, item):
        return self.repo.deleteCharacter(character=item)


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
