
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
  
    seeds = list(map(int, lines[0].strip().split(': ')[1].split()))

    """  seed_ranges = list(map(int, lines[0].strip().split(': ')[1].split()))
    print("Seed ranges parsed:")
    print(seed_ranges)

    for i in range(0, len(seed_ranges), 2):
        start = seed_ranges[i]
        length = seed_ranges[i + 1]
        seeds.extend(range(start, start + length))

    print("Extracted seeds:")
    print(seeds)"""

    
    maps = {}
    current_map = None
    for line in lines[1:]:
        line = line.strip()
        if line.endswith('map:'):
            current_map = line.split(' ')[0]
            maps[current_map] = []
        elif current_map and line:
            maps[current_map].append(tuple(map(int, line.split())))
    
    return seeds, maps


def convert(number, conversion_map):
    for dest_start, src_start, length in conversion_map:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number  


def find_location(seed, maps):
    seed_to_soil_map = maps['seed-to-soil']
    soil_to_fertilizer_map = maps['soil-to-fertilizer']
    fertilizer_to_water_map = maps['fertilizer-to-water']
    water_to_light_map = maps['water-to-light']
    light_to_temperature_map = maps['light-to-temperature']
    temperature_to_humidity_map = maps['temperature-to-humidity']
    humidity_to_location_map = maps['humidity-to-location']
    
    soil = convert(seed, seed_to_soil_map)
    fertilizer = convert(soil, soil_to_fertilizer_map)
    water = convert(fertilizer, fertilizer_to_water_map)
    light = convert(water, water_to_light_map)
    temperature = convert(light, light_to_temperature_map)
    humidity = convert(temperature, temperature_to_humidity_map)
    location = convert(humidity, humidity_to_location_map)
    return location


def main():
    file_path = 'input.txt' 
    seeds, maps = parse_input(file_path)
    
    locations = [find_location(seed, maps) for seed in seeds]
    lowest_location = min(locations)
    
    print(lowest_location)


if __name__ == '__main__':
    main()

