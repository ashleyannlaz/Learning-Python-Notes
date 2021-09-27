# Conditional example statements
#
#

def main():
    x, y = 1000, 100
    # conditional flow uses if, elif, else
    # no option for switch case with python
    # if (x < y):
    #     st = "x is less than y"
    # elif(x == y):
    #     st = "x is the same as y"
    # else:
    #     st = "x is more than y"

    # conditional statements let you use "a if C else b"
    # kind of like a js ternary statement
    st = "x is less than y" if (x<y) else "x is greater than y"
    print(st)


main()