import pyautogui
import itertools

x, y = (1247, 846)  # Top left tile position
x_offset, y_offset = 225, 150  # Spacing between tiles
tile_numbers = 3  # Number of tile rows

tiles = []

for tile_x in range(3):
    for tile_y in range(tile_numbers):
        tiles.append((x + (tile_x * x_offset), y + (tile_y * y_offset)))

combinations = itertools.combinations(tiles, 3)
combinations = list(combinations)
combinations_count = len(list(reversed(combinations)))

for combination in combinations:
    combinations_count -= 1
    print(f"{combinations_count} combinations left...")
    for tile in combination:
        pyautogui.click(tile)
