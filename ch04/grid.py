myGrid = [['.', '.', '.', '.', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['.', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.']]

def transpose(grid):
    # Make sure the inner lists have the same length
    if all(len(grid[i]) == len(grid[i + 1]) for i in range(len(grid) - 1)):

        # Loop through the lists
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                print(grid[j][i], end='')
            print('')  # Break line

    else:
        print('Uneven grid')

transpose(myGrid)