import random
from collections import Counter

def func(copy_list: list):
  max_elemnt = max(copy_list)
  min_element = min(copy_list)
  if max_elemnt - min_element == 0:
    return None
  return max_elemnt - min_element

my_list = [[random.randint(-10,10) for _ in range(3)] for i_ in range(40)] # data
print(my_list)
test_list = [[1,2,7],[1,1,1],[8,8,8],[6,6,6]] #test data
result = []
for i in test_list:
  result.append(func(list(i)))

c = Counter(result)
print(result)
print(c[None])