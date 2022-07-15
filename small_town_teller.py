import pickle


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
        self.balance = 0
        # self.details = {'owner': owner, 'acc_type': account_type, 'balance': None}


class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.customers = {}  # ID: name
        self.accounts = {}
        self.bank_details = {'customer_id_count': 0, 'account_count' : 1000}  # may be unnecessary, but we will see when it comes time for persistence

    def add_customer(self, new_customer):
        if new_customer not in self.customers.values():
            self.bank_details.update({'customer_id_count': self.bank_details.get('customer_id_count') + 1})
            self.customers.update({self.bank_details.get('customer_id_count'): new_customer})

        else:
            print("You are already a member. You are now invited to make an account!")

    def add_account(self, account):
        if account.owner in self.customers.values() and account not in self.accounts.values():
            self.bank_details.update({'account_count': self.bank_details.get('account_count') + 1})
            account.acc_number = self.bank_details.get('account_count') +1
            acc_entry = {self.bank_details.get('account_count'): account}
            # self.accounts.update(acc_entry)
            self.accounts[self.bank_details.get('account_count')] = account
            print(f"Hi {account.owner.first_name.capitalize()} {account.owner.last_name.capitalize()}!\n"
                  f"Your {account.acc_type} account number is: {self.bank_details.get('account_count')}")
        elif account in self.accounts.values():
            print(f"Your account is already part of our bank. The account number is {account.acc_number}")
        elif account.owner not in self.customers.values():
            print("Please register with the bank first.")

    def remove_account(self, account):
        # self.accounts = {key:val for key, val in self.accounts.items() if val != account}
        key_to_del = account
        del self.accounts[key_to_del]
        print(f'Your account [number: {account}] has been deleted."')

    # probably a few ways to do this, cloning the acct & recreating it seems wasteful to just update the balance.
    def deposit_money(self, account, amount):
        acct = self.accounts[account]
        acct.balance += amount
        self.accounts.update({account: acct})
        # self.accounts.update({account: })
        print(f"Your deposit of {amount} has been added to account # {account}")
        # print(f"Your new balance is: {self.balance_inquiry(account)}")

    def withdraw_money(self, account, amount):
        acct = self.accounts[account]
        acct.balance -= amount
        self.accounts.update({account: acct})
        # self.accounts.update({account: })
        print(f"You have withdrawn ${amount} from account # {account}")
        print(f"New balance is ${acct.balance}")

    def balance_inquiry(self, account):
        acct = self.accounts[account]
        acc_type = acct.acc_type
        acc_balance = acct.balance
        print(f"Balance for {acc_type} account number {account}:\n"
              f"${acc_balance}")
        # print(f"{balance}") # so it looks better in other methods

    def save_data(self):
        PersistenceUtils.write_pickle(self)

    def load_data(self):
        return PersistenceUtils.load_pickle()


class PersistenceUtils():

    def write_pickle(self,  data_to_pickle):
        with open('persistent_small_town_teller.pickle', 'wb') as f:
            pickle.dump(data_to_pickle, f)

    def load_pickle(self):
        pickle_data = None
        with open('persistent_small_town_teller.pickle', 'rb') as f:
            while True:
                try:
                    pickle_data = pickle.load(f)
                except EOFError:
                    break
        return pickle_data


# nick_bank = Bank('nick')
# person1 = Person(1, 'nick', 'nilson')
# nick_bank.add_customer(person1)
# nick_bank.add_customer(person1)
# print(nick_bank.bank_details.get('customer_id_count'))
# nick_acc = Account("Checking", person1)
# nick_acc2 = Account("Savings", person1)
# nick_bank.add_account(nick_acc)
# nick_bank.add_account(nick_acc2)
# # nick_bank.remove_account(1001)
# nick_bank.deposit_money(1001, 200.60)
# nick_bank.balance_inquiry(1001)
# nick_bank.withdraw_money(1001, 2)