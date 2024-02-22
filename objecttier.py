#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
# Logan Lucas
# Project 2
# CS 341
# Spring 2024
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, id, firstName, lastName, phone):
      self._Lobbyist_ID = id
      self._First_Name = firstName
      self._Last_Name = lastName
      self._Phone = phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property 
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, id, salutation, firstName, middleInitial, lastName, suffix, address1, address2, city, stateInitial, zipCode, country, email, phone, fax, yearsRegistered, employers, totalCompensation):
      self._Lobbyist_ID = id
      self._Salutation = salutation
      self._First_Name = firstName
      self._Middle_Initial = middleInitial
      self._Last_Name = lastName
      self._Suffix = suffix
      self._Address_1 = address1
      self._Address_2 = address2
      self._City = city
      self._State_Initial = stateInitial
      self._Zip_Code = zipCode
      self._Country = country
      self._Email = email
      self._Phone = phone
      self._Fax = fax
      self._Years_Registered = yearsRegistered
      self._Employers = employers
      self._Total_Compensation = totalCompensation
   
   @property
   def Lobbyist_Id(self):
      return self._Lobbyist_ID
   
   @property
   def Salutation(self):
      return self._Salutation
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Middle_Initial(self):
      return self._Middle_Initial
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Suffix(self):
      return self._Suffix
   
   @property
   def Address_1(self):
      return self._Address_1
   
   @property
   def Address_2(self):
      return self._Address_2
   
   @property
   def City(self):
      return self._City
   
   @property
   def State_Initial(self):
      return self._State_Initial
   
   @property
   def Zip_Code(self):
      return self._Zip_Code
   
   @property
   def Country(self):
      return self._Country
   
   @property
   def Email(self):
      return self._Email
   
   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Fax(self):
      return self._Fax
   
   @property
   def Years_Registered(self):
      return self._Years_Registered
   
   @property
   def Employers(self):
      return self._Employers
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, lobbyistId, firstName, lastName, phone, totalCompensation, clients):
      self._Lobbyist_ID = lobbyistId
      self._First_Name = firstName
      self._Last_Name = lastName
      self._Phone = phone
      self._Total_Compensation = totalCompensation
      self._Clients = clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation
   
   @property
   def Clients(self):
      return self._Clients


##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   query = """SELECT count(DISTINCT Lobbyist_ID) AS Num_Lobbyists
   FROM LobbyistInfo"""

   numLobbyists = datatier.select_one_row(dbConn, query)[0]

   # error checking
   if numLobbyists == None:
      return -1
   
   return numLobbyists


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   query = """SELECT count(DISTINCT Employer_ID) AS Num_Employers
   FROM EmployerInfo"""

   numEmployers = datatier.select_one_row(dbConn, query)[0]

   # error checking
   if numEmployers == None:
      return -1
   
   return numEmployers


##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   query = """SELECT count(DISTINCT Client_ID) AS Num_Clients
   FROM ClientInfo"""

   numClients = datatier.select_one_row(dbConn, query)[0]

   #error checking
   if numClients == None:
      return -1
   
   return numClients


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   query = """SELECT Lobbyist_ID, First_Name, Last_Name, Phone
   FROM LobbyistInfo
   WHERE First_Name LIKE ? OR Last_Name LIKE ?
   ORDER BY Lobbyist_ID ASC"""

   parameters = [pattern, pattern]

   results = datatier.select_n_rows(dbConn, query, parameters)

   lobbyists = []

   for result in results:
      lobbyist = Lobbyist(result[0], result[1], result[2], result[3])
      lobbyists.append(lobbyist)
      
   return lobbyists


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   pass
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   pass


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   pass


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   pass