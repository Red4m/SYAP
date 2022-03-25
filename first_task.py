def my_func(number):  # 2, 4, 8 ,16 , 32, 64 , 128
    value = 0
    while value <= number - 1:
        value += 1
        yield 2 ** value


number = int(input("input number"))

data = my_func(number)
my_list = []
for i in range(number):
    my_list.append(next(data))

print(my_list)
