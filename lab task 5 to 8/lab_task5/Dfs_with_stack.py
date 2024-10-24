class Stack:
    def __init__(self):
        self.stack = []

    def add_val(self, val):
        self.stack.append(val)

    def pop_val(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        for i in self.stack:
            print(i)

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

def dfs(tree, initial, goal):
    frontier = Stack()
    explored = set()

    frontier.add_val((initial, [initial])) 

    while not frontier.is_empty():
        state, path = frontier.pop_val() 
        explored.add(state) 
        if state == goal:
            return path 
        neighbours = tree.get_neighbours(state)

        for neighbour in neighbours:
            if neighbour not in explored and not any(neighbour == s[0] for s in frontier.stack):
                frontier.add_val((neighbour, path + [neighbour]))

    return None 

# Example 
tree = Tree()
result = dfs(tree, "A", "F")
print("Path to goal:", result)
