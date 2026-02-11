from pyamaze import maze, agent, textLabel
import heapq


# Heuristic function

def manhattan(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



# A* Search Algorithm for pyamaze

def astar(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    goal = (1, 1)

    open_set = []
    heapq.heappush(open_set, (0, 0, start))

    came_from = {}
    g_score = {start: 0}

    visited = set()

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(came_from, current)

        for direction in 'ESNW':  # East, South, North, West
            if m.maze_map[current][direction] == True:
                if direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif direction == 'S':
                    neighbor = (current[0] + 1, current[1])

                tentative_g = current_g + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + manhattan(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current

    return None

# Path reconstruction

def reconstruct_path(came_from, current):
    path = {}
    while current in came_from:
        path[came_from[current]] = current
        current = came_from[current]
    return path



# Run Example

if __name__ == "__main__":

    m = maze(10, 10)
    m.CreateMaze()

    path = astar(m)

    if path:

        print("Path found!")
        a = agent(m, footprints=True)

        m.tracePath({a: path})

        # Show path length
        l = textLabel(m, 'A-Star Path Length', len(path))

        m.run()

    else:
        print("No path found.")

