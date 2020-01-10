from Utils.texture import Texture

class GameField(object):
    def __init__(self):
        self.road = []
        self.enemies = []
        self.turns = []

        self.images_path = [
            "../res/res/GFX/Game/Tilemap/Spawner/EnemyHouse.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_doc.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_ngang.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_turn12.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_turn14.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_turn23.png",
            "../res/res/GFX/Game/Tilemap/Road/Road_turn34.png",
            "../res/res/GFX/Game/Tilemap/Target/Target.png"
        ]

        self.init_road("mapInfo.txt")

    def init_road(self, path):
        with open(path, "r") as f:
            data, grid = f.readlines(), []
            for line in data:
                row = []
                for item in line.split():
                    row.append(item)
                grid.append(row)

            for line in grid:
                print(line)

            for row, line in enumerate(grid):
                for col, item in enumerate(line):
                    if item == "0":
                        pass
                    elif item == "9":
                        self.road.append(Texture(self.images_path[0], col * 48, (len(grid) - row + 2) * 48))
                    elif item == "8":
                        self.road.append(Texture(self.images_path[-1], col * 48, (len(grid) - row + 2) * 48))
                    else:
                        bit_mask = 0
                        direction = ((0, -1), (-1, 0), (0, 1), (1, 0))
                        print(row, col)
                        for index, direc in enumerate(direction):
                            if 0 <= row + direc[0] < len(grid) and 0 <= col + direc[1] < len(grid[0]):
                                print("in")
                                if grid[row + direc[0]][col + direc[1]] == "1":
                                    bit_mask += 1 << index
                        if bit_mask == 3:
                            self.road.append(Texture(self.images_path[3], col * 48, (len(grid) - row + 2) * 48))
                        elif bit_mask == 9:
                            self.road.append(Texture(self.images_path[4], col * 48, (len(grid) - row + 2) * 48))
                        elif bit_mask == 6:
                            self.road.append(Texture(self.images_path[5], col * 48, (len(grid) - row + 2) * 48))
                        elif bit_mask == 12:
                            self.road.append(Texture(self.images_path[6], col * 48, (len(grid) - row + 2) * 48))
                        elif bit_mask == 10:
                            self.road.append(Texture(self.images_path[1], col * 48, (len(grid) - row + 2) * 48))
                        else:
                            self.road.append(Texture(self.images_path[2], col * 48, (len(grid) - row + 2) * 48))

        pass

    def draw_entities(self):
        for item in self.road:
            item.draw()

        for item in self.enemies:
            item.draw()
