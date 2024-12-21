import turtle
from turtle import Screen, Turtle

# Function to draw a message box
def draw_message_box(message, color="black"):
    screen = turtle.Screen()
    screen.clear()
    screen.bgcolor("lightblue")
    
    pen = Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color(color)
    
    # Draw box
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(400)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
    pen.end_fill()
    
    # Write the message
    pen.penup()
    pen.goto(0, 20)
    pen.write(message, align="center", font=("Arial", 16, "bold"))

# Function to get gender input
def get_gender():
    gender = screen.textinput("Gender Input", "Enter your gender (M for Male or F for Female):")
    while gender not in ['M', 'F', 'm', 'f']:
        gender = screen.textinput("Invalid Input", "Please enter 'M' for Male or 'F' for Female:")
    return gender.upper()

# Function to get age input
def get_age():
    while True:
        try:
            age = int(screen.textinput("Age Input", "Enter your age:"))
            if age > 0:
                return age
            draw_message_box("Age must be a positive number.", "red")
        except (TypeError, ValueError):
            draw_message_box("Invalid input. Please enter a valid number.", "red")

# Function to calculate entry fee
def calculate_entry_fee(gender, age):
    if gender == 'M':
        if age < 10:
            return "Your entry is free!"
        elif 10 < age <= 20:
            return "Your entry fee is 30RS."
        elif 20 < age <= 80:
            return "Your entry fee is 50RS."
    elif gender == 'F':
        if age < 10:
            return "Your entry is free!"
        elif 10 < age <= 20:
            return "Your entry fee is 20RS."
        elif 20 < age <= 80:
            return "Your entry fee is 40RS."
    return "Invalid age. Please try again."

# Main function
def main():
    draw_message_box("Welcome to the Entry Fee Calculator!", "green")
    
    gender = get_gender()
    age = get_age()
    result = calculate_entry_fee(gender, age)
    
    draw_message_box(result, "blue")
    
    # Wait for user to close
    screen.mainloop()

# Initialize Turtle Screen
screen = Screen()
screen.title("Entry Fee Calculator")
main()
