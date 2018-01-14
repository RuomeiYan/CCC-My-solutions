def one_line(a,number_list):       # Output one line
    if a in number_list:
        print(" * * * ")
    else:
        print()


def two_row(a,b,number_list):
    if a in number_list and b in number_list:      # Output two row
        for i in range(3):
            print("*     *")
    elif a in number_list:
        for i in range(3):
            print("*")
    else:
        for i in range(3):
            print("      *")


def output(number_list):      # Output a number
    one_line(1,number_list)
    two_row(2,3,number_list)
    one_line(4,number_list)
    two_row(5,6,number_list)
    one_line(7,number_list)

n = int(input())
if n == 0:                  # Output numbers between 0 to 9
    output([1,2,3,5,6,7])
elif n == 1:
    output([3,6])
elif n == 2:
    output([1,3,4,5,7])
elif n == 3:
    output([1,3,4,6,7])
elif n == 4:
    output([2,3,4,6])
elif n == 5:
    output([1,2,4,6,7])
elif n == 6:
    output([1,2,4,5,6,7])
elif n == 7:
    output([1,3,6])
elif n == 8:
    output([1,2,3,4,5,6,7])
else:
    output([1,2,3,4,6,7])