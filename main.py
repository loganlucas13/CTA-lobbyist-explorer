#
# Logan Lucas
# Project 2
# CS 341
# Spring 2024
#
import sqlite3
import objecttier


# brief: prints basic stats (# of lobbyists, employers, and clients)
# param: dbConn - database connection
# return: none
def printStats(dbConn):
    print("General Statistics:")
    print("  Number of Lobbyists: {:,}".format(objecttier.num_lobbyists(dbConn)))
    print("  Number of Employers: {:,}".format(objecttier.num_employers(dbConn)))
    print("  Number of Clients: {:,}\n".format(objecttier.num_clients(dbConn)))


# brief: displays lobbyist details based on name; max of 100 lobbyists shown
# param: dbConn - database connection
# return: none
def Command1(dbConn):
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): \n")

    lobbyists = objecttier.get_lobbyists(dbConn, name)

    print("\nNumber of lobbyists found: {}\n".format(len(lobbyists)))

    if len(lobbyists) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...\n")
        return
    
    for lobbyist in lobbyists:
        print("{} : {} {} Phone: {}".format(lobbyist.Lobbyist_ID, lobbyist.First_Name, lobbyist.Last_Name, lobbyist.Phone)) 
    print()


# brief: prints a single lobbyist's details based on ID
# param: dbConn - database connection
# return: none
def Command2(dbConn):
    id = input("Enter Lobbyist ID: \n")

    lobbyist = objecttier.get_lobbyist_details(dbConn, id)

    if lobbyist == None:
        print("No lobbyist with that ID was found.\n")
        return
    
    print("{} :".format(lobbyist.Lobbyist_ID))
    print("  Full Name: {} {} {} {} {}".format(lobbyist.Salutation, lobbyist.First_Name, lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix))
    print("  Address: {} {} , {} , {} {} {}".format(lobbyist.Address_1, lobbyist.Address_2, lobbyist.City, lobbyist.State_Initial, lobbyist.Zip_Code, lobbyist.Country))
    print("  Email: {}".format(lobbyist.Email))
    print("  Phone: {}".format(lobbyist.Phone))
    print("  Fax: {}".format(lobbyist.Fax))
    print("  Years Registered: {}".format(', '.join(map(str, lobbyist.Years_Registered)) + ',')) # formats correct output of years
    print("  Employers: {}".format(', '.join(lobbyist.Employers) + ','))
    print("  Total Compensation: ${:,.2f}\n".format(lobbyist.Total_Compensation))


# brief: prints the lobbyist details of a specified number (N) of lobbyists ordered by compensation in a given year
# param: dbConn - database connection
# return: none
def Command3(dbConn):
    N = int(input("Enter the value of N: "))

    if (N <= 0):
        print("Please enter a positive value for N...")
        return
    
    year = input("Enter the year: ")
    print()

    topLobbyists = objecttier.get_top_N_lobbyists(dbConn, N, year)

    count = 1
    for lobbyist in topLobbyists:
        print("{} . {} {}".format(count, lobbyist.First_Name, lobbyist.Last_Name))
        print("  Phone: {}".format(lobbyist.Phone))
        print("  Total Compensation: ${:,.2f}".format(lobbyist.Total_Compensation))
        print("  Clients: {}".format(', '.join(lobbyist.Clients) + ','))
        count += 1

        if count == N+1:
            break


# brief: adds a year to a lobbyist's data given an ID
# param: dbConn - database connection
# return: none
def Command4(dbConn):
    year = input("Enter year: ")
    id = input("Enter the lobbyist ID: ")

    status = objecttier.add_lobbyist_year(dbConn, id, year)
    print()

    if status <= 0:
        print("No lobbyist with that ID was found.")
        return
    
    print("Lobbyist successfully registered.")


# brief: sets the salutation for a lobbyist given their ID
# param: dbConn - database connection
# return: none
def Command5(dbConn):
    id = input("Enter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")

    status = objecttier.set_salutation(dbConn, id, salutation)
    print()

    if status <= 0:
        print("No lobbyist with that ID was found.")
        return
    
    print("Salutation successfully set.")


##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')

dbConn = sqlite3.connect('Chicago_Lobbyists.db')

printStats(dbConn)

command = input("Please enter a command (1-5, x to exit): \n")

while command != 'x':
    match command:
        case '1':
            Command1(dbConn)
        case '2':
            Command2(dbConn)
        case '3':
            Command3(dbConn)
        case '4':
            Command4(dbConn)
        case '5':
            Command5(dbConn)
        case _:
            print("**Error, unknown command, try again...")
    
    command = input("Please enter a command (1-5, x to exit): \n")


# end of garbage

#
# done
#