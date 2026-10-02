#import the bank accounts already saved in my json file
import json
with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","r") as file:
    bank_owners = json.load(file)
with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","r") as file:
    savings_owners = json.load(file)

# -- PARENT CLASS --

class BankAccounts:
    bank = "Bank England" #class attribute - all objects have the same bank 
    def __init__(self,name,balance): #instance attributes - each object can vary name and balance
        self.name = name
        self.balance = balance
    def view_balance(self): #method to view name and balance of one object
        print(self.name, self.balance)
    def deposit_funds(self, deposit):
        self.balance = self.balance + deposit
    def withdraw_funds(self, withdraw):
        if self.balance >= withdraw:
            self.balance = self.balance - withdraw #checks the amount to withdraw is not greater than the balance
        else:
            print("You do not have enough funds")

# -- CHILD CLASS --

class SavingsAccounts(BankAccounts):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def view_savings_balance(self):
        print(self.name, self.balance)
    


owners = [] #a new list for the dictionary list to become objects of class BankAccounts 
for owner in bank_owners: #the for loop goes through each dictionary in bank_owners and makes each the name and balance an object of BankAccounts class
    each_owner = BankAccounts(owner["name"],owner["balance"])
    owners.append(each_owner)

s_owners = [] #a list for the savings accounts as class objects
for owner in savings_owners:
    each_s_owner = SavingsAccounts(owner["name"],owner["balance"])
    s_owners.append(each_s_owner)

print(owners[0].name) #print name from object list 
print(bank_owners[0]["name"]) #print name from dictionary list

owners[0].view_balance() #using function in class, print name and balance of first bank owner, from the owners_list (class object list)
print(bank_owners[0]["name"], bank_owners[0]["balance"]) #print name and balance of first bank owner from the bank_owners (dict list)

# -- FUNCTIONS --
def view_all_balances():  #view all of the accounts - names and balances 
        for owner in owners:
            print("Main account - ",owner.name, owner.balance)
view_all_balances()

def view_all_savings_balances(): #view all of the savings accounts - names and balances 
    for owner in s_owners:
        print("Savings account - ", owner.name, owner.balance)
view_all_savings_balances()


def check_account_exists(index_no): #When option of bank account is selected within the menu, check that the account exists 1-5 
    index_no = int(index_no) - 1
    if owners[index_no].bank == "Bank England":
        return 1
    else:
        print("account doesn't exist")
        return 0
       

# -- MAIN MENU -- 
def main_menu():
    print("\nMENU \n1. Add bank account \n2. Check balance \n3. Deposit funds \n4. Withdraw funds \n5. Transfer funds to savings account \n6. Transfer funds to main account \n7. Delete account \n8. Quit")
    try:
        menu = int(input("Select an option: "))
    except:
        print("not valid input. please try again.")
        return
    
    # -- ADD BANK ACCOUNT --  
    if menu == 1: 
        if len(owners) < 5: #checks the length of current bank owners is less than 5. If there are 5 account already, an error message will show
            new_name = input("Please enter the first name for the new bank account: ")
            if new_name.isalpha(): #checks that the new_name input only contains letters 
                try:
                    new_balance = int(input("How much will you be depositing for your new account: "))
                except ValueError: #if anything other than numbers is entered 
                    print("not valid amount")
                    return
                if new_balance <= 0:
                    print("amount must be greater than 0")
                    return

                bank_owners.append({"name":new_name, "balance":new_balance}) #add the new details to the dictionary list for bank owners
                savings_owners.append({"name":new_name, "balance": 0}) #creates a savings account in the dictionary list for the new owner with value zero 

                with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                    json.dump(bank_owners, file) #add to bankowners json file
                with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                    json.dump(savings_owners, file) #add to savingsaccounts json file

                owners.clear()
                for owner in bank_owners:
                    object_owner = BankAccounts(owner["name"],owner["balance"])
                    owners.append(object_owner)
                view_all_balances()

                s_owners.clear()
                for owner in savings_owners:
                    each_s_owner = SavingsAccounts(owner["name"],owner["balance"])
                    s_owners.append(each_s_owner)
                view_all_savings_balances()

            else:
                print("only letters are valid input")
        else:
            print("not possible. maximum of 5 bank accounts reached")
            return


    # -- CHECK BALANCE --
    elif menu == 2: 
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
        try:
            index_no = int(input("Please select which bank account you would like to view: "))
        except ValueError:
            print("not valid input. please try again.")
            return 
        check_account_exists(index_no)
        try: 

            index_no = int(index_no) - 1
            owners[index_no].view_balance()
            s_owners[index_no].view_savings_balance()

        except:
            print("not valid input")
            return
        
    # -- DEPOSIT FUNDS --
    elif menu == 3: 
            for index, owner in enumerate(owners, start=1):
                print(index, owner.name)
            try:
                index_no = int(input("Please select which bank account you are depositing into: "))
            except ValueError:
                print("not valid input. please try again.")
                return
            if check_account_exists(index_no) == 1:
                try:
                    deposit_amt = int(input("How much would you like to deposit: "))
                except ValueError:
                    print("not valid input. please try again.")
                    return
                if deposit_amt > 0: #value depositted has to be over 0
                    try:
                        index_no = int(index_no) -1
                        owners[index_no].deposit_funds(deposit_amt) 
                        #need to amend the bank_owners(dict) list to match owners(object) new balance
                        bank_owners[index_no]["balance"] = owners[index_no].balance
                        owners[index_no].view_balance() #print the bank_owners list to check updated
                        with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                            json.dump(bank_owners, file) #save into json - already saved into my two lists here so don't need to reload

                    except Exception as error:
                        print("not valid input. please try again.")
                        return
                else:
                    print("you can only deposit a value over 0")
            else:
                return
            
    # -- WITHDRAW FUNDS --
    elif menu == 4: 
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
        try:
            index_no = int(input("Which bank account would you like to withdraw from? "))
        except ValueError:
            print("not valid input. please try again.") #check that they have input an available number
        if check_account_exists(index_no) == 1:
            try:
                withdraw_amt = int(input("How much would you like to withdraw: "))
            except ValueError:
                print("not valid input. please try again.")
            if withdraw_amt <= 0:
                print("Value must be greater than 0")
                main_menu()
            else:
                index_no = int(index_no) - 1
                owners[index_no].withdraw_funds(withdraw_amt)#this will call the function to withdraw and the balance will be changed within the object list owners
                bank_owners[index_no]["balance"] = owners[index_no].balance  #change the balance within the dict list(bank_owners) and then copy that to json 
                with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                    json.dump(bank_owners,file)
        else:
            return      

    # -- TRANSFER TO SAVINGS ACCOUNT -- 
    elif menu ==5:
        for index, owner in enumerate(owners, start=1): #loop through all in object list and number them but start at 1 not 0. 
            print(index, owner.name) #print the index number starting at 1, alongside the owners name
        try:
            index_no = int(input("Please select the account you would like to transfer from: "))
        except ValueError: # exception for if a none integer is entered
            print("not valid input. please try again.")
            return
        
        if check_account_exists(index_no) == 1: #1 is the number returned when the account does exist 
            index_no = int(index_no) - 1
            print("Main account:")
            owners[index_no].view_balance()
            print("Savings account:")
            s_owners[index_no].view_savings_balance() #prints the amount the ower has in their main and savings account
            try:
                transfer_amt = int(input("How much would you like to transfer? "))
            except ValueError:
                print("not valid input. please try again.")
                return

            owners[index_no].balance = owners[index_no].balance - transfer_amt #amending the balances of the objects
            s_owners[index_no].balance = s_owners[index_no].balance + transfer_amt 

            bank_owners[index_no]["balance"] = owners[index_no].balance #amend dictionarys to match the objects balance
            savings_owners[index_no]["balance"] = s_owners[index_no].balance 

            with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:   #update json for balance changes
                json.dump(bank_owners, file) 
            with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                json.dump(savings_owners, file) 

            print("Main account:") #reprint the balances
            owners[index_no].view_balance()
            print("Savings account:")
            s_owners[index_no].view_savings_balance()


    # -- TRANSFER TO MAIN ACCOUNT -- 
    elif menu ==6:
        for index, owner in enumerate(owners, start=1): #loop through all in object list and number them but start at 1 not 0. 
            print(index, owner.name) #print the index number starting at 1, alongside the owners name
        try:
            index_no = int(input("Please select the account you would like to transfer from: "))
        except ValueError: # exception for if a none integer is entered
            print("not valid input. please try again.")
            return   


    # -- DELETE AN ACCOUNT -- 
    elif menu == 7: 
        for index, owner in enumerate(owners, start=1): #loop through all in object list and number them but start at 1 not 0. 
            print(index, owner.name) #print the index number starting at 1, alongside the owners name
        try:
            index_no = int(input("Please select which bank account you would like to delete: "))
        except ValueError: # exception for if a none integer is entered
            print("not valid input. please try again.")
            return
        if check_account_exists(index_no) == 1: #1 is the number returned when the account does exist 
            index_no = int(index_no) - 1 #makes the number selected match the index number
            del bank_owners[index_no] #deletes the bank account
            del savings_owners[index_no]

            with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                json.dump(bank_owners, file)
            with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                json.dump(savings_owners, file)

            #get the owners(class objects) list to match the updated bank_owners(dict)
            owners.clear() #remove all on the owners list to then loop through all the dictionarys to make them objects into that list
            for owner in owners:
                each_owner = BankAccounts(owner["name"],owner["balance"])
                owners.append(each_owner)

            savings_owners.clear()
            for owner in savings_owners:
                each_s_owner = SavingsAccounts(owner["name"],owner["balance"])
                s_owners.append(each_s_owner)


            view_all_balances()
            view_all_savings_balances()

            print(bank_owners)
        else:
            return

main_menu()



        

        
         