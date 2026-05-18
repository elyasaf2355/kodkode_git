#1
def remove_dup(l):
    return set(l)
#2
def count_unique(l):
    return sum([1 for i in set(l)])
#3
def common_elements(l1, l2):
    return [i for i in l1 if i in l2]
def common_elements2(l1, l2):
    return sorted(set(l1) & set(l2))
#4
def unique_elements(l1, l2):
    return sorted(set(l1)^set(l2))
#5
def is_subset(a, b):
    return set(a) <= set(b)
#6
def is_unique(string):
    return len(string) == len(set(string))
#7
def first_repeated(l):
    for i in range(len(l)):
        if l[i] in l[:i]:
            return l[i]
    return None
#8
def unique_words(string):
    return len(set([w.lower() for w in string.split(" ")]))
#9
def pair_sum_exist(l, target):
    for i in l:
        if (target - i) in set(l):
            return True
    return False
#10
def difference(l1,l2):
    return [i for i in l1 + l2 if not (i in l1 and i in l2)]
print(difference([1, 2, 3, 4], [3, 4, 5, 6]))