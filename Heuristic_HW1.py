# Heuristic Homework 1
# Chenlin Cheng
# 4/5/2022

# here I use recursive method to get the optimal result
# as well as to improve the speed compared to enumarate method
import time
import pandas as pd
import numpy as np

start = time.time()
# load dataset
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970),\
    ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457),\
    ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992),\
    ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836),\
    ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655),\
    ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243),\
    ("Item 23", 224916, 466257), ("Item 24", 169684, 369261)
)
cap = 6404180

item_df = pd.DataFrame(list(items), columns=["name", "weight", "value"])
weight = item_df["weight"].tolist()
value = item_df["value"].tolist()
dp_matrix = np.full(shape=(len(weight), cap + 1), fill_value=-1)  # dynamic programming matrix
my_dic = {}  # I use this dict to record if I calculated the subtask


def get_max_value_ind(ind: int, weight: list, value: list, capacity_left: int, my_dic: dict) -> int:
    """
    Use recursive method to solve the knapsack problem
    :param ind: the index of current item
    :param weight: the list of the weight of each item
    :param value: the list of the value of each item
    :param capacity_left: how much space left in the knapsack
    :param I use this dict to record if I calculated the subtask
    :return: the maximum value can be got
    """

    # if there is no capacity left or the index is out of range, return 0
    if capacity_left <= 0 or ind >= len(weight): return 0

    my_key = str(ind) + str(capacity_left)
    if my_key in my_dic.keys(): return my_dic[my_key]

    # 1. we take the current item and put it into the knapsack
    value1 = 0
    if capacity_left >= weight[ind]:
        value1 = value[ind] + get_max_value_ind(ind + 1, weight, value, capacity_left - weight[ind], my_dic)

    # 2. we skip the current item and don't take it
    value2 = get_max_value_ind(ind + 1, weight, value, capacity_left, my_dic)

    value_max = max(value1, value2)

    my_dic[my_key] = value_max

    return value_max


def track_back(my_dic: dict, values: list, sizes: list, cap: int) -> int:
    """
    Track back according to the matrix and find which item to take
    :param my_dic: I use it to keep the history
    :param values: the value of each item
    :param sizes: the size of each item
    :param cap: total capacity
    :return: final capacity after taking items
    """
    # from the first item to the last but one
    for ind in range(len(values) - 1):
        current_key = str(ind) + str(cap)
        next_key = str(ind+1) + str(cap)
        if my_dic[current_key] != my_dic[next_key]:
            print(f"Item {ind + 1}")
            cap = cap - sizes[ind]
    # check the last one item
    if cap >= sizes[-1]:
        cap = cap - sizes[-1]
        print(f"Item {len(sizes)}")
    return cap


value_max = get_max_value_ind(0, weight, value, cap, my_dic)
cap_left_final = track_back(my_dic, value, weight, cap)
print(f"For a total value of {value_max} and a total volume of {cap - cap_left_final}")

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)
