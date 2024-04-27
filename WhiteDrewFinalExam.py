'''Drew White Final Exam
   This code will act as a fitness tracker app
   and will allow users to input their set, reps, adn weights
   that they worked on certain movements.'''

import tkinter as tk
from PIL import Image, ImageTk

#This function builds another window when the barbell squat button is clicked
#and will allow the user to input their numbers for their lifts
def squatBut():
    test = tk.Toplevel()

    sets = tk.Label(test, text = "How many sets? ")
    sets.grid(row = 0, column = 0)

    reps = tk.Label(test, text = "How many reps? ", pady= 5)
    reps.grid(row = 1, column = 0)

    weight = tk.Label(test, text="How much weight? ")
    weight.grid(row = 2, column = 0)

    setEntry = tk.Entry(test)
    setEntry.grid(row = 0, column = 1)

    repEntry = tk.Entry(test)
    repEntry.grid(row = 1, column =1)

    weightEntry = tk.Entry(test)
    weightEntry.grid(row = 2, column = 1)

    result = tk.Label(test, text="")
    result.grid(row=3, column=0, columnspan=2)

    repRes = tk.Label(test, text="")
    repRes.grid(row=4, column= 0, columnspan=2)


    #this will display thet amount of sets a user inputs
    def display_set_count(event=None):
        set_count = setEntry.get()
        result.config(text=f"You worked {set_count} sets")

        

    # Bind the <FocusOut> event to the display_set_count function
    setEntry.bind("<FocusOut>", display_set_count)

#This function builds another window when the bench press button is clicked
#and will allow the user to input their numbers for their lifts
def benchBut():
    test = tk.Toplevel()

    sets = tk.Label(test, text = "How many sets? ")
    sets.grid(row = 0, column = 0)

    reps = tk.Label(test, text = "How many reps? ", pady= 5)
    reps.grid(row = 1, column = 0)

    weight = tk.Label(test, text="How much weight? ")
    weight.grid(row = 2, column = 0)

    setEntry = tk.Entry(test)
    setEntry.grid(row = 0, column = 1)

    repEntry = tk.Entry(test)
    repEntry.grid(row = 1, column =1)

    weightEntry = tk.Entry(test)
    weightEntry.grid(row = 2, column = 1)

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)

        # Open the image
        original_image = Image.open(r"C:\Users\lvwhi\Downloads\pictures\weights.jpg")
        
        # Resize the image to fit within a 400x300 box 
        original_width, original_height = original_image.size
        if original_width > 400 or original_height > 300:
            ratio = min(400 / original_width, 300 / original_height)
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)
            resized_image = original_image.resize((new_width, new_height))
        else:
            resized_image = original_image
        
        # Convert the resized image to PhotoImage
        render = ImageTk.PhotoImage(resized_image)
        
        # Create a Label widget to display the image
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        img.pack()

# Create the main window
window = tk.Tk()
window.title("Fitness Tracker")

# Create buttons (example)
bench = tk.Button(window, text="Bench Press", command=benchBut)
bench.pack()

squat = tk.Button(window, text="Barbell Squat", command=squatBut)
squat.pack()


# Create an instance of the Window class and start the main event loop
app = Window(window)
window.mainloop()
