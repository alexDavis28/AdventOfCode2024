with open("input.txt", "r") as file:
    lines = [line.split() for line in file.read().splitlines()]
left = sorted([line[0] for line in lines])
right = sorted([line[1] for line in lines])
distances = [abs(int(left[i]) - int(right[i])) for i in range(len(left))]
print(sum(distances))