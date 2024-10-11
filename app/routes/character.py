from fastapi import APIRouter, HTTPException, status
from schemas import Character, ReadAllCharacters
from dummyData import data

router = APIRouter()


@router.get(
    "/character/getAll", tags=["character"], response_model=list[ReadAllCharacters]
)
async def read_all_characters() -> list[ReadAllCharacters]:
    return data


@router.get("/character/get/{id} ", tags=["character"], response_model=Character)
async def read_character_by_id(id: int) -> any:
    return filter(lambda x: x["id"] == id, data)


@router.post("/character/add", tags=["character"], response_model=Character)
async def save_character(req: Character):
    exist = await read_character_by_id(req.id)
    if exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id already exists"
        )
    return req


@router.delete(
    "/character/delete/{id}", tags=["character"], status_code=status.HTTP_200_OK
)
async def delete_character(id: int):
    exist = await read_character_by_id(id)
    if not exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Id do not exists, delete cancelled",
        )
