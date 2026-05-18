#1
def sum_d(d):
    sum = 0
    for k, v in dict.items():
        sum += v
    return sum
#2
def max_d(d):
    max = d[d.keys()[0]]
    for k, v in d.items():
        if v > d[max]:
            max = k
    return max
#3
def count_chars(word):
    return {c: word.count(c) for c in set(word)}
#4
def switch(d):
    return {v:k for k,v in d.items()}
#5
def merge_d(d1, d2):
    d1.update(d2)
    return d1
#6
def filter_d(d, t):
    return {k:v for k,v in d.items() if v > t}
#7
def words_by_first(l):
    return {c : [word for word in l if word[0] == c] for c in set([w[0] for w in l])}
#8
def count_words_d(string):
    l = string.split(" ")
    return {w: l.count(w) for w in set(l)}
#9
def common_keyes(d1,d2):
    return sorted(set(d1.keys()) & set(d2.keys()))
#10
def most_common_value(d):
    return max(d.values(), key=lambda x: list(d.values()).count(x))
