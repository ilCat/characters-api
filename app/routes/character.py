from fastapi import APIRouter, HTTPException, status
from app.schemas.character import Character, ReadAllCharacters
from .dummyData import data
from app.services.character import CharacterService

router = APIRouter()

service = CharacterService()


@router.get(
    "/character/getAll", tags=["character"]  ##, response_model=list[ReadAllCharacters]
)
def read_all_characters():  ##-> list[ReadAllCharacters]:
    return service.getAll()


@router.get("/character/get/{id}", tags=["character"])  ##, response_model=Character)
def read_character_by_id(id: int):
    return service.getById(id)


@router.post(
    "/character/add",
    tags=["character"],
)  # response_model=Character)
def save_character(req: Character):
    exist = read_character_by_id(req.id)
    print(exist)
    if exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id already exists"
        )

    return service.save(req)


@router.delete(
    "/character/delete/{id}", tags=["character"], status_code=status.HTTP_200_OK
)
def delete_character(id: int):
    character = read_character_by_id(id)
    if not character:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Id do not exists, delete cancelled",
        )
    return service.delete(character)
