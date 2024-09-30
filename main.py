'''take the input from the user and store it as an integer in year'''
year = int(input("What year Ferrari 250 GTO are you looking at?\n"))

'''takes the previously saved input and determines, through a series of if...elif...else statements,
what the value of the car was during that year'''
if year < 1962:
    print('This is not a valid year')
elif year <= 1964:
    print('The value of the Ferrari 250 GTO in', year, 'was $18,500.')
elif year <= 1968:
    print('The value of the Ferrari 250 GTO in', year, 'was $6,000.')
elif year <= 1971:
    print('The value of the Ferrari 250 GTO in', year, 'was $12,000.')
elif year <= 1975:
    print('The value of the Ferrari 250 GTO in', year, 'was $48,000.')
elif year <= 1980:
    print('The value of the Ferrari 250 GTO in', year, 'was $200,000.')
elif year <= 1985:
    print('The value of the Ferrari 250 GTO in', year, 'was $650,000.')
elif year <= 2012:
    print('The value of the Ferrari 250 GTO in', year, 'was $35,000,000.')
elif year <= 2014:
    print('The value of the Ferrari 250 GTO in', year, 'was $52,000,000.')
else:
    print('This is not a valid year')
