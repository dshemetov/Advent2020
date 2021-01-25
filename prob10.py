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
def get_sequences(nums):
    current_choice = nums[0]
    if len(nums) == 1:
        return [[current_choice]]
    choices = [i for i, x in enumerate(nums) if current_choice < x <= current_choice + 3]
    if len(choices) == 0:
        return [[current_choice]]
    sequences = ([current_choice] + seq for i in choices for seq in get_sequences(nums[i:]))
    return sequences

def part2(fname="input10a.txt"):
    nums = list(parse(fname=fname))
    nums = [0] + sorted(nums) + [max(nums) + 3]
    diffs = [y-x for x,y in zip(nums[:-1], nums[1:])]
    ixs = [i for i, x enumerate(diffs) if x == 3]
    return len(list(get_sequences(nums)))

assert part2("test10b.txt") == 19208

nums = list(parse())
nums = [0] + sorted(nums) + [max(nums) + 3]
diffs = [y-x for x,y in zip(nums[:-1], nums[1:])]
ixs = [i for i, x in enumerate(diffs) if x == 3]
