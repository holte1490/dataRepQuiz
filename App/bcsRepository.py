import sqlite3


class BcsConnection:
    db = sqlite3.connect('Student_Information.db')
    c = db.cursor()


class UserRepository(BcsConnection):

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


class QuestionsRepository(BcsConnection):

    def save_scores(self, c, dbs, bds, hds, dhs, name): ##not working properly
        print(dbs)
        print(bds)
        print(hds)
        print(name)


        c.execute('''UPDATE students SET denbin_score = ?, binden_score = ?, hexden_score = ?, denhex_score = ? WHERE name = ?''',
                  (dbs, bds, hds, dhs, name))
        print("Score updated")
        self.db.commit()


# def stu_table():
#     c.execute('''CREATE TABLE IF NOT EXISTS students(
#                       id integer PRIMARY KEY,
#                       name text NOT NULL,
#                       password text,
#                       denbin_score integer,
#                       binden_score integer,
#                       hexden_score integer,
#                       denhex_score integer
#                 );''')





