#
# header comment!
#
import sqlite3
import objecttier


def Command1(dbConn):
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): \n")

    lobbyists = objecttier.get_lobbyists(dbConn, name)

    print("\nNumber of lobbyists found: {}\n".format(len(lobbyists)))

    if len(lobbyists) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...\n")
        return
    
    for lobbyist in lobbyists:
        print("{} : {} {} Phone: {}".format(lobbyist.Lobbyist_ID, lobbyist.First_Name, lobbyist.Last_Name, lobbyist.Phone)) 
    

##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')

# print("Please enter a command (1-5, x to exit): ")
# print("**Error, unknown command, try again...")

dbConn = sqlite3.connect('Chicago_Lobbyists.db')

# garbage - for testing
print("Number of Lobbyists: {}".format(objecttier.num_lobbyists(dbConn)))
print("Number of Employers: {}".format(objecttier.num_employers(dbConn)))
print("Number of Clients: {}".format(objecttier.num_clients(dbConn)))

print()

Command1(dbConn)

# end of garbage

#
# done
#