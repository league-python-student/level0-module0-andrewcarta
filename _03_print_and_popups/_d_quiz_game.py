from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    vars = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    response =simpledialog.askstring('question 1', 'Answer yes or no to all questions.  do you like pizza?',)
    #      // 3.  Use an if statement to check if their answer is correct
    if response == "yes":
        vars+=1
    #      // 4.  if the user's answer was correct, add one to their score 
    response =simpledialog.askstring("question 2", 'did you answer yes to the last question?')
    if response == "yes":
        vars+=1
    if vars== 2:
        messagebox.showinfo(None, "you are one of the best people in the world, congradulations! you win the game")
    if vars== 1:
        messagebox.showinfo(None, "you lied!!!")
    if vars== 0:
        messagebox.showinfo(None, "are you human?!?!?")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method


#put in somewhere did you answer yes to the last question?  if yes then say youre awsome, if no say
#are you human?