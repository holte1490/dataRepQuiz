from BCS.App.bcsRepository import QuestionsRepository


class QuestionService:
    def __init__(self, db):
        self.question_repository = QuestionsRepository(db)

    def get_questions(self, category: str) -> list():
        questions = self.question_repository.get_questions_for_category(category)

        print(questions)

        return questions
