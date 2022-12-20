def pattern(str_):
    for i in range(len(str_)):
        if i % 2 == 0:
            print(" " * (i//2) + str_[i] + str_[i+1])


if __name__=='__main__':
    str_ = input()
    pattern(str_)