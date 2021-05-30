"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

#import aiohttp
import asyncio
from aiohttp import ClientSession
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def async_fetch_json(url):
    async with ClientSession() as session:
        result = await fetch_json(session, url)
        return result


async def async_main():
#    await async_fetch_users(USERS_DATA_URL)
#    await async_fetch_posts(POSTS_DATA_URL)
    async with ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            results_users = await response.json()
        async with session.get(POSTS_DATA_URL) as response:
            results_posts = await response.json()

    return results_users, results_posts


def main():
    ru, rp = asyncio.run(async_main())
    logger.info("USERS: {}", ru)
    logger.info("POSTS: {}", rp)

if __name__ == "__main__":
    main()
