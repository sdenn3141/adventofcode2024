from helpers import read_file, execute
import json

def look_around(obj, path, target, area):
    x, y = map(int, path.split('X'))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(area) and 0 <= ny < len(area[0]) and area[nx][ny] == target:
            obj[f"{nx}X{ny}"] = {}

def explore(paths, depth, max_depth, area):
    if depth > max_depth:
        return
    for path in list(paths.keys()):
        look_around(paths[path], path, str(depth), area)
        explore(paths[path], depth + 1, max_depth, area)

def collect_max_depth_paths(current_path, current_dict, all_paths, current_depth, max_depth):
    if current_depth == max_depth:
        all_paths.append(current_path)
        return
    for key, nested_dict in current_dict.items():
        new_path = f"{current_path}->{key}"
        collect_max_depth_paths(new_path, nested_dict, all_paths, current_depth + 1, max_depth)

def get_max_depth_paths(paths, max_depth):
    all_paths = []
    for key, nested_dict in paths.items():
        initial_path = key
        collect_max_depth_paths(initial_path, nested_dict, all_paths, current_depth=1, max_depth=max_depth)
    return all_paths  

def part_one(file_name="10/data/10.in"):
    f = read_file(file_name)
    area = [list(s) for s in f]
    paths = {}
    for i in range(len(area)):
        for j in range(len(area[i])):
            if int(area[i][j]) == 0:
                paths[f"{i}X{j}"] = {}
    max_depth = 10
    explore(paths, depth=1, max_depth=max_depth, area=area)
    unique_paths = get_max_depth_paths(paths, 10)
    total = len(set([(p.split("->")[0],p.split("->")[-1]) for p in unique_paths]))
    print(f"Part One: {total}")
    return total


def part_two(file_name="10/data/10.in"):
    f = read_file(file_name)
    area = [list(s) for s in f]
    paths = {}
    for i in range(len(area)):
        for j in range(len(area[i])):
            if int(area[i][j]) == 0:
                paths[f"{i}X{j}"] = {}

    max_depth = 10
    explore(paths, depth=1, max_depth=max_depth, area=area)
    unique_paths = get_max_depth_paths(paths, 10)
    total = len(unique_paths)
    print(f"Part Two: {total}")
    

if __name__ == "__main__":
    execute(part_one, part_two)
