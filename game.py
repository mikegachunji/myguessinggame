import random


try:
    # This is for python2 users
    from Tkinter import *
except ImportError:
    # This is for python3 users
    from tkinter import *


# The upper limit
MAX = 10
# The lower limit
MIN = 1


class Application(Frame):

    # This is the GUI of the application

    def __init__(self, master):

        Frame.__init__(self, master)
        master.minsize(width=500, height=200)
        self.grid()

        self.create_widgets()

        # random number to be guessed by player
        self.number = random.randrange(MIN, MAX + 1)

        self.tries = 0

    def create_widgets(self):

        Label(self,
              text= "I'm thinking of a number between " + str(MIN) +
              " and " + str(MAX)
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Try to guess the number"
              ).grid(row=1, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Number of Tries: 0"
              ).grid(row=0, column=2, columnspan=2, sticky=W)

        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)

        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        Button(self,
               text ="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)

        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=2, column=2, columnspan=4, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid = Text(row=3, column=0, columnspan=3)

    def get_guess(self):
        try:
            guess = int(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid Entry")
        else:
            self.tries += 1
            Label(self,
                  text="Number of tries: " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def check_guess(self, guess):
        if guess < MIN or guess > MAX:
            self.display_message("Invalid input, guess is outside of range")
            self.tries -= 1
            return
        if guess == self.number:
            self.resetgame()
            return
        if guess < self.number:
            self.display_message("Guess Higher...")
            return
        elif guess > self.number:
            self.display_message("Guess Lower...")
            return

    def display_message(self, message):
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):
        self.number = random.randrange(MIN, MAX + 1)
        self.display_message("Game reset. Please enter a new number to play again")
        self.tries = 0
        Label(self,
              text="Number of tries: " + str(self.tries)
              ).grid(row=0, column=2, columnspan=4, sticky=W)

    def resetgame(self):
        self.display_message("Congrats! You guessed correctly. The number was " + \
                              str(self.number) + ". and it only took you " + \
                             str(self.tries) + " Tries!")

def main():
    root = Tk()
    root.title("My Guessing Game")
    app = Application(root)
    root.mainloop()


main()















