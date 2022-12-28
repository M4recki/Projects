class QuizBrain:
    def __init__(self, QuestionList):
        self.QuestionList = QuestionList
        self.QuestionNumber = 0
        self.CurrentQuestion = None
        self.Score = 0


    def NextQuestion(self):
        self.CurrentQuestion = self.QuestionList[self.QuestionNumber]
        self.QuestionNumber += 1
        UserAnswer = input(f"Q.{self.QuestionNumber}: {self.CurrentQuestion.text} (True/False) ")
        self.CheckAnswer(UserAnswer, self.CurrentQuestion.answer)

    def StillHasQuestions(self):
        return self.QuestionNumber < len(self.QuestionList)

    def CheckAnswer(self, UserAnswer, CorrectAnswer):
        if UserAnswer == CorrectAnswer.lower():
            print("You got it right!")
            self.Score += 1
        else:
            print("You didn't get it right")
        print("Correct answer is: " + CorrectAnswer)
        print(f"Your current score is: {self.Score}/{self.QuestionNumber}.")
        print("\n")

