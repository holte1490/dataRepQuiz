from BCS.App.bcsRepository import QuestionsRepository


class QuestionService:
    def __init__(self):
        self.question_repository = QuestionsRepository()

    def get_questions(self, question_category: str) -> list():
        questions = self.question_repository.get_questions_for_category(question_category)

        print(questions)

        return questions

    # def get_answers(self, question_category):
    #     answers = self.