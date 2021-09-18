tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    # Setup the column width
    colWidths = [0] * len(table)
    # Loop throught the lists and find the longest string
    for i in range(len(table)):
        for j in table[i]:
            if colWidths[i] < len(j):
                colWidths[i] = len(j)

    # Make sure the inner lists have the same length
    if all(len(table[i]) == len(table[i + 1]) for i in range(len(table) - 1)):

        # Loop through the lists
        for i in range(len(table[0])):
            for j in range(len(table)):
                print(table[j][i].rjust(colWidths[j]), end=' ')
            print('')  # Break line

    else:
        print('Uneven table')

printTable(tableData)