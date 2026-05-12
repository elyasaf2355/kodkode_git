#1
def is_even(n):
    return n % 2 == 0
#2
def factorial(n):
    sum = n
    while n > 1:
        n -= 1
        sum *= n
    return sum
#4
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1 -i]:
            return False
    return True
#5
def sum_to_one_digit(n):
    if n < 10:
        return n
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum_to_one_digit(sum)
#6
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
#7
def reverse_number(num):
    flag = 1
    if num < 0:
        flag = -1
    num *= flag
    new_num = 0
    while num > 0:
        new_num *= 10
        new_num += num % 10
        num = num // 10
    return new_num * flag
#8
def moves_zero_to_end(nums):
    return [n for n in nums if n != 0] + [0] * nums.count(0)
def mzte(nums):
    i = 0
    z_count = 0

    while i < len(nums):
        if nums[i] == 0:
            z_count += 1
            nums.pop(i)
        else:
            i += 1
    nums += ([0] * z_count)
x = [0,0,0,1,3,0,5,0,0,5,7,8,0]
#9
def calculate(nums):
    print(f"sum: {sum(nums)}, average: {sum(nums) / len(nums):.2f}, minimum: {min(nums)}, maximum: {max(nums)}")
#10
def reverse(nums):
    return [nums[i] for i in range(len(nums)-1, -1, -1)]
#11
def del_dup(nums):
    i = len(nums)-1
    while i > 0:
        if nums[i] in nums[:i - 1]:
            nums.pop(i)
        i -= 1
    if nums[1] == nums[0]: nums.pop(1)

del_dup(x)
print(x)
