####################################################
#  LAB 3
#
#  This is a pseudo student records database.
#  It has 4 functions: Add student, delete student,
#  find student (ID#), reverse lookup (lastname,
#  firstname) and a quit function that will save 
#  the database to a file for later use.
#
#  Author: Blake Ianni (bianni@kent.edu)
# Version: 1.2
#    Date: 12/5/13
#
####################################################

#We need the pickle module to save our
#student roster to disk.
import pickle

try:
    dbfile = open('abcd.db','r')
    students = pickle.load(dbfile)
    dbfile.close()
except:
    students = {}

def add_student():
    print("\n---------------------------------------")
    print("\n---------- Add Student Portal ---------\n")
    print("---------------------------------------")
    print("\nPlease follow the on screen prompts to enter a new student record.")
    #Lastname, Firstname
    name = raw_input("Enter student's name (Lastname, Firstname): ")
    #ID Number
    idnum = raw_input("Enter student's id: ")
    #D.O.B.
    dob = raw_input("Enter student's Date of Birth (mm/dd/yyyy): ")

    students[idnum] = { 'Name':name, 'DOB':dob }
    

def delete_student():
    idnum = raw_input("Delete which student: ")
    del students[idnum]

def find_student():
    idnum = raw_input("Find which student: ")
    print "\nID : " , idnum
    for record in students[idnum]:
        print record, ":" , students[idnum][record]

def reverse_lookup():
    name = raw_input("Which student are we looking up? (Lastname, Firstname)")
    for idnum in students:
        check = name in students
        print check
        if students[idnum] == name:
            return idnum
        else:
            print "There isn't a record for the name queried"
            
    
menu = {}
menu['1'] = "Add student."
menu['2'] = "Delete student."
menu['3'] = "Find student by Id Number"
menu['4'] = "Reverse Look Up by Name"
menu['5'] = 'Exit'

while True:
    print "\n------------------------------"
    print "Hello, welcome back professor."
    print "\n"
    print "What are we going to do? Please choose the corresponding number."
    options = menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("Please select: ")
    if selection == '1':
        add_student()
    elif selection == '2':
        delete_student()
    elif selection == '3':
        find_student()
    elif selection =='4':
        reverse_lookup()
    elif selection == '5':
        print "Goodbye."
        break
    else:
        print "Unknown option selected!"

try:
    dbfile = open('abcd.db', 'w')
    pickle.dump(students, dbfile)
    dbfile.close()
except Exception, e:
    print "Sorry, an error occurred, all your hard work was not saved!"
    print str(e)

#Copypasta trap
import sys
sys.exit()
x = 5
if x is 5:
    print "We're Done!"
# And that's it, we're done.
