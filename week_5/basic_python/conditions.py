#1
from enum import member


def check_age():
    age = int(input("Enter age: "))
    if 0 > age < 120:
        print("Invalid")
    elif age < 13:
        print("child")
    elif age < 18:
        print("Teen")
    else:
        print("Adult")
#2
def check_char():
    char = input("Enter char: ")
    if not (char.isalpha() and char.isascii()):
        print("Invalid")
    elif char.swapcase() in "aeuoi":
        print("Vowel")
    else:
        print("Consonant")
#3
def age_or_member(age:int, vip:bool):
    if (age > 18 and vip) or age in [19, 20 ,21]:
        print("Approved")
    else:
        print("Rejected")
#4
def check_pass(passw, user_try):
    if passw == user_try:
        print("Access granted")
    elif user_try < 8:
        print("Too short")
    else:
        print("Wrong")
#5
def is_in_rect(x, y):
    if 10 < x < 50 and 20 < y < 80:
        print("inside")
    elif 10 > x or x > 50 or 20 > y or y> 80:
        print("outside")
    else:
        print("on border")
#6
def greeting():
    name = input("enter name: ") or "Anonymous"
    print(f"Hello {name}!!!")
#8
def count_positive():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    num3 = int(input("Enter number: "))
    print(bool(num1 > 0) + bool(num2 > 0) + bool(num3 > 0))
#10
def score_grading():
    grade = int(input())
    print("A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "F")