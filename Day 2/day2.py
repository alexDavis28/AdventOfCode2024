with open("input.txt", "r") as file:
    lines = [[int(i) for i in line.split()] for line in file.read().splitlines()]



count = 0
for line in lines:
    diffs = [(line[i+1]-line[i]) for i in range(len(line[:-1]))]
    if (all([i>0 for i in diffs]) or all([i<0 for i in diffs])) and all([1<=abs(i)<=3 for i in diffs]):
        count += 1
print(count)
