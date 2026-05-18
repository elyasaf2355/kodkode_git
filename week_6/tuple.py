#1
def sum_t(t):
    sum = 0
    for i in t:
        sum += t
    return sum
#2
def max_t(t):
    max = t[0]
    for i in t[1:]:
        if i > max:
            max = i
    return max
#3
def count_t(t, x):
    count = 0
    for i in t:
        if i == x:
            count += 1
    return count
#4
def reverse_t(t):
    re_t = []
    for i in range(len(t)-1, -1, -1):
        re_t.append(t[i])
    return tuple(re_t)
#5
def re_pairs(t):
    re_t = []
    for i in range(0,len(t),+2):
        re_t.append(t[i + 1])
        re_t.append(t[i])
    return tuple(re_t)
#6
def min_max(t):
    max = t[0]
    min = t[0]
    for i in t[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max
#7
def dis(a, b):
    return (((b[0] - a[0])**2) + ((b[1]-a[1])**2))**0.5
#8
def merge_sort(t1,t2):
    return tuple(sorted(t1 + t2))
#9
def frequency(t):
    return tuple([(i,t.count(i)) for i in set(t)])
def frequency2(t):
    d = {}
    for i in t:
        if i in d.keys():
            d[i] += 1
        else:
            d.update({i:1})
    return tuple(d.items())
print(frequency2(("a", "b", "a", "c", "b", "a") ))
#10
def rotate(t, k):
    return t[k % len(t):] + t[:k % len(t)]

