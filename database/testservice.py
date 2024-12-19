from database import get_db
from database.models import *


def add_question_db(level, main_question, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Question(level=level, main_question=main_question,
                            v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return True

def get_all_questions_db():
    db = next(get_db())
    all_quest = db.query(Question).all()
    return all_quest


# первые 20 вопросов
def get_questions_db():
    db = next(get_db())
    all_question = db.query(Question).all()

    return all_question[:20]


# топ 10 юзеров
def get_top_10_db():
    db = next(get_db())
    leaders = db.query(Rating.user_id).order_by(Rating.correct_answers.desc())
    return f"{leaders[:10]}"

