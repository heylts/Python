import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Write the function list_oper that takes two list as input.

Function should return a string after performing the operations specified below
 - Check for the squares and cubes of elements in list1 is present in list2
 - Return "Squares and Cubes are present" if squares and cubes of all elements in list1 are present in list2.
 - Return "Squares are only present" if squares of all elements in list1 are only present in list2.
 - Return "Cubes are only present" if cubes of all the elements in list1 are only present in list2.
 - Return "No such pattern is present" if there are squares and cubes of any element in list1 is not present in list2
'''
def list_oper(list1, list2):
    squares_only = True
    cubes_only = True
    for element in list1:
        if element ** 2 not in list2:
            squares_only = False
        if element ** 3 not in list2:
            cubes_only = False
    if squares_only and cubes_only:
        return "Squares and Cubes are present"
    elif squares_only:
        return "Squares are only present"
    elif cubes_only:
        return "Cubes are only present"
    else:
        return "No such pattern is present"


'''
Write the function armstrong which takes two numbers(num1,num2) as input. Function should return the list of armstrong numbers between num1 and num2

Example : [0,1,..]
'''
def armstrong(num1, num2):
    armstrong_numbers = []
    for i in range(num1, num2 + 1):
        # Convert the number to a string and get the length
        str_i = str(i)
        length = len(str_i)
        # Calculate the sum of the digits to the power of the length
        sum = 0
        for digit in str_i:
            sum += int(digit) ** length
        # If the sum is equal to the original number, it is an Armstrong number
        if sum == i:
            armstrong_numbers.append(i)
    return armstrong_numbers


'''
Write the function string_oper which takes a string as input and return another string after removing words that have characters repeated

Input : "This is an example"
Output : "This is an"
'''
def string_oper(string1):
    new_line = " ".join(word for word in string1.split() if len(set(word)) == len(word))
    return new_line


'''
Write a function string_reverse which takes a string as input and return another string with each word in reversed order.

Example : "START OF THE PROJECT"
Output :  "TRATS FO EHT TCEJORP"
'''
def string_reverse(sentence):
    rev_letters = ' '.join(word[::-1] for word in sentence.split(" "))
    return rev_letters


if __name__ == '__main__':
    list1 = ast.literal_eval(input())
    list2 = ast.literal_eval(input())
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    string1 = input()
    string2 = input()
    print(list_oper(list1, list2))
    print(armstrong(num1, num2))
    print(string_oper(string1))
    print(string_reverse(string2))
