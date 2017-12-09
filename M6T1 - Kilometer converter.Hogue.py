# CTI 110
# M6T1: Kilometer converter
# Brandon Hogue
# 10/25

# Conversion formula: Miles = Kilometers * 0.6214
Conversion_Factor = 0.6214
    





def main():
    kilometers = float(input('Enter a distane in kilometers: '))
    show_miles(kilometers)

    


def show_miles(km):
    miles = km * Conversion_Factor
    # Display miles.
    print(km, 'kilometers equals', miles, 'miles.')


main()
