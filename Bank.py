class bank:
    bank_name='HDFC'
    branch_name='marathahalli'
    IFSC='HDFC00024'
    roi=0.07
    
    def __init__(self ,name,mno,accno,pan,balance,pin):
        self.name   =name
        self.mno    =mno
        self.accno  =accno
        self.pan    =pan
        self.balance=balance
        self.pin    =pin
        
    @classmethod
    def change_roi(cls):
        cls.roi=float(input('Enter new roi : '))
        
    @staticmethod
    def get_pin():
        return(input('Enter the pin: '))
    
    def validate(self):
        return self.pin==self.get_pin()
    
    def check_balance(self):
        if self.validate():
            print(self.balance)
        else:
            print('incorrect pin.')
            
    def withdraw(self):
        if self.validate():
            amount=int(input('Enter the amount: '))
            if self.balance>amount:
                self.balance -=amount
                print('Amount withdrawn...')
            else:
                print('insuffent balance...')
        else:
            print('Incorrect pin.')
            
    def deposit(self):
        amount=int(input('Enter amount to be deposit: '))
        self.balance=self.balance+amount
        print(f'your available ballance is{self.balance}')
    def change_pin(self):
        if self.pin==input('Enter the old pin: '):
            new_pin1=input('Enter the new pin: ')
            new_pin2=input('Re enter the new pin: ')
            if(new_pin1==new_pin2):
                self.pin=new_pin1
                print('pin updated succesfully')
            else:
                print('Not matching')
        else:
            print('Incorrect old pin')          
        
b1=bank('Ashish',6386352801,1234554321907,'axt1122',4000,'1234')
b1.change_pin()

b1.withdraw()

b1.deposit()

b1.check_balance()

b1.change_roi()
