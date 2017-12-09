# CTI 110
# M6T2
# Brandon Hogue
# 11/1


Inches_Per_Foot = 12





def main():
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')



def feet_to_inches(feet):
    return feet * Inches_Per_Foot

main()

    
