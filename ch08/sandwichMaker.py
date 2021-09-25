#!/usr/bin/env python3
# sandwichMaker.py

'''
1. Ask for bread type
2. Ask for protein type
3. Ask for cheese
    3a. Ask for cheese type
4. Ask for mayo, mustard, lettuce or tomato
5. How many sandwiches. Min 1
'''
from __future__ import with_statement
import pyinputplus as pyip

# Price list
price = {'wheat': 0.50, 'white': 0.53, 'sourdough': 0.55,
         'chicken': 0.90, 'turkey': 0.95, 'ham': 1.00, 'tofu': 0.85,
         'cheddar': 0.45, 'Swiss': 0.50, 'mozzarella': 0.55,
         'mayo': 0.03, 'mustard': 0.03, 'lettuce': 0.03, 'tomato': 0.03}

totalCost = 0 # Total cost starts at 0

# Choosing bread
promptBread = 'What kind of bread would you like?\n'
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                       promptBread, numbered=True)
totalCost += price[bread]

# Choosing protein
promptProtein = 'What kind of protein would you like?\n'
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                         promptProtein, numbered=True)
totalCost += price[protein]

# Choosing cheese
promptCheese = 'Would you like cheese with that?\n'
withCheese = pyip.inputYesNo(promptCheese)
if withCheese == 'yes':
    promptCheeseType = 'What kind of cheese would you like?\n'
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                            promptCheeseType, numbered=True)
    totalCost += price[cheese]

# Condiments
promptMayo = 'Would you like mayo with that?\n'
withMayo = pyip.inputYesNo(promptMayo)
if withMayo:
    totalCost += price['mayo']
promptMustard = 'Would you like mustard with that?\n'
withMustard = pyip.inputYesNo(promptMustard)
if withMustard:
    totalCost += price['mustard']
promptLettuce = 'Would you like lettuce with that?\n'
withLettuce = pyip.inputYesNo(promptLettuce)
if withLettuce:
    totalCost += price['lettuce']
promptTomato = 'Would you like tomato with that?\n'
withTomato = pyip.inputYesNo(promptTomato)
if withTomato:
    totalCost += price['tomato']

# Quantity
promptQty = 'How many sandwiches would you like?\n'
quantity = pyip.inputInt(promptQty, min=1)
totalCost *= quantity

print(f'The {quantity} burgers cost a total of ${totalCost:.2f}')