import asyncio

from models import  create_tables
from jsonplaceholder_requests import get_users, get_posts, USERS_DATA_URL, POSTS_DATA_URL
from models import session, Base


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


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()


"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


