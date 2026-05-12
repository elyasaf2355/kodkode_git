#1
def print_odds():
    for i in range(1,10,2):
        if i == 7: break
        print(i)

#2
def enter_pass():
    while True:
        if input("Enter pass: ") == '1234':
            print("Welcome!")
            break
        print("Try again")
#3
def enter_products():
    prod_list = []
    while True:
        prod = input("Enter prod: ")
        if prod == 'done':
            print(prod_list)
            break
        prod_list.append(prod)
#3.5
for i in range (1,4):
    for j in range(1,4):
        if j == 2:
            break
        print((i,j))
#4
def vowels_count():
    word = input("enter word: ")
    count = 0
    for char in word:
        if char.lower() in "auieo":
            count += 1
    print(count)
#5
def mult_table():
    for i in range(1, 6):
        print("\n")
        for j in range(1, 6):
            print(i * j, end=" ")
#6
def reverse():
    word = input()
    for i in range(len(word)-1, -1,-1):
        print(word[i], end="")
#7
def count_even_digits(num):
    count = 0
    while num > 0:
        if (num % 10) % 2 == 0:
            count += 1
        num = num // 10
    print(count)
#8
def double_char(word):
    print("".join([c * 2 for c in word]))
#9
def ask_numbers():
    max = 0
    while True:
        num = int(input("Enter number: "))
        if num == 0:
            break
        if num > max:
            max = num
    print("max number is: ", max)
#10
def no_special(word):
    result = True
    for char in word:
        if not char.isdigit() and not char.isalpha():
            result = False
            break
    print(result)
#11
def reverse_number(num):
    new_num = 0
    while num > 0:
        new_num *= 10
        new_num += num % 10
        num = num // 10
    print(new_num)

