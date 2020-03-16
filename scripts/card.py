class card:
    def __init__(self, number, customer_name, exp_date, balance=0):
        self.number = number
        self.customer_name = customer_name
        self.exp_date = exp_date
        self.balance = balance
        self.transactions = {}

    def display_details(self):
        print("\n----------------------")
        print("Number: "+str(self.number))
        print("Name: "+str(self.customer_name))
        print("Expiration Date: "+str(self.exp_date))
        print("Current Balance: "+str(self.balance))
        print("Transaction History: "+str(self.transactions))

    def purchase(self,charge_off,trxn_id):
        if float(charge_off) >= 0:
            print("$%d charged off card." % charge_off)
            self.balance -= charge_off
            self.transactions[trxn_id] = charge_off * -1
        else:
            return print("Transaction not valid!")


class debit(card):
    def __init__(self, number, customer_name, exp_date, pin, balance=0):
        super().__init__(number, customer_name, exp_date, balance=0)
        self.pin = pin

    def check_pin(self):
        print("Enter your pin: ")
        value = input()
        if value != str(self.pin):
            print("Incorrect Pin!")
            return False
        else:
            print("Access granted.")
            return True

    def add_value(self, value, trxn_id):
        if not self.check_pin():
            return None
        if float(value) <= 0:
            return print("Transaction not valid!")
        self.balance += value
        self.transactions[trxn_id] = value
        print("$%d has been added to balance." % value)

    def purchase(self,charge_off,trxn_id):
        if not self.check_pin():
            return None
        if charge_off > self.balance:
            return print("Not sufficient funds!")
        return super().purchase(charge_off,trxn_id)

class credit(card):
    def __init__(self, number, customer_name, exp_date, balance=0):
        super().__init__(number, customer_name, exp_date, balance=0)
        self.cash_back_total = 0
        self.cash_back_rate = 1.02

    def pay_balance(self, value, trxn_id):
        if float(value) <= 0:
            return print("Invalid transaction!")
        self.balance += value
        self.transactions[trxn_id] = value

    def charge_interest(self, interest_rate):
        self.balance *= interest_rate

    def purchase(self,charge_off,trxn_id):
        super().purchase(charge_off, trxn_id)
        self.cash_back_total += charge_off * self.cash_back_rate

    def display_details(self):
        super().display_details()
        print("Cash back total: "+str(self.cash_back_total))
        print("Cash back rate: "+str(self.cash_back_rate))


