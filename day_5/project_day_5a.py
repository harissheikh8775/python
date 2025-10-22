# password generator project
# ........................HARD LEVEL............................#
import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+-_=?@^[]{}~")

print("Welcome to the PyPassword Generator!!")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""

for _ in range(no_letters):
    password += random.choice(letters)
for _ in range(no_symbols):
    password += random.choice(symbols)
for _ in range(no_numbers):
    password += random.choice(numbers)

pass_list = list(password)
random.shuffle(pass_list)  # This shuffles the list in-place

result = "".join(pass_list)  # This joins the shuffled list

print("\nBefore shuffle:", password)
print("After shuffle:", result)
