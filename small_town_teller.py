class Person:
    def __init__(self, p_id, f_name, l_name):
        self.id = p_id
        first_name = f_name
        last_name = l_name

class Account:
    def __init__(self, acc_number, account_type, owner, init_deposit):
        self.acc_num = acc_number
        self.acc_type = account_type
        self.owner = owner
        self.balance = init_deposit


class Bank:
    def add_customer(self):
        pass
    def add_account(self, customer):
        pass
    def remove_account(self, customer, account):
        pass
    def deposit_money(self, customer, account, amount):
        pass
    def withdraw_money(self, customer, account, amount):
        pass
    def balance_inquiry(self, customer, account):