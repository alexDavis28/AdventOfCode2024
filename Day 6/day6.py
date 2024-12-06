with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    lines = [list(line) for line in lines]

# Find the guard
start_y = None
start_x = None
guard = None
for y, line in enumerate(lines):
    for x, space in enumerate(line):
        if space == "^":
            guard = "^"
            start_y, start_x = y, x
            break
dy = 0
dx = 0
y = start_y
x = start_x
width = len(lines[0])
height = len(lines)

while True:
    match guard:
        case "^":
            dy = -1
            dx = 0
        case ">":
            dy = 0
            dx = 1
        case "v":
            dy = 1
            dx = 0
        case "<":
            dy = 0
            dx = -1
    # Bounds check I LOVE REVERSE INDEX
    if y+dy+1 > height or x+dx+1 > width or y+dy < 0 or y+dx < 0 :
        lines[y][x] = "X"
        break
    next_move = lines[y+dy][x+dx]
    if next_move == "#":
        match guard:
            case "^":
                guard = ">"
            case ">":
                guard = "v"
            case "v":
                guard = "<"
            case "<":
                guard = "^"
    else:
        lines[y][x] = "X"
        lines[y+dy][x+dx] = guard
        y += dy
        x += dx

# Count X
count = 0
for line in lines:
    for space in line:
        if space == "X":
            count += 1
print(count)