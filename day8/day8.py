import math

def parse_input(file_path):
    with open(file_path, 'r') as file:
        instructions = file.readline().strip()
        file.readline()  # Skip empty line
        
        network = {}
        for line in file:
            node, connections = line.strip().split(' = ')
            left, right = connections[1:-1].split(', ')
            network[node] = (left, right)
    
    return instructions, network

def navigate_part1(instructions, network):
    current_node = 'AAA'
    steps = 0
    instruction_index = 0
    
    while current_node != 'ZZZ':
        instruction = instructions[instruction_index]
        if instruction == 'L':
            current_node = network[current_node][0]
        else:  # instruction == 'R'
            current_node = network[current_node][1]
        
        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)
    
    return steps

def navigate_part2(instructions, network):
    current_nodes = [node for node in network if node.endswith('A')]
    steps = 0
    instruction_index = 0
    
    cycle_lengths = []

    for start_node in current_nodes:
        node = start_node
        step = 0
        while not node.endswith('Z'):
            instruction = instructions[instruction_index]
            if instruction == 'L':
                node = network[node][0]
            else:  # instruction == 'R'
                node = network[node][1]
            
            step += 1
            instruction_index = (instruction_index + 1) % len(instructions)
        
        cycle_lengths.append(step)
    
    
    return math.lcm(*cycle_lengths)

def main():
    file_path = 'input.txt'  
    instructions, network = parse_input(file_path)
    
    steps_part1 = navigate_part1(instructions, network)
    print(f"Part 1 - Steps required to reach ZZZ: {steps_part1}")
    
    steps_part2 = navigate_part2(instructions, network)
    print(f"Part 2 - Steps required for all paths to end with Z: {steps_part2}")

if __name__ == "__main__":
    main()