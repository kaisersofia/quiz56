from fastapi import APIRouter
from database.userservice import *

user_router = APIRouter(prefix="/user",
                        tags=["Пользовательская часть"])
@user_router.post("/")
async def add_user(username: str, phone_number: str,
                   level: str = "easy"):
    result = add_user_db(name=username, phone=phone_number)
    if result:
        return {"status": 1, "message": "успешно зарегистрированы"}
    return {"status": 0, "message": "ошибка регистрации"}


@user_router.get("/get_all_users")
async def get_all_users():

    result = get_all_users_db()
    if result:
        return {"status": 1, "message": result}
    return {"satus": 0, "message": "ошибка"}


@user_router.get("/get_exact_user")
async def get_exact_user(user_id: int):
    result = get_exact_user_db(user_id)
    if result:
        return {"status": 1, "message": result}
    return {"satus": 0, "message": "ошибка"}

@user_router.post("/user_answer")
async def user_answer_api(user_id: int, level: str,
                      q_id: int, user_answer: str):
    result = users_answer_db(user_id=user_id, level=level,
                             q_id=q_id, user_answer=user_answer)
    if result:
        return {"status": 1, "message": result}
    return {"satus": 0, "message": "ошибка"}









