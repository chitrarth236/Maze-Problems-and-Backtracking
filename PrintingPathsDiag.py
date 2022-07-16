# printing paths in maze, where operations are Diagonal, Horizontal, Vertical

def printPaths(path,r,c):
    if r == 1 and c == 1:
        print(path)
        return
    
    if r > 1 and c > 1:
        printPaths(path + 'D', r - 1, c - 1)
    if r > 1:
        printPaths(path + 'V', r - 1, c)
    if c > 1:
        printPaths(path + 'H', r, c - 1)
    
print(printPaths('',3,3))