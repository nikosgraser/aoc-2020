from typing import List


class Tile:
    def __init__(self, tile_id: str, tile_lines: List[str]):
        self.tile_id = tile_id
        self.raw_lines = tile_lines
        self.borders = self.get_borders()

    def get_borders(self):
        return [
            list(self.raw_lines[0]),
            [line[-1] for line in self.raw_lines],
            list(self.raw_lines[-1]),
            [line[0] for line in self.raw_lines],
        ]

    def has_border(self, other_border: List[str]):
        return any(
            own_border == other_border or own_border == list(reversed(other_border))
            for own_border in self.borders
        )


ALL_TILES: List[Tile] = []
with open('input', 'r') as fd:
    lines = [line.strip() for line in fd.readlines()]

new_tile_id = None
new_tile_lines = []
for line in lines:
    if line.endswith(':'):
        new_tile_id = line.split()[1][:-1]
    elif len(line) > 0:
        new_tile_lines.append(line)
    else:
        ALL_TILES.append(Tile(new_tile_id, new_tile_lines))
        new_tile_id = None
        new_tile_lines = []
ALL_TILES.append(Tile(new_tile_id, new_tile_lines))

corner_product = 1
for tile in ALL_TILES:
    all_other_tiles = [t for t in ALL_TILES if t.tile_id != tile.tile_id]
    num_outer_borders = sum(
        1 for b in tile.borders
        if not any(other_tile.has_border(b) for other_tile in all_other_tiles)
    )
    if num_outer_borders > 1:
        corner_product *= int(tile.tile_id)
print(corner_product)
