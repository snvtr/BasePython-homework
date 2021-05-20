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
from models import Session, Base, User, Post
from jsonplaceholder_requests import *


async def create_one_user(one_user):
    session = Session()
    session.add(one_user)
    session.commit()
    session.close()


async def create_one_post(one_post):
    session = Session()
    session.add(one_post)
    session.commit()
    session.close()


async def async_main():

    ext_users = await async_fetch_users(USERS_DATA_URL)
    ext_posts = await async_fetch_posts(POSTS_DATA_URL)

    try:
        asyncio.gather([await create_one_user(User(username=i["username"], name=i["name"], email=i["email"])) for i in ext_users])
    except:
        print("users(): oops")
    try:
        asyncio.gather([await create_one_post(Post(title=i["title"], body=i["body"], user_id=i["userId"])) for i in ext_posts])
    except:
        print("posts(): oops")


def init_schema():
    Base.metadata.create_all()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    init_schema()
    main()
