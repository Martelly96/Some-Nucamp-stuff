class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
        print(" Name changed to:", self.name)

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.pin = new_password


class BankUser(User):
    def __init__(self, name, pin, password, balance):
        super().__init__(name, pin, password)
        self.balance = balance

    def show_balance(self):
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, User1, User2, amount,):
        if self.pin == User1.pin and User1.balance >= amount:
            User1.withdraw(amount)
            User2.deposit(amount)
            return True
        else:
            return False

    def request_money(self, User1, User2, amount):
        pin2 = print(input(int("Enter Pin: ")))
        if pin2 == self.pin:
            return True
        password2 = print("Enter you password:")
        if password2 == self.password:
            User1.a


# Driver Code for Task 1
Bank_User = BankUser("Bob", "1234", "password", 0)
print(Bank_User)


# Driver Code for Task 2
Bank_User2 = BankUser("Bob", "1234", "password", 0)
print(Bank_User2)
Bank_User2.change_name
Bank_User2.change_pin
Bank_User2.change_password

# Driver Code for Task 3
Bank_User3 = BankUser("Terry", "1234", "password", 0)
print(Bank_User)

# Driver Code for Task 4
Bank_User4 = BankUser("name", "pin", "password", 0)
Bank_User4.show_balance
Bank_User4.deposit(500)
Bank_User4.show_balance
Bank_User4.withdraw(300)

# Driver Code for Task 5
Bank_User5 = BankUser("name", "pin", "password", 0)
Bank_User5.deposit(5000)
Bank_User5.show_balance
Bank_User2.show_balance
Bank_User.show_balance
Bank_User.transfer_money(Bank_User2, Bank_User, 1000)
Bank_User2.transfer_money(Bank_User, Bank_User2, 500)
Bank_User.show_balance
Bank_User2.show_balance
Bank_User2.request_money(Bank_User2, Bank_User, 200)
Bank_User.show_balance
Bank_User2.show_balance
