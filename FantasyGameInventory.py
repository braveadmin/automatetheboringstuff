# Fantasy Game Inventory

# https://automatetheboringstuff.com/2e/chapter5/

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):

    print("Inventory: \n")

    item_total = 0

    for k, v in inventory.items():

        print(str(v) + ' ' + str(k))

        item_total = item_total + v

    print("\nTotal number of items: " + str(item_total))


def addToInventory(inventory, addedItems):

    for item in addedItems:

        if item in inventory.keys():

            inventory[item] += 1

        else:

            inventory.setdefault(item, 1)


addToInventory(inv, dragonLoot)

displayInventory(inv)