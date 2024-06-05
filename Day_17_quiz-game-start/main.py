from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question_bank.append(Question(entry["text"], entry["answer"]))

q = QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()

print("You've completed the quiz")
print(f"Your final score is: {q.score}/{q.question_number}")