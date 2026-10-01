#first, i import the bank accounts already saved in my json file
import json
with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","r") as file:
    bank_owners = json.load(file)

#next, create the class

class BankAccounts:
    def __init__(self,name,balance): #class attributes
        self.name = name
        self.balance = balance
    def view_balance(self):
        print(self.name, self.balance)
    def deposit_funds(self, deposit):
         self.balance = self.balance + deposit
    

#create a new list for the dictionary list to become objects of class BankAccounts. use a for loop to go through each one 
owners = []
for owner in bank_owners:
    each_owner = BankAccounts(owner["name"],owner["balance"])
    owners.append(each_owner)

print(owners[0].name) #from object list 
print(bank_owners[0]["name"]) #from dictionary list

owners[0].view_balance() #call balance of first bank owner on the object list

def view_all_balances():  #view all of the accounts - names and balances 
        for owner in owners:
            print(owner.name, owner.balance)
view_all_balances()

#Main Menu 
def main_menu():
    print("\nMENU \n1. Add bank account \n2. Check balance \n3. Deposit funds \n4. Withdraw funds \n5. Delete account \n6. Quit")
    try:
        menu = int(input("Select an option: "))
    except:
        print("not valid input. please try again.")

    if menu == 1:
        if len(owners) < 5:
            new_name = input("Please enter the name for the new bank account: ")
            try:
                new_balance = int(input("How much will you be depositing for your new account: "))
            except:
                print("not valid amount")
                return
            bank_owners.append({"name":new_name, "balance":new_balance}) #add the new details to the dictionary list 
            with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                json.dump(bank_owners, file) #add to json file
            owners.clear()
            for owner in bank_owners:
                object_owner = BankAccounts(owner["name"],owner["balance"])
                owners.append(object_owner)
            view_all_balances()
        else:
            print("not possible. maximum of 5 bank accounts reached")
            return



    if menu == 2: #check balance
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
        try:
            index_no = int(input("Please select which bank account you would like to view: "))
        except ValueError:
            print("not valid input. please try again.")
            return 
        try: 
            if index_no == 1:
                owners[0].view_balance()
            elif index_no == 2:
                owners[1].view_balance()
            elif index_no == 3:
                owners[2].view_balance()
            elif index_no == 4:
                owners[3].view_balance()
            elif index_no == 5:
                owners[4].view_balance()
        except:
            print("not valid input")
            return
        

    if menu == 3: #deposit funds
            for index, owner in enumerate(owners, start=1):
                print(index, owner.name)
            try:
                index_no = int(input("Please select which bank account you are depositing into: "))
            except ValueError:
                print("not valid input. please try again.")
                return
            try:
                deposit_amt = int(input("How much would you like to deposit: "))
            except ValueError:
                print("not valid input. please try again.")
                return
            try:
                if index_no == 1:
                    owners[0].deposit_funds(deposit_amt) 
                    #need to amend the bank_owners(dict) list to match owners(object) new balance
                    bank_owners[0]["balance"] = owners[0].balance
                    owners[0].view_balance() #print the bank_owners list to check updated
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file) #save into json - already saved into my two lists here so don't need to reload

                elif index_no == 2:
                    owners[1].deposit_funds(deposit_amt)
                    bank_owners[1]["balance"] = owners[1].balance
                    owners[1].view_balance()
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file) 
                    
                elif index_no == 3:
                    owners[2].deposit_funds(deposit_amt)
                    bank_owners[2]["balance"] = owners[2].balance
                    owners[2].view_balance()
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file)
                    
                elif index_no == 4:
                    owners[3].deposit_funds(deposit_amt)
                    bank_owners[3]["balance"] = owners[3].balance
                    owners[3].view_balance()
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file) 
                   
                elif index_no == 5:
                    owners[4].deposit_funds(deposit_amt)
                    bank_owners[4]["balance"] = owners[4].balance
                    owners[4].view_balance()
                    with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
                        json.dump(bank_owners, file)
                    
                else:
                    print("not valid input. please try again.")
                    return

            except Exception as error:
                print("not valid input. please try again.")
                return
                
                
    if menu == 5:
        for index, owner in enumerate(owners, start=1):
            print(index, owner.name)
        try:
            index_no = int(input("Please select which bank account you would like to delete: "))
        except ValueError:
            print("not valid input. please try again.")
            return
        try:
            if index_no == 1:
                del bank_owners[0]
            if index_no == 2:
                del bank_owners[1]
            if index_no == 3:
                del bank_owners[2]
            if index_no == 4:
                del bank_owners[3]
            if index_no == 5:
                del bank_owners[4]
        except:
            print("no bank account to delete")
            return

        with open("/Users/josephinesmith/Documents/Python/git-practice/bankowners.json","w") as file:
            json.dump(bank_owners, file)

        #turn the new bank owners list to the owners list with the class

        owners.clear()
        for owner in owners:
            each_owner = BankAccounts(owner["name"],owner["balance"])

        view_all_balances()
        print(bank_owners)

main_menu()

         