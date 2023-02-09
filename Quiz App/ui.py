from customtkinter import *
from PIL import Image
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
font = ("Arial", 20, "italic")


class QuizInterface(CTk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz = quiz_brain

        # configure window
        self.title("Quizzler App By Marek Baranski")
        self.configure(fg_color=THEME_COLOR, padx=20, pady=20)

        # Score
        self.show_score = CTkLabel(
            self, text="Score: 0", text_color="white", font=font)
        self.show_score.grid(row=0, column=0, columnspan=2)

        # Frame
        self.main_frame = CTkFrame(
            self, width=300, height=250, corner_radius=10, fg_color="white")
        self.main_frame.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

        #Text in the main frame
        self.question_text = CTkLabel(self, text="Question", font=font, bg_color="white", text_color=THEME_COLOR, wraplength=200)
        self.question_text.grid(row=1, column=0, columnspan=2)

        #Buttons
        self.right = CTkImage(Image.open("images/true.png"), size=(60, 60))
        self.display_right = CTkButton(self, image=self.right, text="", width=60, height=60, fg_color="green", hover_color="dark green", command=self.true_choice)
        self.display_right.grid(pady=20, row=2, column=0)

        self.false = CTkImage(Image.open("images/false.png"), size=(60, 60))
        self.display_false = CTkButton(self, image=self.false, text="", width=60, height=60, fg_color="red", hover_color="dark red", command=self.false_choice)
        self.display_false.grid(pady=20, row=2, column=1, columnspan=2)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.main_frame.configure(fg_color="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.show_score.configure(text=f"Score: {self.quiz.score}")
            self.question_text.configure(text=q_text, fg_color="white")
        else:
            self.question_text.configure(text="You have reached the end of the quiz.", fg_color="white")
            self.display_right.configure(state="disabled")
            self.display_false.configure(state="disabled")

    def true_choice(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_choice(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.main_frame.configure(fg_color="green")
            self.question_text.configure(fg_color="green")
        else:
            self.main_frame.configure(fg_color="red")
            self.question_text.configure(fg_color="red")
        self.after(1000, self.get_next_question)
    

