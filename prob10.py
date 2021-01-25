# Part a
def parse(fname="input10a.txt"):
    with open(fname) as f:
        for line in f:
            yield int(line)

def part1():
    nums = list(parse())
    nums = [0] + sorted(nums) + [max(nums) + 3]
    diffs = [y-x for x,y in zip(nums[:-1], nums[1:])]
    return diffs.count(1) * diffs.count(3)

print(part1())


# Part b
def diff(list):
    return [y-x for x,y in zip(list[:-1], list[1:])]

def integer_composition(n):
    from sympy import symbols, Poly
    x = symbols('x')
    f = 0
    for k in range(n+1):
        f += (x + x**2 + x**3)**k
    return Poly(f, x).coeff_monomial(x**n)

def part2():
    # Get the sorted adapter sequence
    nums = list(parse())
    nums = [0] + sorted(nums) + [max(nums) + 3]
    # Find the diffs, add a faux 3 at the beginning and then find the locations of the threes
    diffs = [3] + diff(nums)
    ixs = [i for i, x in enumerate(diffs) if x == 3]
    diffs = (integer_composition(x-1) for x in diff(ixs))
    from functools import reduce
    return reduce(lambda x, y: x * y, diffs)

print(part2())


# Appendix
# Part b
def get_sequences(nums):
    """Brute force; times out."""
    current_choice = nums[0]
    if len(nums) == 1:
        return [[current_choice]]
    choices = [i for i, x in enumerate(nums) if current_choice < x <= current_choice + 3]
    if len(choices) == 0:
        return [[current_choice]]
    sequences = ([current_choice] + seq for i in choices for seq in get_sequences(nums[i:]))
    return sequences
