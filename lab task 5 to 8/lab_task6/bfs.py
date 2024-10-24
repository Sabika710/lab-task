class Tree:
    def __init__(self):
        self.edges = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }

    def get_neighbours(self, node):
        return self.edges.get(node, [])

def bfs(tree, initial, goal):
    frontier = [(initial, [initial])]
    explored = set()

    while frontier:
        state, path = frontier.pop(0) 
        explored.add(state)  

        if state == goal:
            return path 

        neighbours = tree.get_neighbours(state)

        for neighbour in neighbours:
            if neighbour not in explored:
                frontier.append((neighbour, path + [neighbour]))

    return None  

# Example
tree = Tree()
result = bfs(tree, "A", "F")
print("Path to goal:", result)