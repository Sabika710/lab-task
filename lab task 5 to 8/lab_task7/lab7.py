def heuristic(a, b):
    return abs(ord(a) - ord(b))

def a_star(graph, start, goal):
    open_set = {start}  
    came_from = {} 

    g_costs = {start: 0} 
    f_costs = {start: heuristic(start, goal)}  

    while open_set:
        current = min(open_set, key=lambda x: f_costs.get(x, float('inf')))
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        open_set.remove(current)
        for neighbor, cost in graph.get(current, []):
            tentative_g_cost = g_costs[current] + cost

            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                came_from[neighbor] = current
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                open_set.add(neighbor)

    return None 

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path[::-1] 

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('G', 1)],
    'E': [('B', 5), ('H', 2)],
    'F': [('C', 3), ('H', 1)],
    'G': [('D', 1)],
    'H': [('E', 2), ('F', 1)]
}

# Example
start = 'A'  
goal = 'H'  
result = a_star(graph, start, goal)
print("Path to goal:", result)