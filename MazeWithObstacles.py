def PrintingPathsInMaze(maze,r,c,path):
    if r == len(maze[0]) - 1 and c == len(maze) - 1:
        print(path)
        return

    if maze[r][c] == 1:
        return
    
    if r < len(maze[0]) - 1 and c < len(maze) - 1:
        PrintingPathsInMaze(maze, r + 1, c + 1,path + 'D')
    if r < len(maze) - 1:
        PrintingPathsInMaze(maze, r + 1, c, path + 'V')
    if c < len(maze[0]) - 1:
        PrintingPathsInMaze(maze, r, c + 1, path + 'H')




maze = [[0,0,0],[0,1,0],[0,0,0]]
PrintingPathsInMaze(maze,0,0,'')