import math

iter_table = []
iter_no = 0

def false_positon_method(f, a, b, e, maxItr, *root):
    global iter_table, iter_no

    if f(a) * f(b) >= 0:
        print("Method cannot be applied it should be in the root [a, b] range")
        return None

    for i in range(maxItr):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        iter_table.append({
            "iter no": iter_no + 1, "a": a, "b": b, "Approximate root": c,
            "Error": abs(c - root[0]) if root else min(abs(c - a), abs(b - c))
        })
        iter_no += 1

        if abs(b - a) < e:
            return c

        if f(a) * f(c) >= 0:
            b = c

        else:
            a = c

    return (a * f(b) - b * f(a)) / (f(b) - f(a))

def function(x):
    return x**3 - 7*x**2 + 14*x -6

root = false_positon_method(function, 0, 1, 10**-100, 10)
print("Approximate root:", root)

for i in iter_table:
    print(" ".join(f"{k}: {v}  " for k, v in i.items()))
