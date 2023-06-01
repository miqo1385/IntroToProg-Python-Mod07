# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: create a new script that demonstrates how Pickling and Structured error handling work.
# ChangeLog (Who,When,What):
# MQuintana,5.30.2023,Created script
# <Miguel Quintana>,<05/30/2023>, Assignment 07 Pickling and Structured error
# ---------------------------------------------------------------------------- #

import pickle
# Pickling
#Data
country = input("Country of Origen:  ")
strName = str(input("Enter a Name: "))
lstPeople = [country, strName]
print(lstPeople)


# Processing: in this part of the code we will append and dump
# input from user and we will save it as binary file


# Now we store the data with the pickle.dump method
objFile = open("PeopleData.dat", "ab")
pickle.dump(lstPeople, objFile)
objFile.close()

# And, we read the data back with the pickle.load method

objFile = open("PeopleData.dat", "rb")
objFileData = pickle.load(objFile) #
objFile.close()

print(objFileData)


# Try-Except
# in this part the code i created three Try-Except function

# the first one if in Country of origen the user put a number
#  it will create an Error message.
try:
    country = str(input("Country of Origen:  "))
    if country.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


# the second one will do the same with name input
try:
    strName = str(input("Enter a Name: "))
    if strName.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


# the third one it will create an error message if input comes with blank spaces.
try:
    strName = str(input("Enter a Name: "))
    if strName.isspace():
        raise Exception('Do not use space for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')