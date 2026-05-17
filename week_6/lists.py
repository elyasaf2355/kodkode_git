#1
def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum
#2
def max_list(l):
    max = l[0]
    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]
    return max
#3
def count_x(l, x):
    count = 0
    for i in l:
        if i == x: count += 1
    return count
#4
def reverse_l(l):
    new_l = []
    for i in range(len(l)-1 , -1 , -1):
        new_l.append(l[i])
    return new_l
#5
def rem_dup(l):
    new_l = []
    for i in l:
        if not i in new_l:
            new_l.append(i)
    return new_l
#6
def sec_max(l):
    max_x = max_list(l)
    return max([i for i in l if i != max_x])

#7
def merge(l1, l2):
    new_l = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            new_l.append(l1[i])
            i += 1
        else:
            new_l.append(l2[j])
            j += 1
    if i == len(l1):
        new_l += l2[j:]
    else:
        new_l += l1[i:]
    return new_l
#8
def rotate(l, key):
    i = 0
    while i < key:
        x = l.pop(0)
        l.append(x)
        i += 1
    return l
print(rotate([1,2,3,4,5], 7))

def rotate2(l, key):
    k = key % len(l)
    l = l[k:] + l[:k]
    return l
print(rotate2([1,2,3,4,5], 7))
