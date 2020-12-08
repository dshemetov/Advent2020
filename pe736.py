# Project Euler 736
def get_p(p, pt):
    x, y = pt
    for f in reversed(p):
        (x, y) = (x + 1, 2 * y) if f == "r" else (2 * x, y + 1)
    return (x, y)


path = list(["r", "r", "s", "r", "s", "s", "s", "s", "r"])
get_p(path, (45, 90))

path = list(["r", "s", "s", "r"])
get_p(path, (45, 90))

path = list(["r", "r", "s", "r", "s", "s", "s", "s", "r"])
get_p(path, (45, 90))

path = list(["r", "r", "s", "r", "s", "s", "s", "s", "r"])
get_p(path, (0, 1))

path = list(["r", "r", "s", "r", "s", "s", "s", "s", "r"])
get_p(path, (45, 90))
