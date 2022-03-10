from random import randint

# additional data for testing
# first_matrix = [[-1,-4,-7],[-4,7,8],[-1,-2,-3]]
# second_matrix = [[-4,-9,-7],[4,7,8],[0,-2,-10]]

first_matrix, second_matrix = [[[randint(-10, 10) for j_ in range(6)] for i_ in range(6)] for _ in range(2)]

print(first_matrix)
print(second_matrix)
first_matrix = [list(filter(lambda x: x >= 0, i)) for i in first_matrix]
second_matrix = [list(filter(lambda x: x >= 0, i)) for i in second_matrix]
result = []

for i, j in zip(first_matrix, second_matrix):
    if len(i) == 0 and len(j) == 0:
        result.append(1)
    else:
        result.append(0)

print(result)
