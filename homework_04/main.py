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

# from loguru import logger
from sqlalchemy import select
from sqlalchemy.engine import Result

from sqlalchemy.ext.asyncio import AsyncSession

from models import async_engine, async_session, Base, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_tables():
    async with async_engine.begin() as conn:
        # print("todo: drop all")
        await conn.run_sync(Base.metadata.drop_all)
        # print("todo: create all")
        await conn.run_sync(Base.metadata.create_all)


async def fetch_all_data() -> (list[dict], list[dict]):
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(), fetch_posts_data()
    )
    # print("type users_data: ", type(users_data))
    # print("len users_data: ", len(users_data))
    # print("type posts_data: ", type(posts_data))
    # print("len posts_data: ", len(posts_data))
    return users_data, posts_data


async def data_upload(session: AsyncSession):
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
    statement = select(Post).join(Post.user).where(User.id == user_id)
    result: Result = await session.execute(statement)

    posts: list[Post] | None = result.scalars().all()

    print("found posts by user ID: ", user_id, posts)

    return posts


async def get_user_by_post(session: AsyncSession, post_title: str) -> User:
    statement = select(User).join(User.posts).where(Post.title == post_title)
    result: Result = await session.execute(statement)

    user: User | None = result.scalar_one_or_none()
    if user:
        print(f"found user {user.username} by post title {post_title!r}")
    else:
        print("user not found!")
    return user


async def async_main():
    # logger.info("Starting main")
    await create_tables()

    async with async_session() as session:
        await data_upload(session)
        await get_posts_by_user_id(session, 10)
        await get_user_by_post(session, "qui expl")
        await get_user_by_post(session, "magnam ut rerum iure")
    # logger.info("Finish main")


# def main():
#     pass


if __name__ == "__main__":
    asyncio.run(async_main())
