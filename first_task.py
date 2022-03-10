import random


def is_all_numbers_equal_to_zero(random_set):
    if len(random_set) == 1 and random_set == {0}:
        return True
    return False


def is_first_non_zero_number(my_list):
    for i in my_list:
        if i == 0:
            continue
        elif i > 0:
            return "first_non_zero_number_positive"
        elif i < 0:
            return "first_non_zero_number_negative"


def main():
    n = input("input number")
    # additional data for testing
    # list_compr = [0 for _ in range(int(n))]
    list_compr = [random.randint(-10, 10) for _ in range(int(n))]

    print(list_compr)

    res = is_first_non_zero_number(list_compr)
    if is_all_numbers_equal_to_zero(set(list_compr)):
        print("first statement")
    elif res:
        print(res)
    else:
        print("no statement results")


if __name__ == "__main__":
    main()
