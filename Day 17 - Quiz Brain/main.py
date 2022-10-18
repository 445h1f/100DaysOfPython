from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    ans = question['answer']
    que = Question(text, ans)
    question_bank.append(que)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print('You completed the quiz.')
    print(f'Your final score was {quiz.score}/{quiz.question_number}.')