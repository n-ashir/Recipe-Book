#start

# import data from Recipe_Data file
from Recipe_Data import *

def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")


def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
        return oldUser()

print('\n Welcome to Recipe Book! \n ') #print 'Welcome'
users = {'guest':'guest'}
status = input('Are you registered user? y/n? or Press g to Continue as a Guest! ')
status = str(status)
if status == "y":
        oldUser()
elif status == "n":
        newUser()
elif status == 'g':
        print('\nPlease enter as a Guest for login name: \'guest\' and  passw: \'guest\'!')
        print('')
        oldUser()


#printing Meal types
print('''Meal Types:
 1.Breakfast and Brunch. 
 2.Desserts.
 3.Dinners.
 4.Lunch. ''')

#inserting Meal Type's number
type_of_m = input("\n Please insert on of the Meal Type\'s number! ",)
type_of_m = int(type_of_m) # converting integer type
print_recipe(type_of_m) # function show us which type of meal recipe is selected!

#printing options
print('''
      for add new recipe: input 1
      for update recipe:  input 2
      for search recipe:   input 3
      for delete recipe:  input 4
      ''')
options = input('Please Input here: ', ) #inputing recipe optin number
options = int(options) # converting input to integer
option(options)
option_step_two(options)

