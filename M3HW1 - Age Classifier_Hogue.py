# CTI-110
# M3HW1 - Age Classifier
# Brandon 
# 9/24



def main():
    
    # Program should display whether the person is an infant, a child, a teenager, or an adult

    P_infant = 1
    P_child = 13
    P_teenager = 19
    P_adult = 20


    person = int(input('Enter age of person: '))

    if person <= P_infant:
        print('Your age classifition is: infant')
    else:
        if person <= P_child:
            print('Your age classifition is: child')
        else:
            if person <= P_teenager:
                print('Your age classifition is: teenager')
            else:
                if person >= P_adult:
                    print('Your age classifition is: adult')




main()
