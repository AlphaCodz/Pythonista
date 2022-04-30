class AlphaBank():
    def __init__(self):
        self.Initial_Amount = 0
        self.Client_name = ""
    
    def Welcome(self):
        self.Client_name = input("Kindly Enter Your Name:: ")
        return "Hello {} , Welcome to AlphaBank".format(self.Client_name)
    
    def CurrentBalance(self):
        print("Dear {} , Your Current Account Balance = {}".format(self.Client_name, self.Initial_Amount))
    
    def Deposit_Funds(self):
        self.Initial_Amount += float(input("Enter Amount to deposit:: "))
        self.CurrentBalance()
        
    def Withdraw_Funds(self):
        withdrawal_amount = float(input("Enter amount to withdraw:: "))
        
        if withdrawal_amount > self.Initial_Amount:
            print("Insufficient Balance!")
        else:
            self.Initial_Amount -=withdrawal_amount 
              
        self.CurrentBalance()
    
if __name__ == "__main__":
    Bank = AlphaBank()
    Bank.Welcome()
    
while True:
    input_value = int(input('Enter 1 to see your balance,\n2 to deposit\n3 to withdraw\n'))

    if input_value == 1:
        Bank.CurrentBalance()
    elif input_value == 2:
        Bank.Deposit_Funds()
    elif input_value == 3:
        Bank.Withdraw_Funds()
    else:
        print('Please enter a valid input.')