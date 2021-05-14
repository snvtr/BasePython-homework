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

async def create_users():
    session = Session()

    admin = User(username="admin", email="admin@admin")
    guest = User(username="guest", email="guest@guest")

    session.add(admin)
    session.add(guest)
    session.commit()
    session.close()

async def create_one_user(one_user):
    session = Session()
    session.add(one_user)
    session.commit()
    session.close()

async def async_create_users():

    admin = User(username="admin", email="admin@admin")
    guest = User(username="guest", email="guest@guest")

    await asyncio.gather(
        create_one_user(admin),
        create_one_user(guest),
    )

async def create_posts():
    session = Session()

    admin: User = session.query(User).filter_by(username="admin").one()

    post_one = Post(title="Post One", body="Message One", created_by=admin.id)
    post_two = Post(title="Post Two", body="Message Two", created_by=admin.id)

    session.add(post_one)
    session.add(post_two)
    session.commit()
    session.close()


async def create_one_post(one_post):
    session = Session()
    session.add(one_post)
    session.commit()
    session.close()

async def async_create_posts():

    session = Session()
    admin: User = session.query(User).filter_by(username="admin").one()
    session.close()

    post_one = Post(title="Post One", body="Message One", created_by=admin.id)
    post_two = Post(title="Post Two", body="Message Two", created_by=admin.id)

    await asyncio.gather(
        create_one_post(post_one),
        create_one_post(post_two),
    )


async def async_main():
    #await asyncio.gather(
    #    create_users(),
    #    create_posts()
    #    )
    await async_create_users()
    await async_create_posts()


def init_schema():
    Base.metadata.create_all()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    init_schema()
    main()
