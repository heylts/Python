'''
Library

This exception handling scenario deals with the exceptional cases that arise in a typical library interface of a Town library.

 

About the Library Interface

This is a typical interface provided in the library, which takes 3 inputs from the library members, sequentially. They are:

1. memberfee - Membership fee for the library for the next financial year, which can be paid in installments.

2. installment - Number of installments chosen to pay the Membership fee.

3. book - Name of the book the member looks for in the 'Harry Potter' Section.

 

Note

All the above inputs except 'book' are Integers.

 

Write the function definition as follows, for the function 'Library', that takes all the above 3 inputs as its parameters:

 

The maximum permitted number of installments to pay the annual membership fee is '3'.

1. Raise ValueError exception if the input for the number of installments is greater than '3' and Print a Message. The message to the user must be, "Maximum Permitted Number of Installments is 3".

 

The amount per installment is calculated by dividing the Membership fee by the number of installments.

2. Raise ZeroDivisionerror1 exception if the input for the number of installments is equal to '0' and Print a Message. The message to the user must be, "Number of Installments cannot be Zero."

else

Print the amount per installment as "Amount per Installment is 3000.0".

 

The 'Harry Potter' book section contains the following books only:

philosophers stone
chamber of secrets
prisoner of azkaban
goblet of fire
order of phoenix
half blood prince
deathly hallows 1
deathly hallows 2
3. Raise NameError exception if the user is looking for a book other than the books mentioned above and Print a Message. The message to the user must be, "No such book exists in this section"

else

Print "It is available in this section".

 

Note

1. Raise the error exceptions in the same order as above.

2. If any of the exceptions occur, the statements following that should not be executed. 

 

Input Format for Custom Testing

# In the first line, the value for the membership fee

# In the second line, the value for the number of installments

# In the third line, the value for the Name of the book

 

 

Sample Test Case 1

 

Sample Input

STDIN     
-----     
6000
2
Philosophers stone
Sample Output

Amount per Installment is  3000.0
It is available in this section
'''
