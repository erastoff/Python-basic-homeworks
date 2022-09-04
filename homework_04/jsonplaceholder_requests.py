"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:  # type aiohttp.ClientResponse
        data = await response.json()
        # print(type(data))
        # print(type(data[0]))
        return data


async def fetch_users_data(service: str = USERS_DATA_URL) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        users: list[dict] = await fetch_json(session, service)
        return users


async def fetch_posts_data(service: str = POSTS_DATA_URL) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        posts: list[dict] = await fetch_json(session, service)
        return posts
