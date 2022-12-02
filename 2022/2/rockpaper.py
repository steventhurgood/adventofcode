import os

data_filename = os.path.join(
    os.path.dirname(__file__), "data/input.txt")

# A is rock
# B is paper
# C is scissors
# X is rock
# Y is paper
# Z is scissors

# score = 1 for rock, 2 for paper, 3 for scissors
# + 0 if lost, 3 if draw, 6 if won
scores = {
    ('A', 'X'): 3+1,
    ('A', 'Y'): 6+2,
    ('A', 'Z'): 0+3,

    ('B', 'X'): 0+1,
    ('B', 'Y'): 3+2,
    ('B', 'Z'): 6+3,

    ('C', 'X'): 6+1,
    ('C', 'Y'): 0+2,
    ('C', 'Z'): 3+3,
}

#  X = lose, Y = draw, Z = win
strategies = {
    ('A', 'X'): 0+3,  # they chose rock, I chose scissors
    ('A', 'Y'): 3+1,  # I chose rock
    ('A', 'Z'): 6+2,  # I chose paper

    ('B', 'X'): 0+1,  # they chose paper, I chose rock
    ('B', 'Y'): 3+2,  # I chose paper
    ('B', 'Z'): 6+3,  # I chose scissors

    ('C', 'X'): 0+2,  # they chose scissors, I chose paper
    ('C', 'Y'): 3+3,  # I chose scissors
    ('C', 'Z'): 6+1,  # I chose rock
}


score: int = 0
with open(data_filename) as f:
    for line in f:
        opponent, move = line.strip().split(' ')
        print(opponent, move)
        score += strategies[(opponent, move)]

print(score)
