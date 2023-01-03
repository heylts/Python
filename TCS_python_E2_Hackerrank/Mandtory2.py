import ast

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
    square_nums = list(map(lambda x: x ** 2, list1))
    cube_nums = list(map(lambda x: x ** 3, list1))
    
    if (x in square_nums and cube_nums for x in list2):
        return "Squares and Cubes are present"
    
    if all(x in square_nums for x in list2):
        return "Squares are only present"

    if any(x in cube_nums for x in list2):
        return "Cubes are only present"

    elif (x not in square_nums and cube_nums for x in list2):
        return "No such pattern is present"
    
    


'''
Write the function armstrong which takes two numbers(num1,num2) as input. Function should return the list of armstrong numbers between num1 and num2

Example : [0,1,..]
'''

def armstrong(num1, num2):
    rtrn = [] #creating empty string to store the new list
    n = len(str(num2)) 
    for j in range(num1, num2):
        i = j
        cube_sum = 0 #setting initial number
        while i != 0:
            k = i % 10
            cube_sum += k ** n
            i = i // 10
        if cube_sum == j:
            rtrn.append(j)
    return rtrn



'''
Write the function string_oper which takes a string as input and return another string after removing words that have characters repeated

Input : "This is an example"
Output : "This is an"
'''
def string_oper(string1):
    new_line =  " ".join(word for word in string1.split() if len(set(word)) == len(word))
    return new_line




'''
Write a function string_reverse which takes a string as input and return another string with each word in reversed order.

Example : "START OF THE PROJECT"
Output :  "TRATS FO EHT TCEJORP"
'''
def string_reverse(sentence):
    rev_letters = ' '.join(word[::-1] for word in sentence.split(" "))
    return rev_letters










if __name__=='__main__':
    list1 = ast.literal_eval(input())
    list2 = ast.literal_eval(input())
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    string1 = input()
    string2 = input()
    print(list_oper(list1,list2))
    print(armstrong(num1,num2))
    print(string_oper(string1))
    print(string_reverse(string2))