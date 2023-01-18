import sys
import os
import io


def func1(a):
    s = sys.stdout.write(input())
    return s


if __name__ == "__main__":
    try:
        data = input()
        b = func1(data)
    except ValueError as error:
        print(False)
