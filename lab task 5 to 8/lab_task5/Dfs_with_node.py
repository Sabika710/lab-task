class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_val(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def is_empty(self):
        return self.head is None

    def del_val(self):
        if self.is_empty():
            return None
        curr = self.head
        self.head = self.head.next 
        return curr.val 
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

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
    frontier = LinkedList()
    explored = set()
    frontier.add_val((initial, [initial])) 
    while not frontier.is_empty():
        state, path = frontier.del_val() 
        explored.add(state) 

        if state == goal:
            return path 

        neighbours = tree.get_neighbours(state)

        for neighbour in neighbours:
            if neighbour not in explored:
                frontier.add_val((neighbour, path + [neighbour]))

    return None 

# Example 
tree = Tree()
result = dfs(tree, "A", "F")
print("Path to goal:", result)