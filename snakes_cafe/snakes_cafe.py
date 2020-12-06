# print welcome block
print('*'*38)
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**                                  **')
print('** To quit at any time, type "quit" **')
print('*'*38)
print()

# print menu items
print('Appetizers')
print('----------')
print('Wings')
print('Cookies')
print('Spring Rolls')
print()

print('Entrees')
print('-------')
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden')
print()

print('Desserts')
print('--------')
print('Ice Cream')
print('Cake')
print('Pie')
print()

print('Drinks')
print('------')
print('Coffee')
print('Tea')
print('Unicorn Tears')
print()

# interpret user input
# loop or quit
user_input = ''
orders = {
        'wings': 0,
    }
while (user_input.lower() != 'quit'):
    wing_order = orders['wings']
    print('*'*35)
    print('** What would you like to order? **')
    print('*'*35)
    user_input = input('> ').lower()
    orders['wings'] += 1

    
    # user input add to order and print confirmation
    if orders['wings'] < 2:
        print()
        print ('** ' + str(orders['wings']) + ' order of Wings has been added to your meal **')
        print()

    # if loop, print (s) on item
    if orders['wings'] >= 2 and user_input.lower() != 'quit':
        print()
        print ('** ' + str(orders['wings']) + ' orders of Wings have been added to your meal **')
        print()







