# CTI 110
# M6LAB
# Brandon H
# 11/2

P_infant = 1
P_child = 13
P_teenager = 19
P_adult = 20

def main():
    name = input('What is your name? ')
    greet(name)
    #greet('steve')
    #greet('bob')
    #greet('billy')

    age = int(input('What is your age? '))
    print("you are a", ageCategory(age))
    #ageCategory('infant')
    #ageCategory('child')
    #ageCategory('teenager')
    #ageCategory

    

    

    
def greet(name):
    print('Hello there, ', name)


    

def ageCategory(age):
   if age <= P_infant:
        print('Your age category is: infant')
   else:
        if age <= P_child:
            print('Your age category is: child')
        else:
            if age <= P_teenager:
                print('Your age category is: teenager')
            else:
                if age >= P_adult:
                    print('Your age category is: adult')
                    
        return age

    
    
    
    












main()
