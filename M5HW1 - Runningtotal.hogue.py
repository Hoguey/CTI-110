# CTI 110
# Distanced Traveled
# Brandon H
# 10/27



def main():


    runningTotal = 0
    # number = int(input())
    # print('Enter a number:')


    keepGoing = True
    while keepGoing:
        print('Enter an amount')


    

        number = int(input('> '))
        if number < 0:
            keepGoing = False
        else:
            runningTotal += number
    print('Total is:', runningTotal)


main()



