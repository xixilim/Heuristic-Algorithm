# Heuristic Homework 1
# Chenlin Cheng
# 4/5/2022

# here I use recursive method to get the optimal result
# as well as to improve the speed compared to enumarate method
import time
import pandas as pd
import numpy as np

start = time.time()
# Data Set 11:
items = (
    ("Item 1", 65180, 632214), ("Item 2", 46382, 199177), \
    ("Item 3", 19001, 115678), ("Item 4", 37482, 115930), \
    ("Item 5", 32514, 317392), ("Item 6", 70114, 291414), \
    ("Item 7", 86544, 453241), ("Item 8", 81509, 182698), \
    ("Item 9", 69863, 483958), ("Item 10", 87945, 635228), ("Item 11", 48606, 644285), ("Item 12", 55881, 964789), ("Item 13", 58405, 228681), \
    ("Item 14", 84609, 583784), ("Item 15", 41245, 728501), ("Item 16", 99993, 713860), ("Item 17", 71851, 675367), ("Item 18", 38634, 517185), ("Item 19", 73726, 109046), ("Item 20", 30272, 428856), ("Item 21", 56128, 598546), \
    ("Item 22", 75924, 801173), ("Item 23", 29231, 732172), ("Item 24", 81862, 582250),
    ("Item 25", 83937, 140103), ("Item 26", 10072, 998111), ("Item 27", 60193, 824838), ("Item 28", 49808, 247224), ("Item 29", 21057, 384383), ("Item 30", 50886, 717534), ("Item 31", 62513, 111929), ("Item 32", 31759, 149957), ("Item 33", 93863, 683949), ("Item 34", 41580, 161648), ("Item 35", 54374, 803493), ("Item 36", 28248, 101820), ("Item 37", 45494, 976183), ("Item 38", 18950, 857469), ("Item 39", 49268, 911089), ("Item 40", 41956, 416175), ("Item 41", 87130, 761721), ("Item 42", 32210, 948814), ("Item 43", 92018, 515866), ("Item 44", 70401, 926108), ("Item 45", 75357, 517202), ("Item 46", 89573, 835622), ("Item 47", 91687, 196146), ("Item 48", 84394, 281478),\
)
cap = 4282396

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

