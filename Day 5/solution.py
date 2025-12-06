"""
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.
You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.
"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.
The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled.
When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

def read_input(file_path):
    ranges = []
    IDs = []
    
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip().split('-')
            if (len(line) == 2):
                ranges.append((int(line[0]), int(line[1])))
            elif (line[0] == ''):
                continue
            else:
                IDs.append(int(line[0]))

    return ranges, IDs

def count_valid_IDs(ranges, IDs):
    valid_IDs = 0
    
    for id in IDs:
        is_valid = False
        for r in ranges:
            if (r[0] <= id <= r[1]):
                valid_IDs += 1
                break
    
    return valid_IDs
    

file_path = 'Day 5/input.txt'
ranges, IDs = read_input(file_path)
valid_IDs_count = count_valid_IDs(ranges, IDs)
print(f'Number of valid IDs: {valid_IDs_count}')

"""
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""


def get_all_valid_IDs(ranges):
    new_ranges = []

    for r in ranges:
        next_ranges = [r]


        for r2 in new_ranges:
            for r1 in next_ranges:
                if (r1[0] > r2[1] or r1[1] < r2[0]):
                    continue
                elif (r1[0] >= r2[0] and r1[1] <= r2[1]):
                    next_ranges.remove(r1)
                    break
                elif (r1[0] < r2[0] and r2[0] <= r1[1] <= r2[1]):
                    next_ranges.remove(r1)
                    next_ranges.append((r1[0], r2[0]-1))
                elif (r2[0] <= r1[0] <= r2[1] and r1[1] > r2[1]):
                    next_ranges.remove(r1)
                    next_ranges.append((r2[1] + 1, r1[1]))
                elif (r1[0] < r2[0] and r1[1] > r2[1]):
                    next_ranges.remove(r1)
                    next_ranges.append((r1[0], r2[0]-1))
                    next_ranges.append((r2[1] + 1, r1[1]))
        new_ranges.extend(next_ranges)

    valid_IDs = 0
    for r in new_ranges:
        valid_IDs += (r[1] - r[0] + 1)
    return valid_IDs

all_valid_IDs_count = get_all_valid_IDs(ranges)
print(f'Number of all valid IDs: {all_valid_IDs_count}')