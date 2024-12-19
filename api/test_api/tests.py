from fastapi import APIRouter
from database.testservice import *

test_router = APIRouter(prefix="/test", tags=['вопросы'])

@test_router.post('/add_question')
async def add_question(level: str, main_question: str, correct_answer: str,
                       v1: str, v2: str, v3: str = None, v4: str = None):

    result = add_question_db(level=level, main_question=main_question,
                             v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    if result:
        return {"status": 1, "message": "успешно загружено"}
    return {"status": 0, "message": "ошибка"}


@test_router.get('/get_20_questions')
async def get_20_questions():
    result = get_questions_db()
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "ошибка"}



@test_router.get('/get_leaders')
async def get_leaders():
    result = get_top_10_db()
    print(result)
    return f"{result}"








