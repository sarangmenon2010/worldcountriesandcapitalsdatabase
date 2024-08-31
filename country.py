countries = {}

while True:
    print("1 - Add")
    print("2 - Display All Countries")
    print("3 - Display All Capitals")
    print("4 - Delete")
    print("5 - Get Capital")
    choice = int(input("Enter your choice from 1-5 "))
    if choice == 1:
        c = input("Enter country name ")
        l = input("Enter capital name ")
        countries [c] = l
    elif choice == 2:
        print(countries.keys())
    elif choice == 3:
        print(countries.values())
    elif choice == 4:
        country = input("Enter country name that you wish to delete ")
        countries.pop(country)
        print(countries)
    elif choice == 5:
        country = input("Enter country name that you wish to get the capital ")
        print(countries[country])
    else:
        break





