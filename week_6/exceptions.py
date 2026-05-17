#1
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
#2
def safe_divide(a, b):
    try:
        return a /b
    except Exception:
        return "undefined"
#3
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"
#4
def parse_ints(values):
    int_values = []
    for i in values:
        try:
            int_values.append(int(i))
        except ValueError as e:
            print(e)
    return int_values
#5
def set_age(age):
    if 0 < age < 150:
        return age
    raise ValueError
#6
def retry(func, n):
    for i in range(n):
        try:
            return func()
        except Exception:
            if i == n - 1:
                raise

#7
def count_errors(funcs):
    count = 0
    for f in funcs:
        try:
            f()
        except Exception:
            count += 1
    return count
#8
def load_config(path):
    with open(path) as f:
        try:
            l = f.readline()
            print(l)
            int(l)
        except Exception as e:
            raise RuntimeError("failed to load config") from e

try:
    try:
        int("abc")
    except ValueError:
        raise RuntimeError("conversion failed") from ValueError("ddddd", "ggggg")
except RuntimeError as e:
    print(e.__context__)
    print()
