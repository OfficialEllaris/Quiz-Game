class QuizBrain:
    def __init__(self, question_bank):
        self.question_id = 0
        self.question_bank = question_bank
        self.game_score = 0

    def has_more_questions(self):
        return self.question_id < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.question_id]
        self.question_id += 1
        user_answer = input(f"Q.{self.question_id}: {current_question.question} (True/False): ")

        self.evaluate_answer(user_answer, current_question.answer)

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.game_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.game_score}/{self.question_id}\n")
