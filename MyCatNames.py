myCats = []

while True:
    print('Enter the name of the cat number ' + str(len(myCats) + 1) + 'Or enter nothing to stop.')

    catName = input()

    if catName == '':
        break

    myCats = myCats + [catName]

print('My cats are: ')

for cat in myCats:
    print(cat)

