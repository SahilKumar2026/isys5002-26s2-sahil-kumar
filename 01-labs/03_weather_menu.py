"""
ISYS5002 - Week 2 Lab
Exercise 3: Crafting the Weather Menu
"""

# --- Step 1: Display the menu ---
print("Weather Menu:")
print("1. Check Temperature")
print("2. Check Humidity")
print("3. Check Wind Speed")
print("4. Exit")

# --- Step 2: Capture user input ---
choice = input("Enter your choice (1-4): ")
print("You selected option:", choice)

# --- Step 3 & 4: Add conditionals for each option ---
if choice == "1":
    temperature = input("Enter the current temperature (°C): ")
    temperature = float(temperature)
    if temperature >= 30:
        print("It's a hot day! Stay hydrated.")
    elif temperature <= 15:
        print("It's a bit cold, grab a jacket.")
    else:
        print("The temperature is quite mild today.")

elif choice == "2":
    humidity = input("Enter the current humidity level (%): ")
    humidity = float(humidity)
    if humidity >= 70:
        print("It's quite humid today.")
    else:
        print("The air is dry.")

elif choice == "3":
    wind_speed = input("Enter the current wind speed (km/h): ")
    wind_speed = float(wind_speed)
    if wind_speed >= 40:
        print("It's very windy, be careful outside.")
    else:
        print("Wind conditions are calm.")

elif choice == "4":
    print("Exiting the program.")

else:
    print("Invalid choice. Please select a valid option.")
