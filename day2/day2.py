import re


with open('input.txt') as f:
    lines = f.readlines()


x = 12
y= 13
z = 14
valid = []

for line in lines:
    games = int(line.split(":")[0].replace("Game ", ''))
    reds = re.findall(r'(\d+) red', line)
    greens = re.findall(r'(\d+) green', line)
    blues = re.findall(r'(\d+) blue', line)
    
    if all(int(red) <= x for red in reds) and \
       all(int(green) <= y for green in greens) and \
       all(int(blue) <= z for blue in blues):
        valid.append(games)

powers = []
for line in lines:
    reds = re.findall(r'(\d+) red', line)
    greens = re.findall(r'(\d+) green', line)
    blues = re.findall(r'(\d+) blue', line)
    max_red = max([int(x) for x in reds])
    max_blue = max([int(x) for x in blues])
    max_green = max([int(x) for x in greens])
    power = max_red*max_blue*max_green
    powers.append(power)
print(sum(powers))

print(sum(valid))