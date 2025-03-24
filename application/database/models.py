from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)

class TaskPic(Base):
    __tablename__ = 'tasks_pictures'

    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_text: Mapped[str] = mapped_column(String(100))
    task_picUrl: Mapped[str] = mapped_column(String(100))
    task_answer: Mapped[str] = mapped_column(String(100))
    task_comment: Mapped[str] = mapped_column(String(100))

class TaskAud(Base):
    __tablename__ = 'tasks_audio'

    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_text: Mapped[str] = mapped_column(String(100))
    task_audioLINK: Mapped[str] = mapped_column(String(100))
    task_answer: Mapped[str] = mapped_column(String(100))
    task_comment: Mapped[str] = mapped_column(String(100))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

