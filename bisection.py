import math
iter_table = []
iter_no = 0
def bisection_method(f, a, b, e, max_iter, *root):
    global iter_no, iter_table
    if f(a) * f(b) >= 0:
        print("Bisection method cannot be applied. f(a) and f(b) must have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2

        iter_table.append({
            "iter no": iter_no + 1, "a": a, "b": b, "Approximate root": c,
            "Error": abs(c - root[0]) if root else abs((c - a) / 2 ** iter_no)
        })
        iter_no += 1

        if abs(b - a) < e:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def func(x):
    return x**3 - 7*x**2 + 14*x -6

root = bisection_method(func, 0, 1, 10**-100, 100, 2-math.sqrt(2))
print("Approximate root:", root)

for i in iter_table:
    print(" ".join(f"{k}: {v}  " for k, v in i.items()))