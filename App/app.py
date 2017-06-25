import sys
import os

sys.path.append(os.getcwd()[:os.getcwd().index('BCS')])

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from BCS.App.forms import QuestionForm
from BCS.App.questions import get_questions

app: Flask = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', title='Login')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/quiz/<quizname>', methods=['GET', 'POST'])
def quiz(quizname):
    form: QuestionForm = QuestionForm()

    question_title: str = ""
    question_path: str = "./csv/" + quizname + ".csv"
    questions: list = []

    print(question_path)

    try:
        qs_and_as = get_questions(question_path)

        for q in qs_and_as:
            questions.append(q[0])

        if form.validate_on_submit():
            print(form.question.data)

    except FileNotFoundError:
        print("File not found")
        redirect(url_for("page_not_found"))

    return render_template(
        'quiz.html',
        questions=questions,
        form=form,
        question_title=question_title
    )

           
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

