#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_lst = set(my_list)
    sum = 0
    for i in new_list:
        sum += i
    return sum
