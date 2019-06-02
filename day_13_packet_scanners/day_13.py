from typing import List, Set

DOWN = "down"
UP = "up"


class Layer(object):
    def __init__(self, depth, range, scanner, direction):
        self.depth = depth
        self.range = range
        self.scanner = scanner
        self.direction = direction

    def __repr__(self):
        return "depth: {depth} \n range: {range} \n scanner: {scanner} \n".format(depth=str(self.depth),
                                                                                  range=str(
                                                                                      self.range),
                                                                                  scanner=str(self.scanner))


def parse(input) -> List[Layer]:
    lines = input.strip().split("\n")
    depths_ranges = {}
    for line in lines:
        elements = line.split(":")
        depth = int(elements[0])
        range_f = int(elements[1].strip())
        depths_ranges[depth] = range_f

    max_depth = max(depths_ranges.keys())
    for depth in range(0, max_depth + 1):
        if depth not in depths_ranges:
            depths_ranges[depth] = 0

    return [Layer(depth, depths_ranges[depth], 0, DOWN) for depth in range(0, max_depth + 1)]


def max_depth(layers: List[Layer]) -> int:
    return max([layer.depth for layer in layers])


def update_layers(layers: List[Layer], picosecond: int) -> None:
    for layer in layers:
        if layer.range != 0:
            if layer.scanner == 0 and layer.direction == UP:
                layer.direction = DOWN
                layer.scanner += 1
            elif layer.scanner == layer.range - 1 and layer.direction == DOWN:
                layer.direction = UP
                layer.scanner -= 1
            elif layer.direction == UP:
                layer.scanner -= 1
            else:
                layer.scanner += 1


def is_caught_by_scanner(layer: Layer, current_picosecond: int) -> bool:
    return layer.scanner == 0 and current_picosecond == layer.depth and layer.range != 0


def compute_severity(layers: List[Layer]) -> int:
    total_picoseconds = max_depth(layers)
    severities = []
    for current_picosecond in range(0, total_picoseconds + 1):
        current_layer = layers[current_picosecond]
        if is_caught_by_scanner(current_layer, current_picosecond):
            severities.append(current_layer.depth * current_layer.range)

        update_layers(layers, current_picosecond)

    return sum(severities)


file = open('day13_input.txt')
input = file.read()
layers = parse(input)
print(compute_severity(layers))
