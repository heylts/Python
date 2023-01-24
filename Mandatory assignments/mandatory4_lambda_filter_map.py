'''
LAMBDA FILTER MAP

LAMBDA_FILTER_MAP_REDUCE

 

Do the following operations on the list l1 with 10 elements.

 

1. Increment all the elements of the list by 1

2. Extract the elements that are greater than 4 after incrementation.

3. Print the sum of all the elements that are greater than 4.

 

Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

1
2
3
4
5
6
7
8
9
10
Sample Output

56
'''

#CODE STUB

from functools import reduce
l1=[]
for i in range(0,10):
    l1.append(int(input()))

# write your code here
def modify_list(l1):
    # Use map to increment all elements by 1
    l1 = list(map(lambda x: x + 1, l1))
    # Use filter to extract elements greater than 4
    l1 = list(filter(lambda x: x > 4, l1))
    # Use reduce to calculate the sum of the elements
    return reduce(lambda x, y: x + y, l1)

#l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(modify_list(l1))
