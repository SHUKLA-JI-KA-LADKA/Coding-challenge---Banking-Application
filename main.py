from Account import Account #Importing account details from the file Account
import os
listAccount=[] #Making a Variable of list of Account 
cmd = 0 #Declaring  cmd variable
def searchAccount(lst,AN): #search function 
    accObj=None
    for item in lst:
        if item.AccountNo==AN:
            accObj = item
            break
    return accObj
    


while cmd!=6: #loop so that if 6 is choose the app should exit
    os.system("cls")
    print("#-----------------------------------#")
    print("\t Banking System")
    print("#-----------------------------------#")

    #making Menu 

    print("1. Create Account")
    print("2. Show Balance")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Show all Account")
    print("6. Exit")
    print("#-----------------------------------#")

    cmd=int(input("Enter Command : ")) #making menu option  
    match cmd:
        case 1:
            FN=input("Enter First Name ")
            LN=input("Enter Last Name ")
            AN=input("Enter Account No ")
            BL=int(input("Enter Balance "))
            accObj=Account(FN,LN,AN,BL) #Creating Account Object
            listAccount.append(accObj)
            print("Account Created Successfully ")
            input("Press ENTER to Continue....")
        case 2:
            AN=input("Enter Account No. ")
            accObj=searchAccount(listAccount,AN) #Searching existing Account
            if accObj==None:
                print("Account Not Found")
            else:
                accObj.showBalance() #Returning/Showing the balance
            input("Press ENTER to Continue....")
        
        case 3:   #deposite Amount
            AN=input("Enter Account No. : ")
            AT=int(input("Enter Amount : "))
            accObj=searchAccount(listAccount,AN)
            if accObj==None:
                print("Account Not Found")
            else:
                accObj.deposit(AT)
                print("Amount has been deposited Succesfully")
            input("Press ENTER to Continue....")

        case 4:  #Withdraw Amount 
            AN=input("Enter Account No. : ") 
            AT=int(input("Enter Amount : "))
            searchAccount(listAccount,AN)
            if accObj==None:
                print("Account Not Found")
            else:
                if accObj.withdraw(AT):
                    print("Amount Deposited Succfully")
                else:
                     print("Insufficient Balance ")
            input("Press Enter to Continue...")

        case 5: #display all account with name and balance
            print("| Name".ljust(20)+" | " +"Balance".ljust(8)+" | ")
            for item in listAccount:
                name=str(item.First_Name+" ").ljust(20)
                balance=str(item.Balance).ljust(8)
                msg="|"+name+"|"+balance+"  |"
                print(msg)
            input("Press Enter to Continue....")