import math
from hashlib import sha1

file = open('merklept2.txt')
lines = file.readlines()

i = int(lines.pop(0))
j = int(lines.pop(0))
leaves = []

def string_to_hash(tohash):
    return sha1(bytearray.fromhex(tohash)).hexdigest()

def strip_new_line(arr):
    newArr = []
    for i in range(0, len(arr)):
        newArr.append(lines[i].strip("\n"))
    return newArr

def depth_of_tree(arr):
    return math.floor(math.log(len(arr), 2)) + 1


leaves = strip_new_line(lines)


def next_tree_level(arr):
    temp = []
    for i in range(1, len(arr), 2):
        temp.append(string_to_hash(arr[i - 1] + arr[i]))
    return temp

def build_tree(leaves):
    temp = []
    append_if_len_is_uneven(leaves)
    next = next_tree_level(leaves)
    append_if_len_is_uneven(next)
    temp.append(leaves)
    temp.append(next)
    for x in range(0, depth_of_tree(leaves) - 1):
        next = next_tree_level(next)
        append_if_len_is_uneven(next)
        temp.append(next)
    return temp[::-1]


def append_if_len_is_uneven(arr):
    temp = arr
    if len(temp) % 2 != 0 and len(temp) != 2:
        temp.append(temp[len(temp) - 1])
    return temp



def merkle_path_for_i_at_depth_j(i, j, tree):
    n = len(tree)-j-1
    index = int(i // math.pow(2, n))
    tree[j][ index]
    string = ""
    if index % 2 == 0:
        string = "R" + tree[j][index + 1]
    else:
        string = "L" + tree[j][index - 1]
    return string + tree[0][0]


tree = build_tree(leaves)
print(merkle_path_for_i_at_depth_j(i, j, tree))
