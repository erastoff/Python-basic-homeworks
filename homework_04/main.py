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
import asyncio

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import async_engine, async_session, Base, User, Post
from jsonplaceholder_requests import (
    USERS_DATA_URL,
    POSTS_DATA_URL,
    fetch_users_data,
    fetch_posts_data,
)


async def create_tables():
    """
    Function to delete/create all tables in DB (tables which corresponds the metadata of base class).
    """
    async with async_engine.begin() as conn:
        # print("todo: drop all")
        await conn.run_sync(Base.metadata.drop_all)
        # print("todo: create all")
        await conn.run_sync(Base.metadata.create_all)


async def fetch_all_data(
    users_url: str = USERS_DATA_URL,
    posts_url: str = POSTS_DATA_URL,
) -> (list[dict], list[dict]):
    """
    Function to get all data from sources.
    """
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(users_url), fetch_posts_data(posts_url)
    )
    return users_data, posts_data


async def data_upload(session: AsyncSession):
    """
    Function to upload data into database.
    """
    users_data, posts_data = await fetch_all_data()

    users = [
        User(name=item["name"], username=item["username"], email=item["email"])
        for item in users_data
    ]
    session.add_all(users)

    posts = [
        Post(title=item["title"], body=item["body"], user_id=item["userId"])
        for item in posts_data
    ]
    session.add_all(posts)

    await session.commit()


async def get_posts_by_user_id(session: AsyncSession, user_id: int) -> list[Post]:
    """
    Checking the Post.user relationship.
    """
    statement = select(Post).join(Post.user).where(User.id == user_id)
    result: Result = await session.execute(statement)

    posts: list[Post] | None = result.scalars().all()

    print("found posts by user ID: ", user_id, posts)

    return posts


async def get_user_by_post(session: AsyncSession, post_title: str) -> User:
    """
    Checking the User.posts relationship.
    """
    statement = select(User).join(User.posts).where(Post.title == post_title)
    result: Result = await session.execute(statement)

    user: User | None = result.scalar_one_or_none()
    if user:
        print(f"found user {user.username} by post title {post_title!r}")
    else:
        print("user not found!")
    return user


async def async_main():
    await create_tables()

    async with async_session() as session:
        await data_upload(session)
        await get_posts_by_user_id(session, 10)
        await get_user_by_post(session, "qui expl")
        await get_user_by_post(session, "magnam ut rerum iure")


if __name__ == "__main__":
    asyncio.run(async_main())
