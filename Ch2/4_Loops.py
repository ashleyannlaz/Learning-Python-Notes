# ##########
# LOOPS
# ##########

def main():
    x=0

    # define a while loop
    # while (x<5):
    #     print(x)
    #     x = x + 1

    # define a for loop
    for x in range(5,10):
        print(x)

    # use a for loop over a collection
    days=["mon","tues","wed","thu", "fri", "sat", "sun"]
    # iterating through each item in the list and printing
    for d in days:
        print(d)
    # use the break and continue statements
    # for x in range(5,10):
        # if(x==7): break
        # if(x % 2 == 0): continue
        # continue go back and start over
        # break if x = 7 stop and move onto next code
        # print(x)
    # using enumerate() to get index
    for i,d in enumerate(days):
        print(i, d)
        # prints out the array, and the index side by side
main()