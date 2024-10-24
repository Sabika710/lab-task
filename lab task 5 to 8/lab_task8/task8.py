import math

def minmax(curr_depth, curr_index, is_max):
    tree_depth = int(math.log(len(scores), 2))

    if curr_depth == tree_depth:
        return scores[curr_index]

    if is_max:
        return max(minmax(curr_depth + 1, curr_index * 2, False), minmax(curr_depth + 1, curr_index * 2 + 1, False))
    else:
        return min(minmax(curr_depth + 1, curr_index * 2, True), minmax(curr_depth + 1, curr_index * 2 + 1, True))

# Example scores 
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Running the Minimax algorithm
best_score = minmax(0, 0, True)
print("Best score for maximizing player:", best_score)