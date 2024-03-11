import asyncio

from sqlalchemy import select

from models import  create_tables
from jsonplaceholder_requests import get_users, get_posts, USERS_DATA_URL, POSTS_DATA_URL
from models import Session, Base, User

session = Session()

async def put_into_db(res):
    for data in res:
        session.add_all(data)
    await session.commit()


async def async_main():
    await create_tables()
    res = await asyncio.gather(
        get_users(USERS_DATA_URL),
        get_posts(POSTS_DATA_URL)
        )
    await put_into_db(res=res)

    user = await session.execute(select(User.name, User.username).where(User.id < 10))
    print(user.all())
    await session.close()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()

