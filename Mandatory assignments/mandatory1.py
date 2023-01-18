def pattern(str_):
    #loop through the index of the string
    for i in range(len(str_)):
        if i % 2 == 0: #if the index of the element is even number
            print(" " * (i//2) + str_[i] + str_[i+1]) #generating the pattern


if __name__=='__main__':
    str_ = input()
    pattern(str_)
