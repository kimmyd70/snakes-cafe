## **Snakes Cafe**
___________

Submission pull request: https://github.com/kimmyd70/snakes-cafe/pull/3

__________
#### Developer: Kim Damalas
#### Created: 5 December 2020
#### Version 1.0 
#### Class: seattle-py-401n2
___________

This is a command line utility which will mimic the functionality of a point of sale restaurant system using basic Python tools 
____________
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
```
9. Entering an order:
```
***********************************
** What would you like to order? **
***********************************
> Wings

** 1 order of Wings have been added to your meal **

> Wings

** 2 orders of Wings have been added to your meal **
```

10. Exiting:  `> quit`
_____________

**Stretch Goals**

1. Print out a summary of complete order.
2. Only allow ordering items on the menu.
3. Allow ordering items not on menu but give custom reply.

**!! NOTE:**

 I did not attempt these after I had MVP working
_____________
**Configuration and Technologies**

The user must have Python and all associated dependencies installed.  Poetry was used to create snakes-cafe project and the program is run by typing  `snakes_cafe.py` in the command line
___________
**Changes**

5 Dec: set up files on VSCode and Github; initiated README.md; setup and initial push to GitHub (on master branch--oops); switch to feature branch `menu` for proof of life and continued coding; proof of life achieved!

6 Dec: updated `README.md`; coded, tested, troubleshooted `snakes_cafe.py`; submitted PR for grading
____________

Features #7 says "one tiny spot that should be different - see if you can spot it. 

A:  in the Welcome Block, "**" is missing from the end of line 4, so I added it.

**!! NOTE:**

  I also changed the improper grammar on `first`  order confirmation (has vs have)
______________
**Enhanced User Experience**

(Possible Self-imposed Stretch Goal)

 I decided a better user experience is to insert "Would you like anything else?" before ordering a subsequent items vs presenting a ">" with no context.

 **!! NOTE:**
 
   I did not code this because the intent of the lab is to match the given format EXACTLY