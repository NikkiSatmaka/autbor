stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    # Print inventory list
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v, k)
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    # Add the number of occurence in addedItems to inventory
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)

# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)