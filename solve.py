##
# 2WF90 Algebra for Security -- Software Assignment 1 
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:
# 48
#
# Author names and student IDs:
# Nikolov, Pavel (author_student_ID_1) 
# Ivanov, Niki (author_student_ID_2)
# Michailov, Dimiter (1854070)
# Krastev, Kris (author_student_ID_4)
##

# Import built-in json library for handling input/output 
import json

# Import fixedint library to restrict operations to only 32-bit values.
from fixedint import Int32

# Allowed digits for radices
digits = "0123456789ABCDEF"

def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###
    answer = None

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            # Solve integer arithmetic addition exercise
            x = exercise["x"]
            y = exercise["y"]
            radix = exercise["radix"]
            answer_value = addition(x, y, radix)
            answer = {"answer": answer_value}
        elif exercise["operation"] == "subtraction":
            # Solve integer arithmetic subtraction exercise
            x = exercise["x"]
            y = exercise["y"]
            radix = exercise["radix"]
            answer_value = subtraction(x, y, radix)
            answer = {"answer": answer_value}
        # et cetera
    else: # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to solve
        if exercise["operation"] == "reduction":
            # Solve modular arithmetic reduction exercise
            pass
        # et cetera

    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)

def addition(x_str, y_str, radix):
    """
    Perform addition on integers x_str and y_str.
    :param x_str: String representation of x in the given radix.
    :param y_str: String representation of y in the given radix.
    :param radix: The radix.
    :return: The result of the addition as a string and None if invalid.
    """

    # Trivial zero case
    if x_str == '0':
        return y_str
    elif y_str == '0':
        return x_str

    # Handle signs
    x_is_negative = x_str[0] == '-'
    y_is_negative = y_str[0] == '-'

    # Remove the negative sign for further calculations
    if x_is_negative:
        x_str = x_str[1:]
    if y_is_negative:
        y_str = y_str[1:]

    # Case 1: Both numbers are positive
    if not x_is_negative and not y_is_negative:
        result = addition_algorithm(x_str, y_str, radix)
        return result

    # Case 2: One number is negative and one is positive -> subtraction
    elif (x_is_negative and not y_is_negative) or (not x_is_negative and y_is_negative):
        if x_is_negative:
            return subtraction(y_str, x_str, radix)
        else:
            return subtraction(x_str, y_str, radix)

    # Case 3: Both numbers are negative -> perform addition and keep the negative sign
    elif x_is_negative and y_is_negative:
        result = addition_algorithm(x_str, y_str, radix)
        return '-' + result
    
def addition_algorithm(x_str, y_str, radix):
    """
    Algorithm for addition in any radix (helper function to "addition")
    :param x_str: String representation of x in the given radix.
    :param y_str: String representation of y in the given radix.
    :param radix: The radix.
    :return: The result of the addition as a string.
    """
    # Initialize carry to 0
    c = 0       # the carry

    # Ensure both numbers are of equal length by padding with leading zeros
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    # Convert the strings to lists of digits
    x_digits = [digits.index(digit) for digit in x_str]
    y_digits = [digits.index(digit) for digit in y_str]

    result = []

    # Iterate right to left
    for i in range(max_len - 1, -1, -1):
        z_i = x_digits[i] + y_digits[i] + c

        # If the result is greater than the radix add a carry
        if z_i >= radix:
            z_i -= radix
            c = 1  # Carry
        else:
            c = 0  # No carry

        # Append the result digit (z_i)
        result.append(digits[z_i])

    # Handle the final carry
    if c == 1:
        result.append('1')  # Add the final carry to the end of the list

    # The result is currently reversed (append adds at the end of the list)
    result.reverse()

    # Combine the result digits into a single string and return
    return ''.join(result).lstrip('0')  # Ensure no leading zeros in the result