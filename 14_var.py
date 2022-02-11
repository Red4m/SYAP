def get_distance(first_point: list, second_point: list) -> float:
    return ((first_point[0]-second_point[0])**2 + (first_point[1]-second_point[1])**2)**0.5


max_distance = 0
list_of_points = [[1, 3], [1, 5], [1, 7], [2, 8], [3, 7]]
for num, i in enumerate(list_of_points):
    for j in list_of_points[num+1:]:
        distance = get_distance(i, j)
        if distance > max_distance:
            max_distance = distance

print(max_distance)
