import asyncio
from pathlib import Path
from prisma import Prisma
from prisma.models import CharacterClass
import json


async def run():
    db = Prisma(auto_register=True)
    await db.connect()

    barbarian_json = Path("data/classes/barbarian/barbarian.json").resolve()
    barbarian_data = json.loads(barbarian_json.read_text())

    from pprint import pprint
    pprint(barbarian_data)
    barbarian_db = await db.characterclass.create(
        data=barbarian_data,
    )
    print(f"Created {barbarian_db}")
    await db.disconnect()


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
