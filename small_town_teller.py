class Person:
    def __init__(self, p_id, f_name, l_name):
        self.id = p_id
        self.first_name = f_name
        self.last_name = l_name


class Account:
    def __init__(self, account_type, owner):
        self.acc_number = None
        self.acc_type = account_type
        self.owner = owner
        self.balance = None
        # self.details = {'owner': owner, 'acc_type': account_type, 'balance': None}


class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.customers = {}  # ID: name
        self.accounts = {}
        self.bank_details = {'customer_id_count': 0, 'account_count' : 1000}  # may be unnecessary, but we will see when it comes time for persistence

    def add_customer(self, new_customer):
        if person1 not in self.customers.values():
            self.bank_details.update({'customer_id_count': self.bank_details.get('customer_id_count') + 1})
            self.customers.update({self.bank_details.get('customer_id_count'): new_customer})

        else:
            print("You are already a member. You are now invited to make an account!")

    def add_account(self, account):
        if account.owner in self.customers.values() and account not in self.accounts.values():
            self.bank_details.update({'account_count': self.bank_details.get('account_count') + 1})
            account.acc_number = self.bank_details.get('account_count') +1
            acc_entry = {self.bank_details.get('account_count'): account}
            self.accounts.update(acc_entry)
            print(f"Hi {account.owner.first_name.capitalize()} {account.owner.last_name.capitalize()}!\n"
                  f"Your {account.acc_type} account number is: {self.bank_details.get('account_count')}")
        elif account in self.accounts.values():
            print(f"Your account is already part of our bank. The account number is {account.acc_number}")
        elif account.owner not in self.customers.values():
            print("Please register with the bank first.")

    def remove_account(self, account):
        self.accounts = {key:val for key, val in self.accounts.items() if val != account}
        print('Your account has been deleted."')

    def deposit_money(self, customer, account, amount):
        pass

    def withdraw_money(self, customer, account, amount):
        pass

    def balance_inquiry(self, customer, account):
        pass

#
#
nick_bank = Bank('nick')
person1 = Person(1, 'nick', 'nilson')
nick_bank.add_customer(person1)
nick_bank.add_customer(person1)
print(nick_bank.bank_details.get('customer_id_count'))
nick_acc = Account("Checking", person1)
nick_acc2 = Account("Savings", person1)
nick_bank.add_account(nick_acc)
nick_bank.add_account(nick_acc2)

