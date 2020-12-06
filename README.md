This is a command line utility which will mimic the functionality of a point of sale restaurant system using basic Python tools 

**Feature Tasks and Requirements**

1. When run, the program should print an intro message and the menu for the restaurant
2. The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
3. The program should prompt the user for an order
4. When a user enters an item, the program should print an acknowledgment of their input
5. The program should tell the user how to exit
6. The program’s content should match included sample exactly
7. Actually, there’s one tiny spot that should be different - see if you can spot it.
8. The > character represents user input line and should be printed out with a trailing space.

```
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
Entering an order
***********************************
** What would you like to order? **
***********************************
> Wings

** 1 order of Wings have been added to your meal **

> Wings

** 2 orders of Wings have been added to your meal **
```

Exiting

`> quit`

**Stretch Goals**

1. Print out a summary of complete order.
2. Only allow ordering items on the menu.
3. Allow ordering items not on menu but give custom reply.

**Configuration**

Poetry was used to create snakes-cafe project and the program is run by typing  `snakes_cafe.py` in the command line

**Version Changes**

1.0 -- 5 Dec: set up files on VSCode and Github; initiated README.md; setup and initial push to GitHub (on master branch--oops); switch to feature