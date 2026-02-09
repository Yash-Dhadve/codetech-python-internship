# Q1_MonkeyBananaProblem.py
# Solve Monkey-Banana Problem using BFS State Space Search

from collections import deque

# States follow the format:
# (monkey_position, box_position, monkey_on_box?, banana_taken?)
#
# Possible positions: "door", "window", "middle"
# monkey_on_box: True/False
# banana_taken: True/False

def get_neighbors(state):
    m_pos, b_pos, on_box, banana = state
    neighbors = []

    # 1 - Monkey moves alone (if not on box)
    if not on_box:
        places = ["door", "window", "middle"]
        for p in places:
            if p != m_pos:
                neighbors.append((p, b_pos, False, banana))

    # 2 - Monkey pushes the box (only if monkey and box at same place and monkey is NOT on box)
    if m_pos == b_pos and not on_box:
        places = ["door", "window", "middle"]
        for p in places:
            if p != m_pos:
                neighbors.append((p, p, False, banana))

    # 3 - Monkey climbs on the box (only if both at same place)
    if m_pos == b_pos and not on_box:
        neighbors.append((m_pos, b_pos, True, banana))

    # 4 - Monkey gets banana (only if monkey is on the box and box is under banana)
    if on_box and b_pos == "middle":
        neighbors.append((m_pos, b_pos, True, True))

    # 5 - Monkey comes down from box
    if on_box:
        neighbors.append((m_pos, b_pos, False, banana))

    return neighbors


# BFS search
def bfs():
    start = ("door", "window", False, False)
    goal_banana = True

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        m_pos, b_pos, on_box, banana = state

        if banana == goal_banana:
            return path

        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None


# ---------- RUN THE SOLVER ----------
solution = bfs()

print("Solution Path (Monkey -> Box -> Banana):\n")
for s in solution:
    print(s)

"""
Solution Path:

('door', 'window', False, False)
('middle', 'window', False, False)     <-- Monkey walks to middle
('middle', 'middle', False, False)     <-- Monkey pushes box to middle
('middle', 'middle', True, False)      <-- Monkey climbs on box
('middle', 'middle', True, True)       <-- Monkey takes banana
"""
