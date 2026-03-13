def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                
                # Kiểm tra ô phía trên
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                
                # Kiểm tra ô bên trái
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
                    
    return perimeter