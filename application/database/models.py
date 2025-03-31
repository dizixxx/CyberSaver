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

class TextTask(Base):
    __tablename__ = 'text_tasks'
    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_text: Mapped[str] = mapped_column(String(1000))
    task_options: Mapped[str] = mapped_column(String(5000))
    task_answer: Mapped[str] = mapped_column(String(1000))
    task_right_comment: Mapped[str] = mapped_column(String(1000))
    task_wrong_comment: Mapped[str] = mapped_column(String(1000))

class SberTopic(Base):
    __tablename__ = 'sber_topic'
    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_type: Mapped[str] = mapped_column(String(10))
    task_text: Mapped[str] = mapped_column(String(1000))
    task_link: Mapped[str] = mapped_column(String(1000))
    task_options: Mapped[str] = mapped_column(String(5000))
    task_answer: Mapped[int] = mapped_column(BigInteger)
    task_right_comment: Mapped[str] = mapped_column(String(1000))
    task_wrong_comment: Mapped[str] = mapped_column(String(1000))

class GosuslugiTopic(Base):
    __tablename__ = 'gosuslugi_topic'
    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_type: Mapped[str] = mapped_column(String(10))
    task_text: Mapped[str] = mapped_column(String(1000))
    task_link: Mapped[str] = mapped_column(String(1000))
    task_options: Mapped[str] = mapped_column(String(5000))
    task_answer: Mapped[int] = mapped_column(BigInteger)
    task_right_comment: Mapped[str] = mapped_column(String(1000))
    task_wrong_comment: Mapped[str] = mapped_column(String(1000))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)