#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    return_value = [0, 0]

    index = length - 1
    i = 0
    x = 1

    while weights[return_value[0]] + weights[return_value[1]] != limit and return_value is not None or return_value[0] == return_value[1]:
        if i == index:
            return None
        elif weights[i] + weights[x] == limit:
            return_value[0] = x
            return_value[1] = i
        elif x == index:
            i += 1
            x = i + 1
        elif weights[i] + weights[x] != limit:
            x += 1
    return return_value


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


def test_ex1_1():
    weights_1 = [9]
    answer_1 = get_indices_of_item_weights(weights_1, 1, 9)


def test_ex1_2():
    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)


def test_ex1_3():
    weights_3 = [4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)


def test_ex1_4():
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)


test_ex1_1()
test_ex1_2()
test_ex1_3()
test_ex1_4()
