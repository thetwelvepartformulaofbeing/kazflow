from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User  # Импорт модели пользователя

app = FastAPI()

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to KazFlow!"}
