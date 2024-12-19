from database import get_db
from database.models import *


# добавлен юзеров
def add_user_db(name, phone):
    db = next(get_db())
    new_user = User(username=name, phone_number=phone)
    # добав объект в бд
    db.add(new_user)
    # сохраняем изменения
    db.commit()
    return True

def get_all_users_db():
    db = next(get_db())
    # запрос в бд
    all_users = db.query(User).all()
    return all_users

def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user

# сохранение ответов юзера
def users_answer_db(user_answer, user_id, q_id, level):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=q_id).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False
        new_answer = user_answer(user_id=user_id, question_id=q_id,
                                 level=level, user_answer=user_answer)
        db.add(new_answer)
        db.commit()
        if correctness:
            user_result = db.query(Rating).filter_by(user_id=user_id).first()
            if user_result:
                user_result.correct_answers += 1
                db.commit()
                return True
        else:
            return False
    else:
        return False






























