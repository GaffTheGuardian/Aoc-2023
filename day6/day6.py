def input(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
    
    times = list(map(int, lines[0].strip().split()[1:]))
    distance = list(map(int, lines[1].strip().split()[1:]))

    return times, distance

def input_p2(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Remove spaces and convert to single large numbers
    times = int(''.join(lines[0].strip().split()[1:]))
    distance = int(''.join(lines[1].strip().split()[1:]))   

    return times, distance

def awad(time, record):

    x=0
    for youssef in range (1,time):
        traveltime=time - youssef
        distance_travel=youssef*traveltime
        if distance_travel > record:
            x+=1
    return x 

def main():
    times,distances = input('input.txt')

    number=[]
    for i in range(len(times)):
        x=awad(times[i], distances[i])
        number.append(x)
    result = 1 

    for x in number:
        result*=x
    print(result)

    time, distance = input_p2('input.txt')
    part2 = awad(time, distance)

    print(part2)

if __name__=="__main__":
    main()

        