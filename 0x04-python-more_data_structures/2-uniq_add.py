#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_iter = set(my_list)
    uniq_sum = 0
    for i in new_iter:
        uniq_sum += i
    return uniq_sum
