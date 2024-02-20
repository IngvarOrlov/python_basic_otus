import asyncio

from jsonplaceholder_requests import get_users, get_posts, USERS_DATA_URL, POSTS_DATA_URL


async def get_users_and_put_theme_into_db(url):
    users = await get_users(url)
    for user in users:
        print(user.name)

async def get_posts_and_put_theme_into_db(url):
    posts = await get_posts(url)
    for post in posts:
        print(post.title)


async def async_main():
    await get_users_and_put_theme_into_db(USERS_DATA_URL)
    await get_posts_and_put_theme_into_db(POSTS_DATA_URL)



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


