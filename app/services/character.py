# TODO: no se si lo voy a ausar per aca podria usarse la logica
from app.crud.character import CharacterRepository
from app.schemas.character import Character


class CharacterService(CharacterRepository):
    def __init__(self):
        self.repo = CharacterRepository()

    def getAll(self):
        return self.repo.getAllCharacters()

    def getById(self, id):
        return self.repo.getCharacter(id)

    def save(self, item):
        return self.repo.createCharacter(character=item)

    def delete(self, item):
        return self.repo.deleteCharacter(character=item)
