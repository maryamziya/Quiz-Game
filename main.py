#TODO: Make a question bank(list of question object)

from data import question_data
from question_model import Question
from quiz_brain import Quiz


q_bank = []
for ques in question_data:
    text = ques["question"]
    ans = ques["correct_answer"]
    qestion = Question(text,ans)
    q_bank.append(qestion)

quiz = Quiz(q_bank)
q_num = len(q_bank)
for question in range(q_num):
    quiz.next_question()

print(f"Total score:{quiz.score}/{q_num}.")

