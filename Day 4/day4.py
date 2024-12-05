from collections import defaultdict
import re

with open("input.txt", "r") as file:
    text = file.read().splitlines()

# Brute force form lists in 8 cardinal directions
lr = text
rl = [i[::-1] for i in text]
width = len(lr[0])
height = len(text)

ud = []
for i in range(width):
    tmp_col = []
    for j in range(height):
        tmp_col.append(text[j][i])
    ud.append("".join(tmp_col))
du = [i[::-1] for i in ud]

topleftdown = []

# Shamelessly stolen from SO
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return ["".join(i) for i in list(map(grouping.get, sorted(grouping)))]


cols = groups(text, lambda x, y: x)
rows = groups(text, lambda x, y: y)
fdiag = groups(text, lambda x, y: x + y)
bdiag = groups(text, lambda x, y: x - y)
colsR = [i[::-1] for i in cols]
rowsR = [i[::-1] for i in rows]
fdiagR = [i[::-1] for i in fdiag]
bdiagR = [i[::-1] for i in bdiag]

def count_xmas(strings):
    s = r"XMAS"
    return sum([len(re.findall(s, i)) for i in strings])


total = count_xmas(cols)+count_xmas(rows)+count_xmas(fdiag)+count_xmas(bdiag)+count_xmas(colsR)+count_xmas(rowsR)+count_xmas(fdiagR)+count_xmas(bdiagR)
print(total)