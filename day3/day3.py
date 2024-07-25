with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1: Find valid numbers and calculate their sum
valid_numbers = []
for i in range(len(lines)):
    start = -1
    for j, char in enumerate(lines[i]):
        if char.isdigit():
            if start == -1:
                start = j
        else:
            if start != -1:
                number = lines[i][start:j]
                valid = False
                for x in range(max(0, i-1), min(len(lines), i+2)):
                    for y in range(max(0, start-1), min(len(lines[x]), j+1)):
                        if lines[x][y] not in '0123456789.':
                            valid = True
                if valid:
                    valid_numbers.append(number)
                start = -1
    if start != -1:
        number = lines[i][start:]
        valid = False
        for x in range(max(0, i-1), min(len(lines), i+2)):
            for y in range(max(0, start-1), len(lines[x])):
                if lines[x][y] not in '0123456789.':
                    valid = True
        if valid:
            valid_numbers.append(number)

valid_numbers = [int(no) for no in valid_numbers]
print("Sum of valid numbers:", sum(valid_numbers))

# Part 2: Compute valid gears
valid_numbers = []
for i in range(len(lines)):
    start = -1
    for j, char in enumerate(lines[i]):
        if char.isdigit():
            if start == -1:
                start = j
        else:
            if start != -1:
                number = lines[i][start:j]
                valid_no = -1
                for x in range(i-1, i+2):
                    if x >= 0 and x < len(lines):
                        for y in range(start-1, j+1):
                            if y >= 0 and y < len(lines[x]):
                                if lines[x][y] == '*':
                                    valid_no = (int(number), x, y)
                if valid_no != -1:
                    valid_numbers.append(valid_no)
                start = -1
#extends to end of line 
    if start != -1:
        number = lines[i][start:]
        valid_no = -1
        for x in range(i-1, i+2):
            if x >= 0 and x < len(lines):
                for y in range(start-1, len(lines[i])):
                    if y >= 0 and y < len(lines[x]):
                        if lines[x][y] == '*':
                            valid_no = (int(number), x, y)
        if valid_no != -1:
            valid_numbers.append(valid_no)

valid_numbers = sorted(valid_numbers, key=lambda x: (x[1], x[2]))

valid_gears = 0
i = 0
while i < len(valid_numbers) - 1:
    if valid_numbers[i][1] == valid_numbers[i+1][1] and valid_numbers[i][2] == valid_numbers[i+1][2]:
        gear = valid_numbers[i][0] * valid_numbers[i+1][0]
        valid_gears += gear
        i += 2
    else:
        print(f"No pair for {valid_numbers[i]}")
        i += 1

print("Sum of valid gears:", valid_gears)