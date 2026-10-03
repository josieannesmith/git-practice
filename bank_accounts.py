#import the bank accounts already saved in my json file
import json
import requests


with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","r") as file:
    bank_owners = json.load(file)
with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","r") as file:
    savings_owners = json.load(file)
with open("/Users/josephinesmith/Documents/Python/git-practice/euroaccounts.json","r") as file:
    euro_owners = json.load(file)


# -- PARENT CLASS --

class BankAccounts:
    bank = "Bank England" #class attribute - all objects have the same bank 
    def __init__(self,name,balance): #instance attributes - each object can vary name and balance
        self.name = name
        self.balance = balance
    def view_balance(self): #method to view name and balance of one object
        print(self.name,"- Main account:", self.balance)
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
        print(self.name, "- Savings account:", self.balance)

class EuroAccount(BankAccounts):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def view_euro_balance(self):
            print(self.name,"- Euro account:", self.balance)
    

owners = [] #a new list for the dictionary list to become objects of class BankAccounts 
for owner in bank_owners: #the for loop goes through each dictionary in bank_owners and makes each the name and balance an object of BankAccounts class
    each_owner = BankAccounts(owner["name"],owner["balance"])
    owners.append(each_owner)

s_owners = [] #a list for the savings accounts as class objects
for owner in savings_owners:
    each_s_owner = SavingsAccounts(owner["name"],owner["balance"])
    s_owners.append(each_s_owner)

e_owners = [] #a list for the euro accounts as class objects
for owner in euro_owners:
    each_e_owner = EuroAccount(owner["name"],owner["balance"])
    e_owners.append(each_e_owner)


# -- FUNCTIONS --
def view_all_balances():  #view all of the accounts - names and balances 
        for owner in owners:
            print("Main account - ",owner.name, owner.balance)

def view_all_savings_balances(): #view all of the savings accounts - names and balances 
    for owner in s_owners:
        print("Savings account - ", owner.name, owner.balance)

def view_all_euro_balances():
    for owner in e_owners:
        print("Euro account - ", owner.name, owner.balance)



def check_account_exists(index_no): #When option of bank account is selected within the menu, check that the account exists 1-5 
    index_no = int(index_no) - 1
    if owners[index_no].bank == "Bank England":
        return 1
    else:
        print("account doesn't exist")
        return 0
       

# -- MAIN MENU -- 
def main_menu():
    print("MENU \n1. Add bank account \n2. Check balance \n3. Deposit funds \n4. Withdraw funds \n5. Transfer funds \n6. Delete account \n7. Quit")
    try:
        menu = int(input("Select an option: "))
        if menu < 1 or menu > 7:
            raise Exception
    except:
        print("not valid input. please try again.")
        return 
    
    # -- ADD BANK ACCOUNT --  
    if menu == 1: 
        if len(owners) < 5: #checks the length of current bank owners is less than 5. If there are 5 account already, an error message will show
            new_name = input("Please enter the first name for the new bank account: ").title()
            if new_name.isalpha(): #checks that the new_name input only contains letters 
                try:
                    new_balance = int(input("How much will you be depositing for your new account: "))
                    if new_balance <= 0:
                        raise Exception
                except ValueError: #if anything other than numbers is entered 
                    print("not valid amount")
                    return 
                except:
                    print("amount must be greater than 0")
                    return 

                bank_owners.append({"name":new_name, "balance":new_balance}) #add the new details to the dictionary list for bank owners
                savings_owners.append({"name":new_name, "balance": 0}) #creates a savings account in the dictionary list for the new owner with value zero 
                euro_owners.append({"name":new_name, "balance": 0})


                with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                    json.dump(bank_owners, file) #add to bankowners json file
                with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                    json.dump(savings_owners, file) #add to savingsaccounts json file
                with open("/Users/josephinesmith/Documents/Python/git-practice/euroaccounts.json","w") as file:
                    json.dump(euro_owners, file) #add to savingsaccounts json file                    

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

                e_owners.clear()
                for owner in euro_owners:
                    each_e_owner = EuroAccount(owner["name"],owner["balance"])
                    e_owners.append(each_e_owner)
                view_all_euro_balances()

                return
                
            else:
                print("only letters are valid input")
                return 

        else:
            print("not possible. maximum of 5 bank accounts reached")
            return


    # -- CHECK BALANCE --
    elif menu == 2: 
        counter = 0
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
            counter = counter + 1
        try:
            index_no = int(input("Please select which bank account you would like to view: "))
            if index_no > counter:
                raise Exception
        except:
            print("not valid input. please try again.")
            return 
        
        check_account_exists(index_no)
        try: 
            index_no = int(index_no) - 1
            owners[index_no].view_balance()
            s_owners[index_no].view_savings_balance()
            e_owners[index_no].view_euro_balance()
            return

        except:
            print("not valid input")
            return 
        
    # -- DEPOSIT FUNDS --
    elif menu == 3: 
        counter = 0
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
            counter = counter + 1
        try:
            index_no = int(input("Please select which bank account you are depositing into: "))
            if index_no > counter:
                raise Exception
        except:
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
        counter = 0
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
            counter = counter + 1
        try:
            index_no = int(input("Which bank account would you like to withdraw from? "))
            if index_no > counter:
                raise Exception
        except ValueError:
            print("not valid input. please try again.")
            return
        except:
            print("not valid input. please try again.") #check that they have input an available number
            return
        if check_account_exists(index_no) == 1:
            owners[index_no-1].view_balance()
            try:
                withdraw_amt = int(input("How much would you like to withdraw: "))
            except ValueError:
                print("not valid input. please try again.")
                return
            if withdraw_amt <= 0:
                print("Value must be greater than 0")
                return
                
            else:
                index_no = int(index_no) - 1
                owners[index_no].withdraw_funds(withdraw_amt)#this will call the function to withdraw and the balance will be changed within the object list owners
                bank_owners[index_no]["balance"] = owners[index_no].balance  #change the balance within the dict list(bank_owners) and then copy that to json 
                with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                    json.dump(bank_owners,file)

                owners[index_no].view_balance()
        else:
            return    

        # -- TRANSFER FUNDS -- 
    elif menu == 5:
        print("1. Main account to Savings account. \n2. Savings account to Main account. \n3. Main account to Euro Account. \n4. Euro account to Main account")
        try:
            transfer_choice = int(input("Which transfer would you like to make? ")) 
            if transfer_choice < 1 or transfer_choice > 4:  
                raise Exception
        except:
            print("Not a valid input. Please try again.")
            return   

        counter = 0 #to count the length of the list
        for index, owner in enumerate(owners, start=1): #loop through all in object list and number them but start at 1 not 0. 
            print(index, owner.name) #print the index number starting at 1, alongside the owners name
            counter = counter + 1
        try:
            index_no = int(input("Please select the account you would like to transfer from: "))
            if index_no > counter:
                raise Exception
        except: # exception for if a none integer is entered
            print("not valid input. please try again.")
            return

        if check_account_exists(index_no) == 1: #1 is the number returned when the account does exist
            index_no = int(index_no) - 1

            # -- MAIN TO SAVINGS ACCOUNT -- 
            if transfer_choice == 1:  
                print("Main account:")
                owners[index_no].view_balance()
                print("Savings account:")
                s_owners[index_no].view_savings_balance() #prints the amount the ower has in their main and savings account
                try:
                    transfer_amt = int(input("How much would you like to transfer? "))
                    if transfer_amt > owners[index_no].balance:
                        raise Exception
                except:
                    print("not valid input. please try again.")
                    return
                if transfer_amt > 0:
                    owners[index_no].balance = owners[index_no].balance - transfer_amt #amending the balances of the objects
                    s_owners[index_no].balance = s_owners[index_no].balance + transfer_amt 

                    bank_owners[index_no]["balance"] = owners[index_no].balance #amend dictionarys to match the objects balance
                    savings_owners[index_no]["balance"] = s_owners[index_no].balance 

                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:   #update json for balance changes
                        json.dump(bank_owners, file) 
                    with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                        json.dump(savings_owners, file) 
                else:
                    print("Amount must be greater than zero")
                    return 


            # -- SAVINGS TO MAIN ACCOUNT -- 
            if transfer_choice == 2:  
                print("Main account:")
                owners[index_no].view_balance()
                print("Savings account:")
                s_owners[index_no].view_savings_balance() #prints the amount the ower has in their main and savings account
                try:
                    transfer_amt = int(input("How much would you like to transfer? "))
                    if transfer_amt > s_owners[index_no].balance:
                        raise Exception
                except:
                    print("not valid input. please try again.")
                    return 
                if transfer_amt > 0:
                
                    s_owners[index_no].balance = s_owners[index_no].balance - transfer_amt #amending the balances of the objects
                    owners[index_no].balance = owners[index_no].balance + transfer_amt
        
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
                    
                else:
                    print("Amount must be greater than zero")
                    return 

            # -- MAIN TO EURO ACCOUNT -- 
            if transfer_choice == 3:


                import requests
                try: 
                    euro_gbp_json = requests.get("https://latest.currency-api.pages.dev/v1/currencies/eur.json") #requesting the api data for euro bank 
                    if not euro_gbp_json.status_code == 200:
                        raise Exception
                except:
                    print("exchange rate not available")
                    return

                if euro_gbp_json.status_code == 200:
                    print("Main account:")
                    owners[index_no].view_balance()
                    print("Euro account:")
                    e_owners[index_no].view_euro_balance()


                    euro_gbp = euro_gbp_json.json() #turning the data to python code 
                    euro_gbp = (euro_gbp["eur"]["gbp"]) #taking the data i want out of it - the exchange rate

                    try:
                        transfer_amt = int(input("How many pounds would you like to transfer? "))
                        if transfer_amt > owners[index_no].balance:
                            raise Exception
                    except:
                        print("not valid input. please try again.")
                        return 
                    if transfer_amt > 0:

                        exchange_to_eur = int(transfer_amt * euro_gbp)

                        print(f"Exchange rate: {euro_gbp} \nGBP: {transfer_amt} \nEUR: {exchange_to_eur}")

                        owners[index_no].balance = owners[index_no].balance - transfer_amt #change object balances
                        e_owners[index_no].balance = e_owners[index_no].balance + int(exchange_to_eur)

                        bank_owners[index_no]["balance"] = owners[index_no].balance #update the dictionary lists
                        euro_owners[index_no]["balance"] = e_owners[index_no].balance

                        with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                            json.dump(bank_owners, file)
                        with open("/Users/josephinesmith/Documents/Python/git-practice/euroaccounts.json","w") as file:
                            json.dump(euro_owners, file) 
                    else:
                        print("Amount must be greater than zero")
                        return    
                else:
                    print("exchange rate not available")
                    return                               


            # -- EURO TO MAIN ACCOUNT -- 

            if transfer_choice == 4:
                import requests
                try:
                    euro_gbp_json = requests.get("https://latest.currency-api.pages.dev/v1/currencies/eur.json") #requesting the api data for euro bank
                    if not euro_gbp_json.status_code == 200:
                        raise Exception
                except:
                    print("Exchange rate not available")
                    return

                if euro_gbp_json.status_code == 200:
                    print("Main account:")
                    owners[index_no].view_balance()
                    print("Euro account:")
                    e_owners[index_no].view_euro_balance()

                    euro_gbp = euro_gbp_json.json() #turning the data to python code 
                    euro_gbp = (euro_gbp["eur"]["gbp"]) #taking the data i want out of it - the exchange rate

                    try:
                        transfer_amt = int(input("How many euros would you like to transfer? "))
                        if transfer_amt > e_owners[index_no].balance:
                            raise Exception
                        elif transfer_amt < 0:
                            raise Exception
                    except:
                        print("not valid input. please try again.")
                        return
                    
                    exchange_to_gbp = int(transfer_amt / euro_gbp)

                    print(f"Exchange rate: {euro_gbp} \nGBP: {exchange_to_gbp} \nEUR: {transfer_amt}")

                    owners[index_no].balance = owners[index_no].balance + exchange_to_gbp
                    e_owners[index_no].balance = e_owners[index_no].balance - transfer_amt

                    bank_owners[index_no]["balance"] = owners[index_no].balance
                    euro_owners[index_no]["balance"] = e_owners[index_no].balance
                    
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file)
                    with open("/Users/josephinesmith/Documents/Python/git-practice/euroaccounts.json","w") as file:
                        json.dump(euro_owners, file)
                else:
                    print("Exchange rate not available")
                    return

        #for all: 
        else:
            print("not valid input. please try again.")
            return 

        print("Main account:") #reprint the balances
        owners[index_no].view_balance()
        print("Savings account:")
        s_owners[index_no].view_savings_balance()
        print("Euro account:")
        e_owners[index_no].view_euro_balance()

           


    # -- DELETE AN ACCOUNT -- 

    elif menu == 6:
        counter = 0
        for index, owner in enumerate(owners, start=1): #loop through all in object list and number them but start at 1 not 0. 
            print(index, owner.name) #print the index number starting at 1, alongside the owners name
            counter = counter + 1
        try:
            index_no = int(input("Please select which bank account you would like to delete: "))
            if index_no > counter:
                raise Exception
        except: # exception for if a none integer is entered
            print("not valid input. please try again.")
            return 
        if check_account_exists(index_no) == 1: #1 is the number returned when the account does exist 
            index_no = int(index_no) - 1 #makes the number selected match the index number
            del bank_owners[index_no] #deletes the bank account
            del savings_owners[index_no]
            del euro_owners[index_no]

            with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                json.dump(bank_owners, file)
            with open("/Users/josephinesmith/Documents/Python/git-practice/savingsaccounts.json","w") as file:
                json.dump(savings_owners, file)
            with open("/Users/josephinesmith/Documents/Python/git-practice/euroaccounts.json","w") as file:
                json.dump(euro_owners, file)                

            #get the owners(class objects) list to match the updated bank_owners(dict)
            owners.clear() #remove all on the owners list to then loop through all the dictionarys to make them objects into that list
            for owner in owners:
                each_owner = BankAccounts(owner["name"],owner["balance"])
                owners.append(each_owner)

            savings_owners.clear()
            for owner in savings_owners:
                each_s_owner = SavingsAccounts(owner["name"],owner["balance"])
                s_owners.append(each_s_owner)

            euro_owners.clear()
            for owner in euro_owners:
                each_e_owner = EuroAccount(owner["name"],owner["balance"])
                e_owners.append(each_e_owner)

            print("Bank accounts remaining:")
            for owner in bank_owners:
                print(owner["name"])
            
            return 
        else:
            return 
    else:
        return

main_menu()





        

        
         