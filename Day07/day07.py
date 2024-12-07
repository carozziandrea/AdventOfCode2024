##AOC Day07

import time
day = "07"

class Node:
    def __init__(self,value):
        self.value = int(value)
        self.center = None
        self.left = None
        self.right = None

#Part 1
start = time.perf_counter()

def dfs_with_target(node, current_value, target, visited_targets):
    if current_value > target:
        return False

    if node is None:
        return False

    if node.left is None and node.right is None:
        if current_value == target and target not in visited_targets:
            visited_targets.add(target)
            return True
        return False

    if node.left and dfs_with_target(node.left, current_value + node.left.value, target, visited_targets):
        return True

    if node.right and dfs_with_target(node.right, current_value * node.right.value, target, visited_targets):
        return True

    return False

bridge = {}
with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        split = line.split(": ")
        test_value = split[0]
        cal_values = split[1].strip().split(' ')
        bridge.update({test_value:cal_values})

p1 = 0
sols = 0
visited_targets = set()
for t_val, c_val in bridge.items():
    root = Node(c_val[0])
    current = root
    for n in c_val[1:]:
        new_node = Node(n)
        current.left = new_node
        current.right = new_node
        current.center = new_node
        current = new_node
        found = dfs_with_target(root, root.value, int(t_val), visited_targets)
        if found:
            p1 += int(t_val)
            sols += 1

end = time.perf_counter()
print(f'Part 1: {p1}, {sols}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

def dfs_with_concat(node, current_value, target, visited_targets):
    #print(current_value)
    if current_value > target:
        return False

    if node is None:
        return False

    if node.left is None and node.right is None and node.center is None:
        if current_value == target and target not in visited_targets:
            visited_targets.add(target)
            return True
        return False

    if node.left and dfs_with_concat(node.left, current_value + node.left.value, target, visited_targets):
        return True

    if node.right and dfs_with_concat(node.right, current_value * node.right.value, target, visited_targets):
        return True
    
    if node.center and dfs_with_concat(node.center, int(str(current_value) + str(node.center.value)), target, visited_targets):
        return True

    return False

p2 = 0
sols = 0
visited_targets = set()
for t_val, c_val in bridge.items():
    root = Node(c_val[0])
    current = root
    for n in c_val[1:]:
        new_node = Node(n)
        current.left = new_node
        current.right = new_node
        current.center = new_node

        current = new_node
    path = [root.value]
    found = dfs_with_concat(root, root.value, int(t_val), visited_targets)
    if found:
        p2 += int(t_val)
        sols += 1

end = time.perf_counter()
print(f'Part 2: {p2}, {sols}')
print(f'\t {((end - start) * 10**3):.3f} ms')