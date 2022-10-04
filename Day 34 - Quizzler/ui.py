from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain # instaniating QuizBrain
        # tkinter window creating
        self.window = Tk()
        self.window.title('Quizzler') #setting window title
        self.window.config(bg=THEME_COLOR, padx=20, pady=20) #setting background color and padding on x and y of screen

        # adding score label
        self.score_label = Label(text='Score: 0',fg="white", bg=THEME_COLOR, font=('Arial', 15))
        self.score_label.grid(row=0, column=1)

        # creating canvas and adding question text in the middle
        self.canvas = Canvas(width=300, height=250, bg="white",)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, #wraps text in canvas
            text="Some question",
            fill=THEME_COLOR,
            font=('Arial', 18, "bold")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # adding right and wrong buttons
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # adding first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # making bg color white everytime before displaying que
        self.canvas.config(bg='white')
        # displaying question if questions are remaining
        if self.quiz.still_has_questions():
        # updating score
            self.score_label.config(text=f'Score: {self.quiz.score}')
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=que_text)
        else:
            # ending quiz and displaying result
            result = f'You\'ve reached the end of Quiz!\nFinal Score: {self.quiz.score} out of {len(self.quiz.question_list)}'
            self.canvas.itemconfig(self.question_text, text=result)
            # disabling buttons after the end
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Returns True if answer is correct else False."""
        self.give_feedback(self.quiz.check_answer('True'))


    def false_pressed(self):
        """Returns True if answer is correct else False."""
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, is_right):
        # checking if answer is right
        if is_right:
            self.canvas.config(bg="green") # changing canvas bg to green if answer is right
        else:
            self.canvas.config(bg="red") # canvas bg to red on incorrect answer
        # calling self.get_next_question after 1000ms(1 sec.)
        self.window.after(1000, self.get_next_question)
