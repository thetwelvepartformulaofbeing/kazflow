from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных
DATABASE_URL = "sqlite:///./test.db"  # SQLite (для тестирования)
# Если используешь PostgreSQL:
# DATABASE_URL = "postgresql://username:password@localhost/db_name"

# Создание объекта Engine для работы с базой данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Базовый класс для определения моделей данных
Base = declarative_base()

# SessionLocal для управления сессиями
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
