#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        ratio = int(parts[0]) / int(parts[1])
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    # Dynamic Programming
    taken = [0] * len(items)

    def knapsackDP(k, j):
        if j == 0:
            return 0
        elif items[j-1].weight <= k:
            if knapsackDP(k, j-1) >= items[j-1].value + knapsackDP(k-items[j-1].weight, j-1):
    #             remember to mark it as 0!!!
                taken[j-1] = 0
                return knapsackDP(k, j-1)
            else:
                taken[j-1] = 1
                return items[j-1].value + knapsackDP(k-items[j-1].weight, j-1)
        else:
            taken[j-1] = 0
            return knapsackDP(k, j-1)


    value = knapsackDP(capacity, item_count)


    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
