from heapq import *

# Project Euler 736
def get_p(p, pt):
    x, y = pt
    for f in reversed(p):
        (x, y) = (x + 1, 2 * y) if f == "r" else (2 * x, y + 1)
    return (x, y)

path = "rssr"
get_p(path, (45, 90))

path = "rrsrssssr"
get_p(path, (45, 90))
get_p(path, (45, 45 + 45))
get_p(path, (45, 45))
get_p(path, (0, 45))[1]


# A* search algorithm
def A_star(start_state, heuristic_distance):
    """
    Parameters
    ----------
    start: list of lists
        Start state.
    h: mapping from states to float
        Heuristic cost function.

    Returns
    ---------
    path: list
        A list of states from start to goal.
    """
    priority_queue = []
    current_distance = 0
    current_state = start_state
    current_path = ""

    while current_state[0] - current_state[1] != 0:
        # for choice in "rs": 
        for choice in ["rr", "rs", "sr", "ss"]:
            future_path = current_path + choice
            distance = (
                2
                + current_distance
                + heuristic_distance(future_path, start_state)
            )
            heappush(priority_queue, (distance, future_path))

        current_distance, current_path = heappop(priority_queue)
        current_state = get_p(current_path, start_state)

    return current_path

def rs_distance(path, start_state):
    difference = path.count("s") - path.count("r")
    return 4 * abs(1 - difference)

A_star([45, 90], heuristic_distance=rs_distance)