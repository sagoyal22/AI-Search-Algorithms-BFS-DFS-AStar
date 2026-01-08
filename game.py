import heapq

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    for tile in range(1, 8):
        i = from_state.index(tile)
        j = to_state.index(tile)

        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(j, 3)

        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

    
def get_count_heuristic(from_state, to_state=(1,2,3,4,5,6,7,0,0)):
    """
    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that returns the count of the number of incorrectly placed elements in the from_state variable
    """
    count = 0
    for i in range(9):
        if from_state[i] != to_state[i]:
            count += 1
    return count

def print_succ(state):
    """

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))

def print_count_succ(state):
    """

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle along with count based heuristic 
    """
    
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_count_heuristic(succ_state)))


def get_succ(state):
    """

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
   
    succ_states = []
    
    zeros = [i for i, v in enumerate(state) if v == 0]

    for i in range(9):
        if state[i] == 0:
            continue  # tile must not be 0

        neighbors = []
        if i >= 3: neighbors.append(i - 3)
        if i <= 5: neighbors.append(i + 3)
        if i % 3 != 0: neighbors.append(i - 1)
        if i % 3 != 2: neighbors.append(i + 1)

        # Tile i can move into any zero neighbor
        for n in neighbors:
            if state[n] == 0:
                new_state = state.copy()
                new_state[i], new_state[n] = new_state[n], new_state[i]
                succ_states.append(new_state)

    # Remove duplicates + sort
    return sorted([list(s) for s in {tuple(s) for s in succ_states}])
    

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    import heapq

    pq = []

    closed_list = []

    visited = set()

    # initial cost
    h0 = get_manhattan_distance(state, goal_state)
    g0 = 0
    cost0 = g0 + h0

    heapq.heappush(pq, (cost0, state, (g0, h0, -1)))

    max_queue_length = 1

    # A* loop
    while pq:
        if len(pq) > max_queue_length:
            max_queue_length = len(pq)

        cost, cur_state, (g, h, parent_index) = heapq.heappop(pq)

        cur_tuple = tuple(cur_state)
        if cur_tuple in visited:
            continue
        visited.add(cur_tuple)

        closed_list.append((cur_state, parent_index, g, h))
        current_idx = len(closed_list) - 1

        if cur_state == goal_state:
            path = []
            idx = current_idx
            while idx != -1:
                st, p, g_val, h_val = closed_list[idx]
                path.append([st, h_val, g_val])
                idx = p
            path.reverse()

            state_info_list = []
            for st, h_val, g_val in path:
                state_info_list.append((st, h_val, g_val))

            max_length = max_queue_length

            for state_info in state_info_list:
                current_state = state_info[0]
                h = state_info[1]
                move = state_info[2]
                print(current_state, "h={}".format(h), "moves: {}".format(move))
            print("Max queue length: {}".format(max_length))

            return

        for succ in get_succ(cur_state):
            succ_tuple = tuple(succ)
            if succ_tuple in visited:
                continue

            g_new = g + 1
            h_new = get_manhattan_distance(succ, goal_state)
            cost_new = g_new + h_new

            heapq.heappush(pq, (cost_new, succ, (g_new, h_new, current_idx)))





if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()
    print_count_succ([2,5,1,4,0,6,7,0,3])
    print()
    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()
    solve([2,5,1,4,0,6,7,0,3])


