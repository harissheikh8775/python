# password generator project
# ........................EASY LEVEL............................#
import random

password=""
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "!",
    "#",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    "-",
    "_",
    "=",
    "?",
    "@",
    "^",
    "[",
    "]",
    "{",
    "}",
    "~",
]


print("Welcome to the PyPassword Generator!!")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your passwors?\n"))
no_numbers = int(input("How many numbers would you like in your passwrd?\n"))

for letter in range(no_letters):
    password+=letters[random.randint(0,len(letters)-1)]
for symbol in range(no_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]
for letter in range(no_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]
print(password)