#Password Generator Project
import random
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_capital_letters = int(input("How many capital letters would you like in your password?\n"))
nr_letters= int(input("How many small letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


ran_capital_letters = random.sample(capital_letters, nr_capital_letters)
ran_letters = random.sample(small_letters, nr_letters)
ran_numbers = random.sample(numbers, nr_numbers)
ran_symbol = random.sample(symbols, nr_symbols)

ran_signs = ran_capital_letters + ran_letters + ran_numbers + ran_symbol

ran_signs = random.sample(ran_signs, k=len(ran_signs))

password = " "

for sign in ran_signs:
  password += sign

print(f"Your new password is: {password}")
