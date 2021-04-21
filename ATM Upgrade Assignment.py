# Register

# - first name, last name, email, password
# - Genrate user account

# Login
# - Account number and password


# Bank operations 

import random       # This imports random numbers and will be used to generate the account number for the user
database = {}       # A blank dictionary acting as database

def init():             # This function initializes the system 
    
    isValidOptionSelected = False       # Variable for the While Loop
    print("Welcome to AkaraOgun Merchant Bank")
    
    while isValidOptionSelected == False:   # This While Loop allows the user retry the login section till they get the select the right option
                    
        accountCheck = int(input("Do you already have an account?: 1 (Yes) 2 (No) \n"))

        if (accountCheck == 1):                 # This conditonal calls the login function below because it means the person already has an account
            isValidOptionSelected = True        # This terminates the While Loop
            login()             
        elif (accountCheck == 2):               # This condiional calls the register function and walks the user through the registration process
            isValidOptionSelected = True
            register()
        else:
            print("You've selected an invalid option")

def login():            #  This is the login function
    print("********** Login **********")

    loginAttempt = False

    while loginAttempt == False:
        
        userAccountNumber = int(input("Please type your account number: \n"))
        password = input("Please type your password: \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == userAccountNumber):         # This checks the account number imputed by the user and makes sure its the same as the one generated during the registration process
                if(userDetails[3] == password):         # This checks the inputed password with the password in the datatbase using it's index position [3]
                    loginAttempt = True
                    print("Login Successful")
                    print("==== ==== ==== ==== ==== ==== ====")
                
                else:
                    print("Invalid account details. Please try again.")

    bankOperation(userDetails)     #  After they have logged in, this function start the bank operations 


def register():         # This is the register function
    print("****** Register *******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create your password: \n")

    accountNumber = generateAccountNumber()         # This sets the random number generated to the account number of the user 
    
    database[accountNumber] = [ first_name, last_name, email, password]      # This stores the user's information into the database 
    
    print("Your account has been created")
    print("==== ==== ==== ==== ==== ==== ====")
    print("This is your account number: %d" % accountNumber)
    print("Please keep it safe")
    print("==== ==== ==== ==== ==== ==== ====")

    login()     # This function call returns the user back to go and login with their new account they just created


def bankOperation(user):       # This is the bank operations function

    print("Welcome %s %s " % (user[0], user[1]))
    
   
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Check Balance (4) Logout (5) Exit \n"))

    if (selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation()

    elif (selectedOption == 3):
        checkBalance()

    elif (selectedOption == 4):
        logout()

    elif (selectedOption == 5): 
        exit()
        
    else:
        print("Invalid option selected")
        bankOperation(user) 
    


def depositOperation():
    print("Deposit Operations")


def withdrawalOperation():
    print("Withdrawal")

def checkBalance():
    print("Checking your balance")

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)      # This returns random numnbers between the set range 
    
def logout():
    login()


### ACTUAL BANKING SYSTEM ###




init()
