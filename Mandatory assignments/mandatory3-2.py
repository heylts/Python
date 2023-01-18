import calc_module
import calc_module2

def caller_func(inp1, inp2, num, string):
    ans1 = calc_module.mul(inp1, inp2)
    ans2 = calc_module.div(inp1, inp2)
    ans3 = calc_module.even(num)
    ans4 = calc_module2.add(inp1, inp2)
    ans5 = calc_module2.sub(inp1, inp2)
    ans6 = calc_module2.even(string)

    list1 = [ans1, ans2, ans3, ans4, ans5, ans6]
    return list1


if __name__ == '__main__':
    inp1 = 2
    inp2 = 4
    num = 6
    string_inp = "Boot"
    list1 = caller_func(inp1, inp2, num, string_inp)
    fd = open("output.txt", "w")
    for i in list1:
        fd.write(str(i))
        fd.write("\n")


    fd.close()
