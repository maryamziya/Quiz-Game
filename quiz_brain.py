from multiprocessing.connection import answer_challenge


class Quiz:

    def __init__(self,question_bank):
        self.q_bank = question_bank
        self.score = 0
        self.q_num = 0

    def next_question(self):
        question = self.q_bank[self.q_num].text
        answer = self.q_bank[self.q_num].answer
        user_ans = input(f"Q{self.q_num + 1}:{question} (True/False)").title()
        if user_ans == answer:
            print("You got it!!")

            self.score += 1
        else:
            print("It's wrong!")
        self.q_num += 1
        print(f"The answer was:{answer}.")
        print(f"Current score:{self.score}/{self.q_num}.")
