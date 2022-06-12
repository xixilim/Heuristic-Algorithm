# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:28:01 2022

@author: chenl
"""
import numpy
import numpy as np

data = np.array([[0, 0, 0, 0],
                 [4, 6, 5, 3],
                 [7, 8, 9, 7],
                 [9, 10, 11, 12],
                 [12, 11, 10, 14],
                 [15, 12, 9, 16]])

commercial = 5


def max_value(data):
    # define number of state & stage
    state = data.shape[0]
    stage = data.shape[1]
    # define array for dynamic programming
    vote = np.zeros(shape = (state, stage + 1), dtype = int)
    index = np.zeros(shape = (state, stage), dtype = int)
    for i in range(state):
        for j in range(stage):
            a = data[:i + 1, stage - j - 1] + vote[i::-1, stage - j]
            vote[i, stage - j - 1] = np.max(a)
            index[i, stage - j - 1] = np.argmax(a)

    return vote, index


def com_number(index, limit):
    index_list = np.zeros(shape = (index.shape[1],))
    # define the limit number of commercials
    num = limit
    # loop through each index to approach the limit
    for i in range(index.shape[1]):
        index_list[i] = index[num, i]
        num -= index[num, i]
    return index_list


if __name__ == "__main__":
    vote, index = max_value(data)
    area = com_number(index, commercial)
    
    print(f"The number of commercials in each area: {area}")
    print(f"The number of votes: {vote[-1, 0]} k")

