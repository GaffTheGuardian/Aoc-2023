def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    

    seeds = list(map(int, lines[0].strip().split(': ')[1].split()))
    
    maps = []
    current_map = []
    for line in lines[1:]:
        line = line.strip()
        if line.endswith('map:'):
            if current_map:
                maps.append(current_map)
            current_map = []
        elif line:
            current_map.append(tuple(map(int, line.split())))
    
    if current_map:
        maps.append(current_map)

    return seeds, maps


def convert(number, conversion_map):
    for dest_start, src_start, length in conversion_map:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number


def find_location(seed, maps):
    seed_to_soil_map = maps[0]
    soil_to_fertilizer_map = maps[1]
    fertilizer_to_water_map = maps[2]
    water_to_light_map = maps[3]
    light_to_temperature_map = maps[4]
    temperature_to_humidity_map = maps[5]
    humidity_to_location_map = maps[6]
    
    soil = convert(seed, seed_to_soil_map)
    fertilizer = convert(soil, soil_to_fertilizer_map)
    water = convert(fertilizer, fertilizer_to_water_map)
    light = convert(water, water_to_light_map)
    temperature = convert(light, light_to_temperature_map)
    humidity = convert(temperature, temperature_to_humidity_map)
    location = convert(humidity, humidity_to_location_map)
    return location


def apply_mappings(seeds, maps):
    locations = []
    
    for i in range(0, len(seeds), 2):
        start_seed = seeds[i]
        range_length = seeds[i + 1]
        ranges = [[start_seed, start_seed + range_length]]
        results = []
        
        for mapping in maps:
            while ranges:
                start_range, end_range = ranges.pop(0)
                
                for target, start_map, length in mapping:
                    end_map = start_map + length
                    offset = target - start_map
                    
                    if end_map <= start_range or end_range <= start_map:
                        continue
                    
                    if start_range < start_map:
                        ranges.append([start_range, start_map])
                        start_range = start_map
                    if end_map < end_range:
                        ranges.append([end_map, end_range])
                        end_range = end_map
                    
                    results.append([start_range + offset, end_range + offset])
                    break
                else:
                    results.append([start_range, end_range])
            
            ranges = results
            results = []
        
        locations.extend(ranges)
    
    return min(loc[0] for loc in locations)


def main():
    file_path = 'input.txt'
    seeds, maps = parse_input(file_path)
    
   
    locations = [find_location(seed, maps) for seed in seeds]
    lowest_location_part1 = min(locations)
    
   
    lowest_location_part2 = apply_mappings(seeds, maps)
    
    print("Part 1: Lowest Location Number:", lowest_location_part1)
    print("Part 2: Lowest Location Number:", lowest_location_part2)


if __name__ == '__main__':
    main()
