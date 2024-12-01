with open("input.txt", "r") as file:
    lines = [line.split() for line in file.read().splitlines()]
left = sorted([int(line[0]) for line in lines])
right = sorted([int(line[1]) for line in lines])
left = [i*right.count(i) for i in left]
# distances = [abs(left[i] - right[i]) for i in range(len(left))]
print(sum(left))


# Code golf

print(sum([i*sorted([int(line[1]) for line in [line.split() for line in open("input.txt", "r").read().splitlines()]]).count(i) for i in sorted([int(line[0]) for line in [line.split() for line in open("input.txt", "r").read().splitlines()]])]))