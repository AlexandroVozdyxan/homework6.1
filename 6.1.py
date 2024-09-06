import string
from ctypes import string_at
from turtledemo.penrose import start

letters = string.ascii_letters
user_input = input("Enter a letters 'a-c': ")

if len(user_input) == 3 and user_input[0].isalpha() and user_input[1] == "-" and user_input[2].isalpha():
    first_letter = user_input[0]
    second_letter = user_input[2]

    start_index = letters.index(first_letter)
    end_index = letters.index(second_letter)

    if start_index > end_index:
        start_index, end_index = end_index, start_index
    result = letters[start_index:end_index + 1]
    print(result)