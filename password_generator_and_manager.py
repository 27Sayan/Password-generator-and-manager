import random
import string
import re

alphabets = list(string.ascii_lowercase)+list(string.ascii_uppercase)
numbers = [str(i) for i in range(10)]
special_char = list(string.punctuation)

def get_valid_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if not user_input:  
            print("Input cannot be empty. Please enter a positive integer.")
            continue
        match = re.match(r"^\d+$", user_input)
        if match and int(user_input) > 0:
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer greater than 0.")

def pass_generator(input_length,input_special_char,input_numbers,input_alphabets):
    new_pass = list(random.sample(alphabets,input_alphabets))+list(random.sample(numbers,input_numbers))+list(random.sample(special_char,input_special_char))
    return new_pass
    
def pass_checker(new_pass):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in new_pass:
       if char.isupper():
           has_upper = True
       elif char.islower():
           has_lower = True
       elif char.isdigit():
           has_digit = True
       elif not char.isalnum():
           has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return new_pass
    else:
        print("Unable to generate a strong password with those specifications.")
        exit()

def pass_add(user,password):
    with open('passwords.txt','a') as f:
        f.write(user + " | " + password + "\n")

def view_pass(uname):
    found = False
    with open('passwords.txt', 'r') as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split(" | ")
            if user == uname:
                print("User:", user, "Password:", passw)
                found = True
                break

    if not found:
        print("Username not found in the file.")

def pass_options():
    while True:
        option = input("Would you like to save or view your password? ").lower()
        if option == "save":
            username = input("Please enter the username for this password: ")
            pass_add(username,final_pass)
            print("Your password has been saved.")
            break
        elif option == "view":
            view_uname = input("Please enter the username for viewing your password: ")
            view_pass(view_uname)
            break
        else:
            print("Invalid input.")

input_length = get_valid_positive_integer("Length of your password: ")
input_special_char = get_valid_positive_integer("How many special characters would you like: ")
input_numbers = get_valid_positive_integer("How many numbers would you like: ")
input_alphabets = input_length - (input_numbers + input_special_char)

generated_password = pass_generator(input_length,input_special_char,input_numbers,input_alphabets)
final_pass = "".join(map(str, pass_checker(generated_password)))
print("Your password is: ",final_pass)
pass_options()
