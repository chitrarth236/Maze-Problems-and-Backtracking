# counting paths in maze:

def countPaths(r,c):
    if r == 1 or c == 1:
        return 1
    
    return countPaths(r, c-1) + countPaths(r-1, c)
    

# Here, I am using 3x3 Maze
print(countPaths(3,3))