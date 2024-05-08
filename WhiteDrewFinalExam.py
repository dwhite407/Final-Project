'''Drew White Final Exam
   This code will act as a fitness tracker app
   and will allow users to input their set, reps, and weights
   that they worked on certain movements, but will also allow the user 
   to submit their cardio information for running'''
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


#This function will display the users sets, reps, and weight they did in their workout
def submitDataWeights(setEntry, repEntry, weightEntry): 
    setCount = setEntry.get()
    repCount = repEntry.get()
    weightCount = weightEntry.get()

    #This if statemenet validates the data entered by the user
    if setCount.isdigit() and repCount.isdigit() and weightCount.isdigit():
        resultWindow = tk.Toplevel()
        resultWindow.title("Workout Numbers")

        resultWindow.geometry("300x50")

        resultDisplay = tk.Label(resultWindow, text=f"You worked {setCount} sets\nYou did {repCount} reps per set\nYou used {weightCount} pounds for each set")
        resultDisplay.pack()
    else:
        messagebox.showerror("Error", "Please enter valid numbers for sets, reps and wieght.")

#This function allows an if statement validate if a number entered is a float or integer
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
#This function will display the users cardio information, such as their total time and distance they ran
def submitDataCardio(timeEntry, distanceEntry):
    time = timeEntry.get()
    distance = distanceEntry.get()

    #This if statment validates the data entered by the user
    if time.isdigit() and is_float(distance):
        result = tk.Toplevel()
        result.title("Cardio Statistics")

        result.geometry("300x50")

        resultDisplay = tk.Label(result, text=f"You ran for {time} minutes\n You ran a total of {distance} miles")
        resultDisplay.grid(row=0, column = 0)
    else:
        messagebox.showerror("Error", "Please enter valid numbers for time and distance. ")


#This function makes another window when the barbell squat button is clicked
#and will allow the user to input their numbers for their lifts
def squatBut():
    test = tk.Toplevel()
    test.title("Barbell Squat")

    sets = tk.Label(test, text = "How many sets? ")
    sets.grid(row = 0, column = 0)

    reps = tk.Label(test, text = "How many reps? ", pady= 5)
    reps.grid(row = 1, column = 0)

    weight = tk.Label(test, text="How much weight (pounds)? ")
    weight.grid(row = 2, column = 0)

    setEntry = tk.Entry(test)
    setEntry.grid(row = 0, column = 1)

    repEntry = tk.Entry(test)
    repEntry.grid(row = 1, column =1)

    weightEntry = tk.Entry(test)
    weightEntry.grid(row = 2, column = 1)

    result = tk.Label(test, text="")
    result.grid(row=3, column=0, columnspan=2)

    submitButton = tk.Button(test, text="SUBMIT", command=lambda: submitDataWeights(setEntry,repEntry, weightEntry))
    submitButton.grid(row =5, column=1, pady=5)

    repRes = tk.Label(test, text="")
    repRes.grid(row=4, column= 0, columnspan=2)

    returnButton = Button(test, text="Return to Main", command=test.destroy)
    returnButton.grid(row=5, column=0, pady=5)


#This function makes another window when the bench press button is clicked
#and will allow the user to input their numbers for their lifts
def benchBut():
    test = tk.Toplevel()
    test.title("Bench Press")

    sets = tk.Label(test, text = "How many sets? ")
    sets.grid(row = 0, column = 0)

    reps = tk.Label(test, text = "How many reps? ", pady= 5)
    reps.grid(row = 1, column = 0)

    weight = tk.Label(test, text="How much weight (pounds)? ")
    weight.grid(row = 2, column = 0)

    setEntry = tk.Entry(test)
    setEntry.grid(row = 0, column = 1)

    repEntry = tk.Entry(test)
    repEntry.grid(row = 1, column =1)

    weightEntry = tk.Entry(test)
    weightEntry.grid(row = 2, column = 1)

    result = tk.Label(test, text="")
    result.grid(row=3, column=0, columnspan=2)

    submitButton = tk.Button(test, text="SUBMIT", command=lambda: submitDataWeights(setEntry, repEntry, weightEntry))
    submitButton.grid(row =5, column=1, pady=5)

    returnButton = Button(test, text="Return to Main", command=test.destroy)
    returnButton.grid(row=5, column=0, pady=5)

    
#This function makes another window when the cardio buttone is clicked
#and will allow the user to input their running information
def cardioBut():
    test = tk.Toplevel()
    test.title("Cardio")

    time = tk.Label(test, text = "How long did you run (minutes)? ")
    time.grid(row=0, column=0)

    distance = tk.Label(test, text = "How far did you run (miles)? ")
    distance.grid(row = 1, column = 0)

    timeEntry = tk.Entry(test)
    timeEntry.grid(row = 0, column = 1)

    distanceEntry = tk.Entry(test)
    distanceEntry.grid(row = 1, column =1)

    submitButton = tk.Button(test, text="SUBMIT", command=lambda: submitDataCardio(timeEntry, distanceEntry))
    submitButton.grid(row =4, column=1, pady=5)

    returnButton = Button(test, text="Return to Main", command=test.destroy)
    returnButton.grid(row=4, column=0, columnspan=2, pady=5)

#This function allows the exit button to close out the whole application
def exitApp():
    window.destroy()

#Creates the main window
window = tk.Tk()
window.title("Fitness Tracker")
window.configure(bg="light green")



#This function allows the images to be displayed on the screen
def show_image(imagePath, row, column):
    try:
        # Load the image
        img = Image.open(imagePath)

        # Resize the image
        img = img.resize((300, 400))  # Resize the image to the desired dimensions

        # Create a Tkinter-compatible image object
        imgTk = ImageTk.PhotoImage(img)

        # Create a label to display the image
        picLabel = tk.Label(window, image=imgTk)
        picLabel.image = imgTk  # Keep a reference to avoid garbage collection
        picLabel.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')  # Add padding and alignment

    except FileNotFoundError:
        print("Image file not found. Check the file path.")

window.columnconfigure(0, weight=1)  # Column 0 will resize horizontally
window.columnconfigure(1, weight=1)  # Column 1 will resize horizontally
window.columnconfigure(2, weight=1)  # Column 2 will resize horizontally
window.rowconfigure(0, weight=1)     # Row 0 will resize vertically
window.rowconfigure(1, weight=0)     # Row 1 will resize vertically

#Display the bench press image
bench_image_path = r"C:\Users\lvwhi\Downloads\weight-lifting-muscle-man-bodybuilder-600nw-2294612599.webp"
show_image(bench_image_path, row = 0, column = 0)

#Display the barbell squat image
squat_image_path = r"C:\Users\lvwhi\Downloads\squat.png"
show_image(squat_image_path, row = 0, column = 1)

#display the cardio running image
cardio_image_path = r"C:\Users\lvwhi\Downloads\running.png"
show_image(cardio_image_path, row = 0, column = 2)

#This creates a fram for the buttons
buttonFrame = tk.Frame(window)
buttonFrame.grid(row =1, column = 0, columnspan = 3, pady=(5,0))

#This creates a button for barbell squat
squat = tk.Button(window, text= "Barbell Squat", width = 42, command=squatBut)
squat.grid(row = 1, column =1,  padx=5)

#This creates a button for the barbell bench press
bench = tk.Button(window, text= "Barbell Bench Press", width=42, command=benchBut)
bench.grid(row=1, column =0,  padx=5)

#This creates a button for the cardio
cardio = tk.Button(window, text = "Cardio", width = 42, command=cardioBut)
cardio.grid(row = 1, column = 2,  padx=5)

#This creates an exit application button
exitButton = tk.Button(window, text="Exit", width=42, command=exitApp)
exitButton.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

#Starts the main window 
window.mainloop()
