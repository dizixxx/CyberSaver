from application.database.models import async_session
from application.database.models import User, TextTask, SberTopic, GosuslugiTopic, Base
from sqlalchemy import select
from collections import namedtuple

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_users():
    async with async_session() as session:
        return await session.scalars(select(User))

async def get_text_tasks():
    async with async_session() as session:
        return await session.scalars(select(TextTask))

async def get_sber_topic_tasks():
    async with async_session() as session:
        return await session.scalars(select(SberTopic))

async def get_gosuslugi_topic_tasks():
    async with async_session() as session:
        return await session.scalars(select(GosuslugiTopic))

async def get_task_by_id(task_id: int, table: type[Base]):
    async with async_session() as session:
        return await session.scalar(select(table).where(table.task_id == task_id))

async def get_answer_options(task_id: int, table):
    async with async_session() as session:
        query = select(table).where(table.task_id == task_id)
        task = await session.scalar(query)

        if not task or not task.task_options:
            return []
        options = task.task_options.split('&')
        return [opt.strip() for opt in options if opt.strip()]

# async def get_task_pic_by_id(task_id: int):
#     async with async_session() as session:
#         return await session.scalar(select(TaskPic).where(TaskPic.task_id == task_id))
