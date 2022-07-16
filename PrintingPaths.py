# printing paths in maze, where operations are one step horizontal, and one step vertical

def printPaths(path,r,c):
    if r == 1 and c == 1:
        print(path)
        return
        
    if r > 1:
        printPaths(path + 'V', r - 1, c)
    if c > 1:
        printPaths(path + 'H', r, c - 1)
    
print(printPaths('',3,3))