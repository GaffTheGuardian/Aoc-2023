import re

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]

points = []

for line in lines:
    parts = line.split("|")
    winners = parts[0].split(":")[1].split()
    current = parts[1].split()
    
    founds = 0
    for win in winners:
        if win in current:
            founds += 1
    
    if founds != 0:
        points.append(2**(founds-1))


print(sum(points))
#part 2 

lines = [[line.split(":")[1], 1] for line in lines]

for i in range(len(lines)):
    parts = lines[i][0].split("|")
    winners = parts[0].split()
    current = parts[1].split()
    founds = 0
    for win in winners:
        if win in current:
            founds += 1
    for nc in range(i+1, i+1+founds):
        if nc < len(lines):
            lines[nc][1] += lines[i][1]

cards = [x[1] for x in lines]
print(sum(cards))

