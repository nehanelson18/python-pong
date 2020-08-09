# https://www.youtube.com/watch?v=rfscVS0vtbw
# print("Hello World")
# DRAWING A SHAPE

# print("/___|")
# print("   /|")
# print("  / |")
# print(" /  |")

# VARIABLES AND DATA TYPES
# character_name = "Tom"
# character_age = 50.567
# is_Male - True
# 3 basic types of data, strings, numbers and boolean
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
# character_name = "Mike"
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ", ")

# WORKING WITH STRINGS
# can do \n  for new line
# phrase = "Giraffe Academy"
# print(phrase + " is cool")
# print(phrase.lower())
# print(phrase.isupper())  # prints boolean
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("z"))
# print(phrase.replace("Giraffe", "Elephant"))

# WORKING WITH NUMBERS
# print(3 + 4.5)
# print(10 % 3)
# my_num = -5
# print(my_num)
# turn number into string:
# print(str(my_num) + " my favorite number")
# print(abs(my_num))
# print(pow(3, 2))
# print(max(3, 11))
# print(round(3.7))
# from math import * (to reach the other libraries)
# floor, ceil, sqrt..

# GETTING INPUT FROM USERS
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# BUILDING A BASIC CALCULATOR
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# MAD LIBS GAME
# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a Celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# LISTS
# friends = ["neha", "sreeja", "sreeja", "karen", "mIke"]
# lucky_numbers = [1, 2, 3, 4, 5]
# print(friends[0])
# print(friends[1:3])
# friends[1] = "bob"
# print(friends[1])
# first position in the back of a list is -1

# LIST FUNCTIONS
# print(friends)
# friends.extend(lucky_numbers)
# friends.append("Creed")  # always adds to the end of list
# friends.insert(1, "Kelly")
# friends.remove("neha")
# friends.pop()  # removes last element in list
# friends.clear()
# print(friends.index("sreeja"))
# print(friends.count("sreeja"))
# friends.sort()
# print(friends)
# lucky_numbers.reverse()
# print(lucky_numbers)
# friends2 = friends.copy()
# print(friends)

# TUPLES
# like a list; it is immutable cannot be changed or modified.
# coordinates = [(4, 5), (6,7), (80,34)]
# coordinates[1] = 10 # as u can see immutable
# print(coordinates[1])
# difference between tuple and list; cannot be changed AT ALL

# FUNCTIONS  (code inside function has to be indented)
# def sayhi(name, age):
# print("Hello " + name + ", You are " + str(age))


# print("Top")
# sayhi("Mike", 35)
# sayhi("Steve", 70)
# print("Bottom")

# RETURN STATEMENTS
# return info from a function
# def cube(num):
# return num*num*num
# cant print anything after a return

# result = cube(4)
# print(result)

# IF STATEMENT
# is_male = True
# is_tall = False

# if is_male and is_tall:
# print("You are a tall male")
# elif is_male and not(is_tall):
# print("You are a short male")
# elif not(is_male) and is_tall:
# print("You are a short male")
# else:
# print(" You are not a male and not tall")

# IF STATEMENT & COMPARISONS
# def max_num(num1, num2, num3):
# if num1 >= num2 and num1 >= num3:
# return num1

# elif num2 >= num1 and num2 >= num3:
# return num2
# else:
# return num3


# print(max_num(300, 40, 5))

# BUILDING A BETTTER CALCULATOR
# num1 = float(input("Enter first number: "))
# op = (input("Enter operator: "))
# num2 = float(input("Enter second number: "))

# if op == "+":
# print(num1 + num2)
# elif op == "-":
# print(num1 - num2)
# elif op == "/":
# print(num1 / num2)
# elif op == "*":
# print(num1 * num2)
# else:
# print("invalid operator")

# DICTIONARIES (aka hastables)

# monthConversions = {
# define key value pairs
# "Jan": "January",
# "Feb": "February",
# "Mar": "March",
# "Apr": "April",
# "May": "May",
# "Jun": "June",
# "Jul": "July",
# "Aug": "August",
# "Sep": "September",
# "Oct": "October",
# "Nov": "November",
# "Dec": "December",

# }

# print(monthConversions["Nov"])
# print(monthConversions.get("Dec"))

# WHILE LOOP
# i = 1
# while i <= 10:
# print(i)
# i += 1
# print("done with loop")

# BUILDING A GUESSING GAMEre

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
# if guess_count < guess_limit:
# guess = input("Enter guess: ")
# guess_count += 1
# else:
# out_of_guesses = True

# if out_of_guesses:
# print(" Out of guesses, YOU LOSE")
# else:
# print("You win!")

# FOR LOOP
# friends = ["Jim", "Karen", "Kevin"]
# len(friends)
# for index in range(3, 10): # for index in range(len(friends))
# print(index)
# for index in range(5):
# if index == 0:
# print("first iteration")
# else:
# print("Not first")

# EXPONENT FUNCTION
# print(2**3)
# def raise_to_power(base_num, pow_num):
# result = 1
# for index in range(pow_num):
# result = result * base_num
# return result

# print(raise_to_power(3, 4))

# 2D LISTS & NESTED LOOPS
# number_grid = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for row in number_grid:
# for col in row:
# print(col)
# print(number_grid[2][1])

# BUILD A TRANSLATOR
# def translate(phrase):
# translation = ""
# for letter in phrase:
# if letter in "AEIOUaeiou":
# if letter.isupper():
# translation = translation + "G"
# else:
# translation = translation + "g"
# else:
# translation = translation + letter
# return translation


# print(translate(input("Enter a phrase: ")))

# COMMENTS
# use, can use ''' but it will take up space ''' #

# TRY EXCEPT
# try:
#answer = 10/0
#number = int(input("Enter a number: "))
# print(number)
# except ZeroDivisionError as err:
# print(err)
# except ValueError:
#print("invalid input")

# READING FILES
# w (modify),r (read), a (append), r+ (r and w)
#employee_file = open("employees.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline()) # reads first line
# print(employee_file.readlines())  # stores as an array
# for employee in employee_file.readlines():
# print(employee)
# employee_file.close()
# always close a file after u open it

# WRITING TO FILES
#employee_file = open("employees1.txt", "w")
#employee_file.write("Toby - Human Resources")
#employee_file = open("index.html", "w")
#employee_file.write("<p> This is HTML </p>")
#employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# MODULES AND PIP
# any external file u want to use just import
#import useful_tools
# print(useful_tools.roll_dice(10))
# python.org has all modules.
# pip helps install package modules

# CLASSES AND OBJECTS
# clases u can define ur own data type
#from Student import Student
#student1 = Student("Jim", "Business", 3.1, False)
#student2 = Student("Pam", "Art", 2.5, True)
# print(student2.gpa)

# BUILDING A MULTIPLE CHOICE QUIZ
'''
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
'''
# OBJECT FUNCTIONS
#from Student import Student
#student1 = Student("Oscar", "Accounting", 3.1)
#student2 = Student("Phyllis", "Business", 3.8)

#print(student2.on_honor_roll())

#INHERITANCE

