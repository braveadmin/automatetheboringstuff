# table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'tenryuubito', 'goose']]

def tablePrinter(tableData):

    colWidths = [0] * len(tableData)

    line = []

    x = 0


    for i in range(len(tableData)):

            for j in range(len(tableData[i])):

                if len(tableData[i][j]) > colWidths[i]:

                    colWidths[i] = len(tableData[i][j])

    for x in range(len(tableData[0])):

        for y in range(len(tableData)):

            print(tableData[y][x].rjust(colWidths[y]), end = ' ' )

        print('')



tablePrinter(tableData)