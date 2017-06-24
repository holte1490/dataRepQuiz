##sql database connection ##

import sqlite3

db = sqlite3.connect('Student_Information.db')
c = db.cursor()


def stu_table():
    c.execute('''CREATE TABLE IF NOT EXISTS students(
                      id integer PRIMARY KEY,
                      name text NOT NULL,
                      password text,
                      denbin_score integer,
                      binden_score integer,
                      hexden_score integer,
                      denhex_score integer
                );''')


def create_new_student(stu_name, password):
    c.execute('''INSERT INTO students(name, password)
                   VALUES(?,?)''',(stu_name, password))
    db.commit()
    return stu_name


def saveScores(c, dbs, bds, hds, dhs, name): ##not working properly

    print(dbs)
    print(bds)
    print(hds)
    print(name)
    
    c.execute('''UPDATE students SET denbin_score = ?, binden_score = ?, hexden_score = ?, denhex_score = ? WHERE name = ?''',
              (dbs, bds, hds, dhs, name))
    print("Score updated")
    db.commit()


def progressUpdate(name):
    '''fetch data from database'''
    c.execute('''SELECT * FROM students WHERE name = ? ''',(name,))
    p = c.fetchone()
    print(p)



