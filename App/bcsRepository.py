import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class BaseRepository():
    def __init__(self, db):
        self.db = db

class UserRepository(BaseRepository):

    def create_new_student(self, user_name, password):
        self.c.execute('''INSERT INTO students(name, password)
                   VALUES(?,?)''',(user_name, password))
        self.db.commit()
        return user_name

    def progress_update(self, name):
        '''fetch data from database'''
        self.c.execute('''SELECT * FROM students WHERE name = ? ''',(name,))
        p = self.c.fetchone()
        print(p)

from BCS.App.models import Question

class QuestionsRepository(BaseRepository):


    # def save_scores(self, dbs, bds, hds, dhs, name): ##not working properly
    #     print(dbs)
    #     print(bds)
    #     print(hds)
    #     print(name)
    #
    #     self.c.execute('''UPDATE students SET denbin_score = ?, binden_score = ?, hexden_score = ?, denhex_score = ? WHERE name = ?''',
    #               (dbs, bds, hds, dhs, name))
    #     print("Score updated")
    #     self.db.commit()

    def get_questions_for_category(self, category):

        questions = Question.query.all()

        print(questions)

        print("Hello")
        print(category)

        #
        # self.db.execute(
        #         '''SELECT * FROM question WHERE question.category = ?''', (category,)
        #     )


        return ""








