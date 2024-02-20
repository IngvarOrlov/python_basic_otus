import asyncio
from aiohttp import ClientSession
from models import User, Post

USERS_DATA_URL = "https://my-json-server.typicode.com/IngvarOrlov/python_basic_otus/db"
POSTS_DATA_URL = "https://my-json-server.typicode.com/IngvarOrlov/python_basic_otus/db"
# POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/users"

# @dataclass
# class User:
#     id: int
#     name: str
#     username: str
#     email: str


async def fetch_api(url) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data

async def get_users(url) -> list[User]:
    data = await fetch_api(url)
    users_json = data['users']
    # print(users_json)
    users =[]
    for user in users_json:
        users.append(User(id = user['id'],
                          name=user['name'],
                          username=user['username'],
                          email=user['email']))
    return users


async def get_posts(url) -> list[User]:
    data = await fetch_api(url)
    posts_json = data['posts']
    posts =[]
    for post in posts_json:
        posts.append(Post(user_id=post['user_id'],
                          title=post['title'],
                          body=post['body']))
    return posts

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
- доработайте модуль `jsonplaceholder_requests`:
    - установите значения в константы `USERS_DATA_URL` и `POSTS_DATA_URL` (ресурсы нужно взять отсюда https://jsonplaceholder.typicode.com/)
    - создайте асинхронные функции для выполнения запросов к данным ресурсам (используйте `aiohttp`)
        - рекомендуется добавить базовые функции для запросов, которые будут переиспользованы (например `fetch_json`)
"""


