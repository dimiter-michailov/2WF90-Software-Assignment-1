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


def check_32bit(num_str, radix):
    """
    Check if num_str in the given radix fits in 32-bits.
    """
    # Strip leading negative sign
    num_str = num_str.lstrip('-')

    # Define the maximum possible value for a signed 32-bit integer in each radix
    max_value_32bit = {
        2: "1111111111111111111111111111111",  # Max value base 2
        3: "12112122212110202101",            # Max value base 3
        4: "1333333333333333",                # Max value base 4
        5: "1004424420424",                   # Max value base 5
        6: "55303200553",                     # Max value base 6
        7: "104134211161",                    # Max value base 7
        8: "17777777777",                     # Max value base 8
        9: "547877367",                       # Max value base 9
        10: "2147483647",                     # Max value base 10
        11: "2826874035",                     # Max value base 11
        12: "4823711051",                     # Max value base 12
        13: "1A20B960",                       # Max value base 13
        14: "39949A577",                      # Max value base 14
        15: "684354074",                      # Max value base 15
        16: "7FFFFFFF"                        # Max value base 16
    }

    # Check if the string is longer than the max allowed length for the radix
    if len(num_str) > len(max_value_32bit[radix]):
        return False
    
    # Check if the string value exceeds the maximum allowed value for the radix
    if num_str > max_value_32bit[radix]:
        return False
    return True
