"""
ISYS5002 - Week 2 Lab
Exercise 1: Personalised Greeting & User Preferences
"""

import datetime

# --- Step 1: Collect basic user input ---
user_name = input("What is your name? ")
fav_colour = input("What is your favourite colour? ")
fav_food = input("What is your favourite food? ")

print("Name:", user_name)
print("Favourite Colour:", fav_colour)
print("Favourite Food:", fav_food)

# --- Step 2: Output a personalised summary ---
print("Hello, " + user_name + "! Your favourite colour is " + fav_colour +
      " and you love " + fav_food + ".")

# --- Step 3: Extend the program with an extra input ---
fav_hobby = input("What is your favourite hobby? ")
print("Hello, " + user_name + "! Your favourite colour is " + fav_colour +
      ", you love " + fav_food + ", and you enjoy " + fav_hobby + ".")

# --- Step 4: Experiment with input() ---
spirit_animal = input("What's your spirit animal? ")
print("Interesting choice! I wonder why a", spirit_animal, "resonates with you.")

# --- Step 5: Simple string manipulation ---
print("Your name in all caps is", user_name.upper() + "!")

# --- Challenge 1: Multi-line greeting ---
print("Hello, " + user_name + "!\nYour favourite colour is " + fav_colour +
      " and you love " + fav_food + ".")

# --- Challenge 2: Age calculator ---
birth_year_input = input("What year were you born? ")
birth_year = int(birth_year_input)
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are approximately {age} years old this year.")
