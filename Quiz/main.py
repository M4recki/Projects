from data import question_data
from question_model import NewQuestion
from quiz_brain import QuizBrain

Questions = []

# Iterate through the question_data list and create a new instance of the NewQuestion class for each dictionary
for Data in question_data:
    Question = NewQuestion(text=Data["question"], answer=Data["correct_answer"])
    Questions.append(Question)

Quiz = QuizBrain(Questions)
while Quiz.StillHasQuestions():
    Quiz.NextQuestion()
print("You have completed the quiz")
print(f"Your final score is {Quiz.Score}/{Quiz.QuestionNumber}")