# Exercise 2.5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

celsius_temperature = float(input("Enter Celsius temperature: "))

fahrenheit_temperature = (celsius_temperature * 1.8) + 32

print(celsius_temperature, "Celsius is equal to", round(fahrenheit_temperature, 2), "degree Fahrenheit")
