from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int


class ReadAllCharacters(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    eye_color: str
    birth_year: int
