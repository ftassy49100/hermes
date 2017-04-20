import json

from sqlalchemy.sql.functions import func
from app import db
from app.models.category import Category
from app.models.worker import Worker
from app.models.question import Question
from app.models.result import Result
from app.models.worker import Worker


def answers_per_category():
    return (db.session.query(Category, func.count(Result.result_id))
            .join(Question)
            .join(Result)
            .group_by(Category).all())


def answers_per_user(user_id):
    return db.session.query(func.count(Result.result_id)).filter_by(worker_id=user_id).first()[0]


def answers_per_user_per_category(user_id):
    return (db.session.query(Category, func.count(Result.result_id))
            .join(Question)
            .join(Result)
            .group_by(Category).filter_by(worker_id=user_id).all())


def user_per_category_json(user_id):
    data = []
    answer_categories = answers_per_user_per_category(user_id)
    for category, result in answer_categories:
        data.append([category.name, result])
    return json.dumps(data, ensure_ascii=False)
