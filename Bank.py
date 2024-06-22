class Bank:
    bank_name = 'HDFC'
    branch_name = 'Marathahalli'
    IFSC = 'HDFC00024'
    roi = 0.07
    
    def __init__(self, name, mno, accno, pan, balance, pin):
        self.name = name
        self.mno = mno
        self.accno = accno
        self.pan = pan
        self.balance = balance
        self.pin = pin
        
    @classmethod
    def change_roi(cls):
        new_roi = float(input('Enter new ROI: '))
        cls.roi = new_roi
        print(f'ROI updated to {cls.roi}')
    
    @staticmethod
    def get_pin():
        return input('Enter the PIN: ')
    
    def validate(self):
        return self.pin == self.get_pin()
    
    def check_balance(self):
        if self.validate():
            print(f'Balance: {self.balance}')
        else:
            print('Incorrect PIN.')
            
    def withdraw(self):
        if self.validate():
            amount = int(input('Enter the amount to withdraw: '))
            if self.balance >= amount:
                self.balance -= amount
                print(f'Amount {amount} withdrawn successfully.')
            else:
                print('Insufficient balance.')
        else:
            print('Incorrect PIN.')
            
    def deposit(self):
        amount = int(input('Enter amount to deposit: '))
        self.balance += amount
        print(f'Your available balance is {self.balance}.')
    
    def change_pin(self):
        old_pin = input('Enter the old PIN: ')
        if old_pin == self.pin:
            new_pin1 = input('Enter the new PIN: ')
            new_pin2 = input('Re-enter the new PIN: ')
            if new_pin1 == new_pin2:
                self.pin = new_pin1
                print('PIN updated successfully.')
            else:
                print('PINs did not match.')
        else:
            print('Incorrect old PIN.')
            
# Main program loop
while True:
    print("\nWelcome to HDFC Bank")
    print("1. Create Account")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Check Balance")
    print("5. Change PIN")
    print("6. Change ROI")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input('Enter your name: ')
        mno = input('Enter your mobile number: ')
        accno = input('Enter your account number: ')
        pan = input('Enter your PAN number: ')
        balance = int(input('Enter initial balance: '))
        pin = input('Set your PIN: ')
        
        account = Bank(name, mno, accno, pan, balance, pin)
        print('Account created successfully.')
        
    elif choice == '2':
        if 'account' in locals():
            account.withdraw()
        else:
            print('Please create an account first.')
            
    elif choice == '3':
        if 'account' in locals():
            account.deposit()
        else:
            print('Please create an account first.')
            
    elif choice == '4':
        if 'account' in locals():
            account.check_balance()
        else:
            print('Please create an account first.')
            
    elif choice == '5':
        if 'account' in locals():
            account.change_pin()
        else:
            print('Please create an account first.')
            
    elif choice == '6':
        Bank.change_roi()
        
    elif choice == '7':
        print('Exiting...')
        break
    
    else:
        print('Invalid choice. Please enter a valid option.')

