"""
ISYS5002 - Week 2 Lab
Exercise 2: User Preferences Survey
"""

# --- Step 1: Creating the survey ---
name = input("What's your name? ")
favourite_colour = input("What's your favourite colour? ")
favourite_food = input("What's your favourite food? ")
favourite_movie = input("What's your favourite movie? ")

print("\nHello, " + name + "!")
print("Your favourite colour is " + favourite_colour + ", you love " + favourite_food +
      ", and your favourite movie is " + favourite_movie + ".")

# --- Step 2: Extend with another preference ---
favourite_hobby = input("What's your favourite hobby? ")
print("Hello, " + name + "!")
print("Your favourite colour is " + favourite_colour +
      ", you love " + favourite_food +
      ", your favourite movie is " + favourite_movie +
      ", and you enjoy " + favourite_hobby + ".")

# --- Challenge 1: Starred preferences ---
print("\nYour preferences:")
print("* Name:", name)
print("* Favourite Colour:", favourite_colour)
print("* Favourite Food:", favourite_food)
print("* Favourite Movie:", favourite_movie)
print("* Favourite Hobby:", favourite_hobby)

# --- Challenge 2: F-string formatting ---
print(f"\nHello, {name}! Your favourite colour is {favourite_colour}, "
      f"you love {favourite_food}, your favourite movie is {favourite_movie}, "
      f"and you enjoy {favourite_hobby}.")
