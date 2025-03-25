from prisma.models import Character


Character.create_partial(
    "CharacterCreation",
    exclude=[
        "id",
        "level",
        "experience",
        "proficiencyBonus",
        "createdAt",
        "updatedAt",
    ],
)
