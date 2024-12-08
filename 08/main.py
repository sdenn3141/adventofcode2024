from itertools import combinations
from helpers import read_file
from multiprocessing import Process

class AntiNodeLocator:
    def __init__(self, area, harmonics_enabled):
        self.area = area
        self.nodes = {}
        self.antinodes = []
        self.harmonics_enabled = harmonics_enabled
    
    def locate_nodes(self):
        for i in range(len(self.area)):
            for j in range(len(self.area[i])):
                if self.area[i][j] == '.' or self.area[i][j] == '#':  
                    continue
                self.nodes[self.area[i][j]] = self.nodes.get(self.area[i][j], [])
                self.nodes[self.area[i][j]].append([i, j])
    
    def mark_antinodes(self):
        for key in self.nodes.keys():
            pairs = list(combinations(self.nodes[key], 2))
            for pair in pairs:
                x_gap = pair[1][1] - pair[0][1]
                y_gap = pair[1][0] - pair[0][0]
                if self.harmonics_enabled:
                    new_antinodes = [[pair[0][0] + y_gap * i, pair[0][1] + x_gap * i] for i in range(-len(self.area), len(self.area))]
                else:
                    new_antinodes = [[pair[0][0] + y_gap * 2, pair[0][1] + x_gap * 2],[pair[0][0] - y_gap, pair[0][1] - x_gap]]
                for a in new_antinodes:
                    if a[0] < 0 or a[0] > len(self.area) - 1 or a[1] < 0 or a[1] > len(self.area[0]) - 1:
                        continue
                    else:
                        self.area[a[0]][a[1]] = '#'
        
    def count_antinodes(self):
        total = 0
        for l in self.area:
            total += l.count('#')
        return total

                
def part_one(file_name='08/data.in'):
    area = read_file(file_name)
    char_list = [list(s) for s in area]
    locator = AntiNodeLocator(char_list, False)
    locator.locate_nodes()
    locator.mark_antinodes()
    print(f"Part One: {locator.count_antinodes()}")
    return locator.count_antinodes()


def part_two(file_name='08/data.in'):
    area = read_file(file_name)
    char_list = [list(s) for s in area]
    locator = AntiNodeLocator(char_list, True)
    locator.locate_nodes()
    locator.mark_antinodes()
    print(f"Part Two: {locator.count_antinodes()}")
    return locator.count_antinodes()


if __name__ == "__main__":
    p1 = Process(target=part_one)
    p2 = Process(target=part_two)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done!")