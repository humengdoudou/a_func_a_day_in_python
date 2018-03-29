#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# This is the python code for testing random function in python lib.
#
# Author: hudoudou love learning
# Time: 2018-03-29

import random

# random lib test

print(random.random())                       # randomly generate a float in [0,1)

print(random.uniform(1, 5))                  # randomly generate a float in [min, max)

print(random.randint(1, 5))                  # randomly generate an int in [min, max]

print(random.randrange(10))                  # randomly generate an int in [0, max)
print(random.randrange(1, 10))               # randomly generate an int in [min, max)
print(random.randrange(1, 10, 2))            # randomly generate an int in [min, max), step size: N, so int is min + K * N

print(random.choice("abc"))                  # randomly select a char from string
print(random.choice([1, 2, 3]))              # randomly select an element from list

print(random.sample("abcdefg", 3))           # random select N chars from string, the N chars to be a new list
print(random.sample([1, 2, 3, 4, 5, 6], 3))  # random select N elements from list, the N elements to be a new list

list_number = [1, 2, 3, 4, 5]
random.shuffle(list_number)
print("shuffle(list):", list_number)         # random shuffle a list
