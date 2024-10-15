from fastapi import APIRouter, HTTPException, status
from app.schemas.character import Character, ReadAllCharacters
from app.services.character import CharacterService

router = APIRouter()

service = CharacterService()


@router.get(
    "/character/getAll", tags=["character"], response_model=list[ReadAllCharacters]
)
def read_all_characters() -> list[ReadAllCharacters]:
    # Endpoint to get all characters
    return service.getAll()


@router.get("/character/get/{id}", tags=["character"], response_model=Character)
def read_character_by_id(id: int) -> Character:
    # Endpoint to get a character by its ID
    result = service.getById(id)
    if not result:
        # If the ID already exists, raise an HTTP 400 exception
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Id {id} do not exists"
        )
    # Save the new character
    return result


@router.post("/character/add", tags=["character"], response_model=Character)
def save_character(req: Character) -> Character:
    # Endpoint to add a new character
    exist = service.getById(req.id)
    if exist:
        # If the ID already exists, raise an HTTP 400 exception
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id already exists"
        )
    # Save the new character
    return service.save(req)


@router.delete(
    "/character/delete/{id}", tags=["character"], status_code=status.HTTP_200_OK
)
def delete_character(id: int):
    # Endpoint to delete a character by its ID
    character = service.getById(id)
    if not character:
        # If the character does not exist, raise an HTTP 400 exception
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Id {id} do not exists, delete operation cancelled",
        )
    # Delete the existing character
    return service.delete(character)
