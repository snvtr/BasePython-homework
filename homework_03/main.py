"""
Домашнее задание №3
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

import asyncio
from models import Session, Base, User, Post, engine
from jsonplaceholder_requests import *


async def create_one(one):
    async with Session() as session:
        async with session.begin():
            session.add(one)
        await session.commit()


async def async_init_schema():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_main():

    await async_init_schema()

    ext_users = await async_fetch_json(USERS_DATA_URL)
    ext_posts = await async_fetch_json(POSTS_DATA_URL)

    #asyncio.gather([await create_one(User(username=i["username"], name=i["name"], email=i["email"])) for i in ext_users])
    #asyncio.gather([await create_one(Post(title=i["title"], body=i["body"], user_id=i["userId"])) for i in ext_posts])

    for i in ext_users:
        await create_one(User(username=i["username"], name=i["name"], email=i["email"]))

    for i in ext_posts:
        await create_one(Post(title=i["title"], body=i["body"], user_id=i["userId"]))

    print("done")

def main():
    #asyncio.run(async_main())
    asyncio.get_event_loop().run_until_complete(async_main())

if __name__ == "__main__":
    main()
