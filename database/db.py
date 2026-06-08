from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    LargeBinary,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

DATABASE_URL = "sqlite:///database/attendance.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    employee_id = Column(
        String,
        unique=True,
        nullable=False
    )

    embedding = Column(
        LargeBinary,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class AttendanceLog(Base):

    __tablename__ = "attendance_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    status = Column(
        String,
        nullable=False
    )

Base.metadata.create_all(bind=engine)