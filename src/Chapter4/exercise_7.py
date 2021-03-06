# Exercise 4.7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# Run the program repeatedly as shown above to test the various different values for
# input.

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

def computegrade(score):
    grade = ""

    if score > 1.0:
        grade = "Bad score"
    else:
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"

    return grade

score = 0.0
try:
    score = float(input("Enter score: "))
except:
    print("Error, please enter numeric input")
    quit()

grade = computegrade(score)

print(grade)
