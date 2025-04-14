from fastapi import APIRouter

from prisma.models import CharacterClass

router = APIRouter(
    prefix="/classes",
    tags=["items"],
    responses={404: {"description": "Page Not found"}},
)


async def get_classes() -> list[CharacterClass]:
    return await CharacterClass.prisma().find_many()


@router.get("/", response_model=list[CharacterClass])
async def read_classes() -> list[CharacterClass]:
    """Get all classes from DB"""
    classes = await get_classes()
    return classes


@router.get("/{class_id}", response_model=CharacterClass)
async def get_class(class_id: int) -> CharacterClass:
    return await CharacterClass.prisma().find_first(where={"id": class_id})
