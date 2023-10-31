# [18:53] Vytautas Sluckas
# Write a Python program that prompts the user to input an integer and raises a ValueError 
# exception if the input is not a valid integer.
# exception ValueError:
# Raised when an operation or function receives an argument that has the right type but 
# an inappropriate value, and the situation is not described by a more precise exception such as IndexError.

# ​[18:54] Vytautas Sluckas
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# exception FileNotFoundError:

# from typing import Optional

# def get_integer_input() -> Optional[int]:
#     number = input("enter nr: ")
#     if number.isnumeric():
#         return int(number)
#     raise ValueError("Not number!")

# try:
#     print(get_integer_input())
# except ValueError:
#     print("enter number")

# def get_age() -> int:
#     number =input("enter age")
#     if number.isnumeric():
#         if int(number) > 18:
#             return int(number)
#         else:
#             raise ValueError("too young")
#     else:
#         raise TypeError("enter NUMBER")
    
# try:
#     age = get_age()
# except ValueError:
#     print("you are too young, you cant enter")
# except TypeError:
#     print("enter nr.")
# else: 
#     print(age)
# finally: print("i am done")      

# [19:58] Vytautas Sluckas
# write a function called calculate, function accepts sign as string, and two variables as integers. 
# Do the calculation between two numbers according to sign and return result Handle all possible errors that may occur.

from typing import Union

def calculator(sign: str, *args) -> Union[int, float]:
    if sign not in["+", "-", "*"]:
        raise ValueError("look at sign")
    if type(args) != int:
        raise TypeError("look at number")
    if sign =="+":
        return sum(args)
    if sign == "-":
        return args[0] - sum(args[1:])
    if sign == "*":
        res = 1
        for num in args:
            res *= num
        return res
print(calculator("-", 1, 2))

