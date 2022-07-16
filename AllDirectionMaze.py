def display(maze):
    for row in maze:
        print(row)


def AllDirectionMaze(path, r, c, maze, count):

    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        maze[r][c] = count
        display(maze)
        print(path)
        print()
        return 

    if maze[r][c] != 0:
        return

    maze[r][c] = count

    if r > 0:
        AllDirectionMaze(path + 'U', r - 1, c, maze, count + 1)
    if c > 0:
        AllDirectionMaze(path + 'L', r, c - 1, maze, count + 1)
    if c < len(maze[0]) - 1:
        AllDirectionMaze(path + 'R', r, c + 1, maze, count + 1)
    if r < len(maze) - 1:
        AllDirectionMaze(path + 'D', r + 1, c, maze, count + 1)

    maze[r][c] = 0

maze = [[0,0,0],[0,0,0],[0,0,0]]
AllDirectionMaze('',0,0,maze,1)
    

