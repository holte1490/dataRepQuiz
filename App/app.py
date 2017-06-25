import sys
import os

sys.path.append(os.getcwd()[:os.getcwd().index('BCS')])

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from BCS.App.forms import QuestionForm

app: Flask = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from BCS.App import models
from BCS.App.questionService import QuestionService

@app.route('/')
def index():
    return render_template('index.html', title='Login')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/quiz/<quizname>', methods=['GET', 'POST'])
def quiz(quizname):
    form: QuestionForm = QuestionForm()
    question_service = QuestionService(db)

    questions = question_service.get_questions('denbin')
    print(questions)

    if form.validate_on_submit():
        print(form.question.data)

    return render_template(
        'quiz.html',
        questions=questions,
        form=form,
        question_title=quizname
    )

           
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

