from ui import QuizInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [Question(example['question'], example['correct_answer']) for example in question_data] # list comprehension - order matters

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#   quiz.next_question()
print("You've completed the quiz")
print('\n')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')