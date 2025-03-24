from application.database.models import async_session
from application.database.models import User, TaskPic, TaskAud
from sqlalchemy import select

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_tasks_pic():
    async with async_session() as session:
        return await session.scalars(select(TaskPic))

async def get_tasks_aud():
    async with async_session() as session:
        return await session.scalars(select(TaskAud))

async def get_users():
    async with async_session() as session:
        return await session.scalars(select(User))

async def get_task_pic_by_id(task_id: int):
    async with async_session() as session:
        return await session.scalar(select(TaskPic).where(TaskPic.task_id == task_id))

async def get_task_aud_by_id(task_id: int):
    async with async_session() as session:
        return await session.scalar(select(TaskAud).where(TaskAud.task_id == task_id))