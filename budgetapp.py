class Category:
    def __init__(self,category):
        self.category=category
        self.ledger=[]
        self.total=0
    def check_funds(self,amount):
        if amount>self.total:
            return  False
        return True
    def deposit(self,amount,description=""):
        dictionary={}
        dictionary["amount"]=amount
        dictionary["description"]=description
        self.ledger.append(dictionary)
        self.total+=amount
    def withdraw(self,amount,description=""):
        if self.check_funds(amount)==False:
            return False
        dictionary = {}
        dictionary["amount"] = -amount
        dictionary["description"] = description
        self.ledger.append(dictionary)
        self.total-=amount
        return True
    def get_balance(self):
        return self.total
    def transfer(self,amount,other):
        if self.check_funds(amount)==False:
            return False
        dictionary = {}
        dictionary["amount"] = -amount
        dictionary["description"] =  "Transfer to "+other.category
        self.ledger.append(dictionary)
        self.total-=amount
        dictionary2 = {}
        dictionary2["amount"] = amount
        dictionary2["description"] = "Transfer from " + self.category
        other.ledger.append(dictionary2)
        other.total+=amount
        return True


def create_spend_chart(categories):
    pass