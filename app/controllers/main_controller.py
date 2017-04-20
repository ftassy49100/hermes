from datetime import datetime
from flask import redirect, url_for, flash
from flask.globals import request
from sqlalchemy.sql.functions import func

from app import app, db
from flask import render_template

from app.models.answer import Answer
from app.models.question import Question
from app.models.result import Result
from app.models.worker import Worker
from app.forms.forms import PointingForm
from app.repository.user_indicators import answers_per_user_per_category, user_per_category_json, answers_per_user
from random import randint


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/questions/list')
def questions_list():
    questions = Question.query.all()
    return render_template('questions.html', title='Liste des questions', questions=questions)


def question(worker):
    max_question = db.session.query(db.func.max(Question.id)).one()[0]
    question_id = randint(1, max_question)
    chosen_question = Question.query.filter_by(id=question_id)
    worker = worker
    return render_template('ask.html', title="Question " + str(question_id), questions=chosen_question,
                           worker=worker)


@app.route('/pointage', methods=['GET', 'POST'])
def pointing():
    form = PointingForm()
    if form.validate_on_submit():
        worker_id = form.worker_id.data
        worker = Worker.query.filter_by(id=worker_id).one()
        flash('{}, votre pointage a été pris en compte.'.format(worker.firstname), 'success')
        return question(worker)
    return render_template('pointing.html', title="Pointage", form=form)


@app.route('/store_result', methods=['GET', 'POST'])
def store_result():
    question_id = request.form.get('question_id')
    answer_id = request.form.get('answer')
    worker_id = request.form.get('worker_id')
    worker = Worker.query.filter_by(id=worker_id).one()
    question = Question.query.filter_by(id=question_id).one()
    answer_to_store = Result(question_id, answer_id, worker.id)
    db.session.add(answer_to_store)
    db.session.commit()
    res_id = answer_to_store.result_id
    return redirect(url_for('result', stored_id=res_id))


@app.route('/result/<stored_id>', methods=['GET', 'POST'])
def result(stored_id):
    result = Result.query.filter_by(result_id=stored_id).one()
    right_answer = Answer.query.filter_by(question_id=result.question_id, right_answer=1).one()
    user_answer = Answer.query.filter_by(id=result.answer_id).one()
    question = Question.query.filter_by(id=result.question_id).one()
    if user_answer == right_answer:
        flash('Bonne réponse !', 'success')
        return render_template('result.html', right_answer=True, question=question, answer=right_answer)
    flash('Mauvaise réponse !', 'danger')
    return render_template('result.html', right_answer=False, question=question, answer=right_answer)


@app.route('/result/user/<user_id>', methods=['GET'])
def indicator_per_user(user_id):
    user = Worker.query.filter_by(id=user_id).one()
    result_per_category = answers_per_user_per_category(user_id)
    nb_total_answer = answers_per_user(user_id)
    return render_template('user_indicators.html', user=user, nb_total_answer=nb_total_answer,
                           result_per_category=result_per_category)


@app.route('/profils')
def profils():
    users = Worker.query.all()
    return render_template('profil_list.html', users=users)


@app.route('/result/user/<user_id>/categories.json', methods=['GET'])
def user_category_json(user_id):
    return user_per_category_json(user_id)
