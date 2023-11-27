'''

Необходимо создать API для управления списком пользователей.
Создайте класс User с полями id, name, email и password.

API должен содержать следующие конечные точки:
— GET /users — возвращает список пользователей.
— GET /users/{id} — возвращает пользователя с указанным идентификатором.
— POST /users — добавляет нового пользователя.
— PUT /users/{id} — обновляет пользователя с указанным идентификатором.
— DELETE /users/{id} — удаляет пользователя с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.

'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


app = FastAPI()
users_db = []


@app.get("/users", response_model=list[User])
def get_users():
    return users_db


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user.dict())
    return user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_index] = updated_user.dict()
    return updated_user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.remove(user)
    return user
