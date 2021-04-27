#cup="water"
#print(cup)
#cup="sand"
#print(cup)

#crate = ['sand','water',7,5.9,True]
#print(crate[1])#list/array-variable that can hold multiple values at the same time.
#crate.append('Loretta')#adding a bew item on the list

#print(crate[5])

#firstValue=50
#secondValue=200
#result=firstValue+secondValue
#print(result)
#string1="Loretta"
#string2="4.5"
#string3="0"
#string4="truth"
#string5="6"

#print(string1+' has the '+string4)
#number1=5
#number2=0
#number3=-2
#number4=4.5
#number5=5463677483773

#print(number1+number3)
#print(number1+string1)
#age = 55

#isStudentAction=True
#print(isStudentAction)

#isGraduate=False
#print(isGraduate)
#if(age > 45):
    #print('yes')

    #string formating
#name = "Loretta" #string=s
#age=23 #number=d
#print("Her name is %s and she is %d" % (name,age))    

#sampleList = ['Loretta', 'love', 'dove']

#print("some text %s" % sampleList)

#length of a string
#string="Iam a string"
#string2="LORETTA IS GREAT"
#print(len(string))  length 
#print(string.index('m'))  position
#print(string.count('a'))
#print(string[1:6]) #displays from string 1 to 6


#print(string1.upper())
#print(string2.lower())

#print(string1[::-1])
#print(string.startswith("p"))
#print(string.endswith("g"))

#operators

#firstValue=4
#secondValue=7

#addition, used for concatenation of strings
#print(firstValue+secondValue)
#multiplication

#print(firstValue*secondValue)

#division
#print(firstValue/secondValue)

#assignment operator =
#comparison

#print(firstValue==secondValue) #compares if two values are equal.

#print(firstValue>secondValue)

#print(firstValue<secondValue)

#print(firstValue>=secondValue)

#print(firstValue<=secondValue)

#remainder
#print(firstValue % secondValue)

#voice="Scream |"
#print(voice * 5)
#alist=[1, 2, 3, 4, 5, 6]
#print(alist * 3)

#A=[1,2,3,4]
#B=[5,5,7,8]

#print(A+B)

#age=35
#print(age)
#age +=1
#print(age)

#age=15
#height=5

#the two conditions must be true for the test to pass
#if(age>=18 and height>=5):
 #   print('Person can get on this ride')

#elif(age<18 or height<5):
 #   print('Person cannot get on this ride')    
#or condition, only one is required to be true for the test to pass
#if(age<18):
    #print('Customer is not allowed to wach this movie')    
#else:
 #    print('Error, something went wrong with your inputs')
 #For Loops 
#alist=[1,3,5,6,7]
#for item in alist:
 #   print(item)
#for x in range(5):
 #   if(not(x==0)):
  #   print(x)
  #while loop
#count = 5

 
#while count > 0:
 #   print(count)
  #  count -= 1  
  #Functions
import datetime  
import random
import validation
import database
#database={
 #   1175761664: ['Loretta', 'Khisa', 'lorettakhisa15@gmail.com', 'lolop'], "Balance":200
#}  #dictionary
def init():

    print("Welcome to bankPHP")

    haveAccount=int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))
    if(haveAccount==1):
        login()
    elif(haveAccount==2):
        register()
    else:
        print("You have selected invalid option")        
        init()
    


def login():
    print("********LOGIN********")

    accountNumberFromUser=input("What is your account number? \n")

    is_valid_account_number =validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        password=input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if accountNumber==int(accountNumberFromUser):
                if(userDetails[3]==password):
                    bankOperation(userDetails)

        print('Invalid account or password')
        login()   
    else:
        init()             


def register():
      print("******REGISTER*****")     
      email=input("What is your email address \n")
      first_name=input("What is your first name \n")
      last_name=input("What is your last name \n")
      password=input("Create your password \n")

      accountNumber=generateAccountNumber()

      

      #return database
      #using database module to create new user record
      #create a file
      is_user_created=database.create(accountNumber,[first_name, last_name, email, password, 0])

      if(is_user_created):

            e=datetime.datetime.now()
            print("Your account has been created")
            print("=== ==== ===== ===== ===== ==")
            print("Your account number is: %d" % accountNumber)
            print("Make sure to keep it safe")
            print("== ==== ===== ===== ==== ==== =")
            print('date and time =%s' % e)

            login()

      else:
            print("Something went wrong, please try again")
            register()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1] ))

    isSelectedOptionValid=False
    while isSelectedOptionValid==False:
        selectedOption=int(input("What would you like to do?: 1 (deposit) 2 (withdraw) 3 (complain) 4 (exit) \n"))

        if(selectedOption==1):
           
            depositOperation()
        elif(selectedOption==2):
            
            withdrawalOperation()
        elif(selectedOption==3):
              
            complain()
        elif(selectedOption==4):
            
            exit()        
        else:
            print("Invalid option selected")
            bankOperation(user)    

def withdrawalOperation():
    print("How much would you like to withdraw?")

    amount=int(input('Write amount \n'))
    if(database["Balance"]>amount):
        print('Take your cash')
        balance=database["Balance"]-amount
        print("Your balance is %d" % balance)
    else:
        print("you cannot withdraw that amount")

    

    #get current balance
    #get amount to withdraw
    #check if current balance>withdraw amount
    #deduct withdrawn amount from current balance
    #display current balance
def depositOperation():
    print("How much would you like to deposit?")

    amount=int(input('Write amount \n'))
    balance=database["Balance"]+amount
    print('Your balance is %d' % balance)
#get current balance
#get amount to deposit
#add deposited amount to current balance
#display current balance
#do you want to do another operation?
def complain():
    print('What issue would you like to report?')
    issue=input('Report any issues here \n')
    print('Thank you for contacting us.')


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def get_current_balance(userDetails):
    return userDetails[4]    

   ###Actual banking system
init() 
exit()