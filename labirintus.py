import random
from colorama import init
from colorama import Fore

def printMaze(maze):

    # colorama
    init()

    # for i in range(0, height):
    #     for j in range(0, width):
    #         print((i, j), end=" ")
    #     print('\n')

    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == wall):
                print(Fore.GREEN + str(maze[i][j]), end=" ")
            elif (maze[i][j] == "2"):
                print(Fore.LIGHTCYAN_EX + str(maze[i][j]), end=" ")
            elif (maze[i][j] == "3"):
                print(Fore.BLUE + str(maze[i][j]), end=" ")
            else:
                print(Fore.RED + str(maze[i][j]), end=" ")

        print('\n')


# Környező mezők száma:
def surroundingCells(rand_wall, wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == wall):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == wall):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == wall):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == wall):
        s_cells += 1

    return s_cells

def delete_wall(rand_wall, walls):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

def mainFunctionGenerateLab(wall, cell, unvisited, height, width, maze):

    # üres labirintus létrehozása:
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # random tér kiválasztása:
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height - 1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width - 1):
        starting_width -= 1

    # random tér leellenőrizve: mezővé alakítás, 'befalazás'
    maze[starting_height][starting_width] = cell

    walls = []
    walls.append([starting_height - 1, starting_width])     #fenti
    maze[starting_height - 1][starting_width] = wall

    walls.append([starting_height, starting_width - 1])     #bal
    maze[starting_height][starting_width - 1] = wall

    walls.append([starting_height, starting_width + 1])     #jobb
    maze[starting_height][starting_width + 1] = wall

    walls.append([starting_height + 1, starting_width])     #lenti
    maze[starting_height + 1][starting_width] = wall

    while (walls):
        # véletlen fal kiválasztása:
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Bal
        if rand_wall[1] != 0:
            # print(rand_wall)
            if (maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == cell):

                # környező mezők kigyűjtése:
                s_cells = surroundingCells(rand_wall, wall)

                if s_cells < 2:
                    # minden feltételnek megfelel: mezővé alakítás
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Új falak
                    # Felső mező
                    if rand_wall[0] != 0:
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Alsó mező
                    if rand_wall[0] != height - 1:
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Legbaloldalibb mező
                    if rand_wall[1] != 0:
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Felhasznált fal törlése:
                delete_wall(rand_wall, walls)

                continue

        # Felső
        if rand_wall[0] != 0:
            if (maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall, wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Felső mező
                    if rand_wall[0] != 0:
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Legbaloldalibb mező
                    if rand_wall[1] != 0:
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Legjobboldalibb mező
                    if rand_wall[1] != width - 1:
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                delete_wall(rand_wall, walls)

                continue

        # Alsó
        if rand_wall[0] != height - 1:
            if (maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall, wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    if rand_wall[0] != height - 1:
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[1] != 0:
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if rand_wall[1] != width - 1:
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                delete_wall(rand_wall, walls)

                continue

        # Jobb
        if rand_wall[1] != width - 1:
            if (maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == cell):

                s_cells = surroundingCells(rand_wall, wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    if rand_wall[1] != width - 1:
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if rand_wall[0] != height - 1:
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[0] != 0:
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # falak kitörlése
                delete_wall(rand_wall, walls)

                continue

        # Falak kitörlése a listából
        for wal in walls:
            if (wal[0] == rand_wall[0] and wal[1] == rand_wall[1]):
                walls.remove(wal)

    # maradék érintetlen blokk fallá alakítása:
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = wall

    # start megjelölése
    for i in range(0, width):
        if (maze[1][i] == wall):
            maze[0][i] = '3'
            break
    # end megjelölése
    for i in range(width - 1, 0, -1):
        if (maze[height - 2][i] == wall):
            maze[height - 1][i] = '2'
            break

    printMaze(maze)


# MAIN
wall = '0'
cell = '1'
unvisited = 'u'
height = 20
width = 20
maze = []

mainFunctionGenerateLab(wall, cell, unvisited, height, width, maze)



