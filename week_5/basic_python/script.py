#1
def is_even(num: int):
    print(num % 2 == 0)
#2
def swap(num1: int, num2: int):
    num1, num2 = num2, num1
    print(num1, num2)
def swap2(num1: int, num2: int):
    num1 = num2 + num1
    num2 = num1 - num2
    num1 = num1 - num2
    print(num1, num2)
#3
def sum_of_digits(num: int):
    sum = num // 100
    num = num % 100
    sum += num // 10 + num % 10
    print(sum)
#4
def BMI(height, weight):
    print(f"{weight / (height ** 2): .2f}")
#5n
def print_decimal(num: float):
    print(f"integer is: {int(num)}\nfractional is: {num - int(num)}")
print_decimal(3.83)