from fastapi import FastAPI
from contextlib import asynccontextmanager
from prisma.models import Character
from prisma.partials import CharacterCreation
from app.prisma import db
from app.routers import classes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application Lifespan event manager."""
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(classes.router)


@app.get("/", response_model=Character)
async def root() -> list[Character]:
    """Application root path"""

    characters = await db.character.find_many()
    return {"characters": characters}


@app.get("/characters")
async def get_characters() -> list[Character]:
    """Get all characters from DB"""
    characters = await db.character.find_many()
    print(characters)
    return characters


@app.post("/characters/create")
async def create_character(character: CharacterCreation):
    new_character = await db.character.create(data=dict(character))
    return new_character


@app.get("/characters/{character_id}")
async def get_character(character_id: int) -> Character:
    """Get a single character by given Id."""
    character = await db.character.find_first(where={"id": character_id})
    return character
