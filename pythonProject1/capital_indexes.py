# weight = int(input('Weight: '))
# lbs_kg = input('(L)bs or (K)g: ')
# conversion_rate = .45
#
# if lbs_kg.upper() == 'L':
#     kg = lbs_kg = weight * conversion_rate
#     print(f'You are {kg} kilos')
# elif lbs_kg.upper() == 'K':
#     lbs = lbs_kg = weight / conversion_rate
#     print(f'You are {lbs} pounds')


# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('sorry you failed')
#
# prompt = ""
# started = False
#
# while True:
#     prompt = input('> ').lower()
#
#     if prompt == 'help':
#         print('''
#             start - to start the car
#             stop - to stop the car
#             quit - to exit
#         ''')
#     elif prompt == 'start':
#         if started:
#             print('Car already started')
#         else:
#             started = True
#             print('car started')
#     elif prompt == 'stop':
#         if not started:
#             print(('car already stopped'))
#         else:
#             print('car stopped')
#             started = Falsest
#     elif prompt == 'quit':
#         break
#     else:
#         print("Sorry, I don't understand that")


# for item in 'Python':
#     print(item)
#
# for item in ['apple', 'orange', 'grapes']:
#     print(item)
#
# for item in range(5, 10, 2):
#     print(item)


# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')
# 1:54
# numbers = [2, 2, 2, 2, 5]
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)


# names = ['Larry', 'Curly', 'Moe']
# print(names[1])


# 1:59

# import math
#
# numbers = [3, 1, 15, 4, 14]
# max_nbr = max(numbers)
# print(max_nbr)

# numbers = [3, 1, 15, 4, 14]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max =   number
# print(max)

# 2:01 two dimensional lists
# import random
#
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#]
# matrix[1][1] = 20
# print(matrix[1][1])
# print(matrix)
#
# for row in matrix:
#     for item in row:
#         print(item)

# list methods 2:06:11
#
# numbers = [5, 2, 6, 7, 4]
#
# numbers.append(20)
# print(numbers)
# numbers.insert(0,89)
# print(numbers)
# numbers.remove(89)
# print(numbers)
# numbers.clear()
# print(numbers)
# numbers = [5, 2, 6, 7, 4]
# numbers.pop()
# print(numbers)
#
# numbers = [5, 2, 6, 7, 4]
# print(numbers.index(2))
#
# numbers = [5, 2, 6, 7, 4]
# print(50 in numbers)
#
# numbers = [5, 2, 6, 5, 7, 4]
# print(numbers.count(5))
#
# numbers = [5, 2, 6, 5, 7, 4]
# numbers.sort()
# print(numbers)
#
# numbers = [5, 2, 6, 5, 7, 4]
# numbers.reverse()
# print(numbers)
#
# numbers = [5, 2, 6, 5, 7, 4]
# numbers2 = numbers.copy()
# print(numbers2)


## ToDO Unique numbers in a list
# numbers = [5, 2, 6, 5, 7, 4]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

## ToDO Tuples
# numbers = (1, 2, 3)
# print(numbers[0])

# # unpacking
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# x, y, z = coordinates
# print(x, y, z)

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer["name"])
# print(customer.get("birthdate","June"))
# customer["birthdate"] = "June 9 1963"
# print(customer)

# digit_text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# phone = input('Enter your phone number ')
# for number in phone:
#     print(digit_text[int(number)])


# digits_mapping = {
#      "1": "One",
#      "2": "Two",
#      "3": "Three",
#      "4": "Four"
#     }
# output = ""
# phone = input('Enter your phone number ')
# for number in phone:
#     output += digits_mapping.get(number, "!") + " "
# print(output)
#
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😒"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
#
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# greet_user(last_name="Smith", first_name="John")


# def square(number):
#     return number * number
#
#
# #sq = square(10)
# print(square(10))

#
# def emojis(message):
#     words = message.split(' ')
#     emojis = {
#          ":)": "😊",
#         ":(": "😒"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input("> ")
# print(emojis(message))

# try:
#     age = int(input('Enter your age: '))
#     income = 30000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# constructors

# 3:03:30
# numbers = [1, 3, 5, 7, 9]
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point1 = Point()
# point1.draw()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
# person = Person("charles")
# person.talk()

# class Mammal():
#     def walk(self):
#
# class dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class cat(Mammal):
#     def meow(self):
#         print("meow")
#
#
# dog1 = dog()
# dog1.bark()


#
# from converters import lbs_to_kg
#
# weight = int(input("Enter your weight "))
# print(lbs_to_kg(weight))

# from utils import find_max
# numbers = [10, 3, 6, 2]
# print(find_max(numbers))

# Packages
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping

# from ecommerce.shipping import calc_shipping
# calc_shipping()

## ToDO Random Challenge
# import random
#
#
# def random_number():
#     return random.randint(1, 100)


# random_number()
# import random
# for i in range(3):
#     print(random.randint(10,20))

# import random
# members = ['John', 'George', 'Frank', 'Charles']
#
# leader = random.choice(members)
# print(leader)

# import random
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

# Path
# from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft

# Relative path
# path = Path("ecommerce")
# print(path.exists())
# # make directories
#
# path = Path("emails")
# try:
#     print(path.mkdir())
# except FileExistsError:
#     print(path.rmdir())

# path = Path()
# for file in path.glob('*'):
#     print(file)

# x = 1577.0 % 424.0
# print(x)
# x = 1577.0 / 424.0
# print(x)

# for x in range(5):
#     print(x)

# counter = 0
# for x in range(1, 10):
#     result = x % 2
#     if result == 0:
#         print(x)
#         counter += 1
# print(f"What have {counter} even numbers")
#
# #  this function makes the second parameter optional when you call the funtion by puting by=1
# def increment(number, by=1):
#     return number + by
#
#
# print(increment(2, 5))

# # ** allows you to send multiple key value pairs and it forms a dictionary
# def save_user(**user):
#     print(user["name"])
#
#
# save_user(id=1, name="John", age=22)
#
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
# print("Start")
# print(multiply(1,2,3))

## ToDO Fizz Buzz Challenge
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return 'FizzBuzz'
#     if input % 3 == 0:
#         return 'Fizz'
#     if input % 5 == 0:
#         return 'Fuzz'
#     return input
#
#
# print(fizz_buzz(25))

# letters = ["a", "b", "c"]
# for letter in enumerate(letters):
#     print(letter)


# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(index, letter)


## ToDO Determine which letter is uppercase in a string
# def capital_indexes(word):
#     for index, letter in enumerate(word):
#         if word[index].isupper():
#             output.append(index)
#     return output
#
#
# output = []
# capital_indexes("HeLlO")
# print(output)

## ToDO Online Status Challenge

# def online_count(statuses):
#     count = 0
#     for name in statuses:
#         if statuses[name] == "online":
#              count += 1
#     return count
#
#
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
#
# print(online_count(statuses))

# long version

# def online_count(people):
#     count = 0
#     for person, status in people.items():
#         if status == "online":
#             count += 1
#     return count
#
# people = {
#      "Alice": "online",
#      "Bob": "offline",
#      "Eve": "online",
#  }
#
# print(online_count(people))

# short version
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])
#
#
# people = {
#      "Alice": "online",
#      "Bob": "offline",
#      "Eve": "online",
#  }
#
# print(online_count(people))

## ToDO Thousands separator Challenge
# def format_number(number):
#     numbers = "{:,}".format(int(number))
#     return numbers
#
# format_number('1000000')
#
# # DIY solution
# def format_number(n):
#     result = ""
#     for i, digit in enumerate(reversed(str(n))):
#         if i != 0 and (i % 3) == 0:
#             result += ","
#         result += digit
#     return result[::-1]
#
# # built-in solution
# def format_number(n):
#     return "{:,}".format(n)

## ToDO Counting parameters Challenge
# def param_count(*args):
#     return (len(args))
#
# param_count()
# param_count(2, 3, 4)

## ToDO All equal Challenge
# def all_equal(list):
#    result = all(element == list[0] for element in list)
#    if (result):
#       return True
#    else:
#       return False
#
#
# List = [1, 1, 1]
# all_equal(List)

## ToDO Boolean and Challenge
# def triple_and(parm1, parm2, parm3):
#     if parm1 == True and parm2 == True and parm3 == True:
#         return True
#     else:
#         return False
#
#
# triple_and(True, True, True)


## ToDO  Incomplete
# def zap(a, b):
#     tuples_list = ()
#     tl = []
#     for i in range(4):
#         tuples_list = a[i], b[i]
#         tl.append(tuples_list)
#     return tl
#
# a = [0, 1, 2, 3]
# b = [5, 6, 7, 8]
#
# tl = zap([0, 1, 2, 3], [5, 6, 7, 8])
# print(tl)

#         uniques.append(number)
# Use a while loop or a for loop with range to count up an index i. Then use i to access each element in a and b at a
# time. Create a tuple and append it to a result list that you gradually build up.

## ToDO Double letters Challenge
# `def double_letters(word):
#     previous_letter = ''
#     for i in word:
#         if i == previous_letter:
#             return True
#         else:
#             previous_letter = i
#
#     return False
#
#
# double_letters("hello"
#
# # naive solution
# def double_letters(string):
#     for i in range(len(string) - 1):
#         letter1 = string[i]
#         letter2 = string[i+1]
#         if letter1 == letter2:
#             return True
#     return False
#
# # shorter solution
# # using a list comprehension, zip, and any
# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])

## ToDO Adding and removing dots Challenge
# def add_dots(word):
#     tl = ''
#     count = 0
#     length = len(word)
#     for i in word:
#         tl += i
#         count += 1
#         if count < length:
#             tl += '.'
#     print(tl)
#
# def remove_dots(word):
#     tl = ''
#     for i in word:
#         if i != '.':
#             tl += i
#     print(tl)
#
# add_dots("test")
# remove_dots("t.e.s.t"
#
# # the longer way
# def add_dots(s):
#     out = ""
#     for letter in s:
#         out += letter + "."
#     return out[:-1]
#
# def remove_dots(s):
#     out = ""
#     for letter in s:
#         if letter != ".":
#             out += letter
#     return out
#
#
# # the short way
# def add_dots(s):
#     return ".".join(s)
#
# def remove_dots(s):
#     return s.replace(".", "")

## ToDO Up and Down Challenge
# def up_down(number):
#     down = number - 1
#     up = down + 2
#     return (down, up)
# # up_down(5)
#
# def up_down(x):
#     return (x-1, x+1)


## ToDO min-maxing Challenge
# def largest_difference(list_of_numbers):
#     max_nbr = max(list_of_numbers)
#     min_nbr = min(list_of_numbers)
#     return max_nbr - min_nbr
#
# largest_difference([1,2,3])

# short solution
# def largest_difference(numbers):
#     return max(numbers) - min(numbers)
#
# # naive solution
# def largest_difference(numbers):
#     smallest = 100
#     for n in numbers:
#         if n < smallest:
#             smallest = n
#
#     largest = -100
#     for n in numbers:
#         if n > largest:
#             largest = n
#
#     difference = largest - smallest
#     return difference

## ToDO Palindrome Challenge
# def palindrome(word):
#     reverse_word = word[::-1]
#     if word == reverse_word:
#         return True
#     else:
#         return False
#
#
# palindrome("charles")
#
# def palindrome(string):
#     return string == string[::-1]
#
# palindrome("charles")


## ToDO Consecutive zeros Challenge
# def consecutive_zeros(bin_str):
#     result = 0
#     streak = 0
#     for letter in bin_str:
#         if letter == "0":
#             streak += 1
#         else:
#             streak = 0
#         result = max(result, streak)
#     return result
#
# consecutive_zeros("1001101000110")
#
#
# def consecutive_zeros(bin_str):
#     return max([len(s) for s in bin_str.split("1")])

## ToDO Type check Challenge
# def only_ints(parm1, parm2):
#     parm1_type = type(parm1)
#     parm2_type = type(parm2)
#     if parm1_type == parm2_type:
#         return True
#     else:
#         return False
#
#
# only_ints(1, 2)

# def only_ints(a, b):
#     return type(a) == int and type(b) == int


## ToDO Middle letter Challenge
# def mid(word):
#     result = len(word) % 2
#     if result != 0:
#         result = round(len(word) // 2)
#         x = word[result]
#         return x
#     else:
#         x = '""'
#         return x
#
# x = mid("abc")
# print(x)
#
# def mid(my_string):
#     length = len(my_string) % 2
#     if length == 0:
#         return ""
#     elif length != 0:
#         middle = len(my_string) // 2
#         return my_string[middle]
# print(mid("cars"))

# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
# def mid(string):
#     if len(string) % 2 == 0:
#         return ""
#     return string[len(string)//2]
#
# x = mid("abc")
# print(x)


## ToDO Counting syllables Challenge
# def count(word):
#     cnt = 0
#     for item in word:
#         if item == '-':
#             cnt += 1
#     return cnt + 1
#
#
# count('ho-tel')
#
# # naive solution
# def count(word):
#     syllables = 1
#     for letter in word:
#         if letter == "-":
#             syllables = syllables + 1
#     return syllables
#
# # using the count method
# def count(word):
#     return word.count("-") + 1
#
# # using split
# def count(word):
#     return len(word.split("-"))

## ToDO Custom zip Challenge
# def zap(a, b):
#     zap_list = []
#     for i in range(len(a)):
#         zap_list.append((a[i], b[i]))
#     return zap_list
#
# print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
#
#
# # concise solution with list comprehensions
# def zap(a, b):
#     return [(a[i], b[i]) for i in range(len(a))]

## ToDO Anagrams Challenge
# def is_anagram(string1, string2):
#     return sorted(string1) == sorted(string2)
#
#
# is_anagram("typhoon", "opython")

## ToDO Flatten a list Challenge
# def flatten(out_list):
#     new_list = []
#     for in_list in out_list:
#         for item in in_list:
#           new_list.append(item)
#     return new_list
# print(flatten([[1, 2], [3, 4], [5, 6], [7, 8]])
#
# # solution with nested list comprehensions
# # (can be put on a single line for conciseness)
# def flatten(outer_list):
#     return [
#         item
#         for inner_list in outer_list
#         for item in inner_list
#     ]

## ToDo Tic tac toe input Challenge
# board = [
#     ["X", "O", "X"], # 1
#     [" ", " ", " "], # 2
#     ["O", " ", " "], # 3
# ]   # A    B    C
#
# def get_row_col(tic_tac):
#     tic = tic_tac.upper()
#     col = tic[0]
#     row = int(tic[1]) - 1
#
#     board_keys = {"A": 0, "B": 1, "C": 2}
#
#     for key in board_keys:
#         if key == col:
#             column = board_keys[key]
#             return (row, column)
#
# print(get_row_col("c1"))

## ToDO List xor Challenge
# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
#
# Your function must return whether n is exclusively in list1 or list2.
#
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.
#
# For example:
#
# list_xor(1, [1, 2, 3], [4, 5, 6]) == True
# list_xor(1, [0, 2, 3], [1, 5, 6]) == True
# list_xor(1, [1, 2, 3], [1, 5, 6]) == False
# list_xor(1, [0, 0, 0], [4, 5, 6]) == False

# def list_xor(n, list1, list2):
#
#     list_one = n in list1
#     list_tow = n in list2
#
#     if list_one != list_tow:
#         return True
#
#     if list_one == list_tow:
#         return False

## ToDO Writing short code Challenge
# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
#
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
#
# What makes this tricky is that your function body must only contain a single line of code.
#
# def convert(lists): return [str(con_list) for con_list in lists]
# print(convert([1, 2, 3]))
#
# # using map
# def convert(ns):
#     return list(map(str, ns))

## ToDO Solution validation Challenge
# The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.
#
# Write a function named validate that takes code represented as a string as its only parameter.
#
# Your function should check a few things:
#
# the code must contain the def keyword
# otherwise return "missing def"
# the code must contain the : symbol
# otherwise return "missing :"
# the code must contain ( and ) for the parameter list
# otherwise return "missing paren"
# the code must not contain ()
# otherwise return "missing param"
# the code must contain four spaces for indentation
# otherwise return "missing indent"
# the code must contain validate
# otherwise return "wrong name"
# the code must contain a return statement
# otherwise return "missing return"
# If all these conditions are satisfied, your code should return True.
#
# Here comes the twist: your solution must return True when validating itself.
# def validate(code):
#
#     if "def" not in code:
#         return "missing def"
#     if ":" not in code:
#         return "missing :"
#     if "(" not in code or ")" not in code:
#         return "missing paren"
#     if "(" + ")" in code:
#         return "missing param"
#     if "    " not in code:
#         return "missing indent"
#     if "validate" not in code:
#         return "wrong name"
#     if "return" not in code:
#         return "missing return"
#     return True



## ToDO Sample "if statement" to a "Ternary Operator" statement
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

age = 18

message = "Eligible" if age >= 18 else not "Not Eligible"
print(message)

