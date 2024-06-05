from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(bg=THEME_COLOR, text="Score: 0", fg='white', font=("Arial", 12), pady=10)
        self.score.grid(row=0, column=1, sticky='e')

        self.question_canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.question_canvas.create_text(150, 125, text="A Question", font=('Arial', 20, 'italic'), width=280)
        self.question_canvas.grid(row=1, column=0, columnspan=2)

        right_image = PhotoImage(file="images\\true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command= self.right_click)
        self.right_button.grid(row=2, column=0, pady=20)

        wrong_image = PhotoImage(file="images\\false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=self.wrong_click)
        self.wrong_button.grid(row=2, column=1, pady=20)

        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.score.config(text=f"Score : {self.quiz_brain.score}")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"Your Final Score is: {self.quiz_brain.score}")
            self.screen.after(1000, func=self.screen.destroy)

    def right_click(self):
        is_right = self.quiz_brain.check_answer("true")
        self.give_feedback(is_right)

    def wrong_click(self):
        is_right = self.quiz_brain.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.screen.after(1000, func=self.turn_white)
        self.screen.after(1000, func=self.get_next_question)

    def turn_white(self):
        self.question_canvas.config(bg='white')
