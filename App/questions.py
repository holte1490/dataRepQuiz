# import csv, random, sys, sqlite3
# from BCS.App.bcsRepository import QuestionsRepository
#
# ##read the file in and return question and answer set##
# def get_questions(qset):
#     questions = []
#     with open(qset,mode="r",encoding="utf-8") as my_file:
#         reader = csv.reader(my_file)
#         for row in reader:
#             questions.append(row)
#     return questions
#
# ##ask the question and mark##
# def ask_question(question,score):
#     print(question[0])
#     for multi in question[1:-1]:
#         print("{0:>5}{1}".format("",multi))
#     answer = input("Please enter an answer: ")
#     print()
#     if answer == question[-1]:
#         print("Correct!")
#         score += 1
#     else:
#         print("Incorrect!".format(question[-1]))
#     print()
#     return score
#
# ##cycle through question set at random and print final score##
# def topic(qset, intro_message):
#     questions = get_questions(qset)
#     score = 0
#     print(intro_message)
#     print("============================")
#     print()
#     print()
#     number = 10
#     for next_question in range(number):
#         question = random.choice(questions)
#         score = ask_question(question, score)
#         questions.remove(question)
#     print("Your final score was {0} out of {1}.".format(score,number))
#     p = (1.0*score/10)*100
#     return p
#
# ##display menu and validate choice##
# def displaymenu():
#     print("1. Progress Update")
#     print("2. Denary to Binary")
#     print("3. Binary to Denary")
#     print("4. Hexadecimal to Denary")
#     print("5. Denary to Hexadecimal")
#     print("6. Save Scores & Exit")
#     while True:
#         try:
#             choice = int(input("Please enter the number of your choice"))
#         except ValueError:
#             print("This is not a valid number, please try again")
#             continue
#         else:
#             return choice
#             break
#
#
# ##Add new student to table##
# def new_student():
#     stu_name = input("What is your full name?")
#     password = input("Please enter a suitable password")
#     dbconn.create_new_student(stu_name, password)
#     print("Welcome to the Number Representation Quiz", stu_name)
#     return stu_name
#
#
#
# if __name__ == "__main__":
#     dbconn.stu_table()
#     ##login/register##
#     new = input("Are you joining us for the first time?   Y/N" )
#     if new == "Y":
#         stu_name = new_student()
#     else:
#         stu_name =input("Please enter your name")
#         #implement proper login system
#
#     option = displaymenu()
#
#     denbin_score = 0
#     binden_score = 0
#     hexden_score = 0
#     denhex_score = 0
#
#     while option != 6:
#
#         if option == 1:
#             dbconn.progressUpdate(stu_name)
#         if option == 2:
#             denbin_score = topic("denbin.csv", "Denary to Binary Conversion")
#             print(denbin_score,"%")
#         if option == 3:
#             binden_score = topic("binden.csv", "Binary to Denary Conversion")
#             print(binden_score, "%")
#         if option == 4:
#             hexden_score = topic("hexden.csv", "Hexadecimal to Denary Conversion")
#             print(hexden_score,"%")
#         if option == 5:
#             denhex_score = topic("denhex.csv", "Denary to Hexadecimal Conversion")
#             print(denhex_score,"%")
#
#
#         option = displaymenu()
#
#     print(binden_score, denbin_score, hexden_score, denhex_score, stu_name)
#     dbconn.saveScores(c, denbin_score, binden_score, hexden_score, denhex_score, stu_name)
#     sys.exit()
#
