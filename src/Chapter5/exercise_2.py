# Exercise 5.2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

total = 0.0
count = 0
maximum_number = None
minimum_number = None

while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    number = None
    try:
        number = float(input_number)
    except:
        print("Invalid input")
        continue

    total += number
    count += 1

    if maximum_number is None:
        maximum_number = number

    if minimum_number is None:
        minimum_number = number

    if number > maximum_number:
        maximum_number = number

    if number < minimum_number:
        minimum_number = number

print(total, count, maximum_number, minimum_number)
