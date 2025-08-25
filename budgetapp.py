class Category:
    def __init__(self,category):
        self.category=category
        self.ledger=[]
        self.total=0
        self.twithdraw=0
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
        self.twithdraw+=amount
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
    def __str__(self):
        string = ""
        string = string + self.category.center(30, "*") + '\n'
        for action in self.ledger:
            amount = f"{float(action['amount']):.2f}"
            description = str(action["description"])
            description=description[:23]
            string = string + description.ljust(30-len(amount))+ amount + '\n'

        string=string+"Total: "+f"{float(self.total):.2f}"
        return string
    def spent(self):
        return self.twithdraw

def create_spend_chart(categories):
    totalspent=0
    string=""
    category=[]
    string=string+"Percentage spent by category"+'\n'
    for object in categories:
        totalspent+=object.spent()
        category.append(object.spent())
    procents=[]
    for x in category:
        procent=(x*100)/totalspent
        procents.append(procent)
    procents1=[]
    for x in procents:
        x=(x//10)*10
        procents1.append(x)
    for index in range(100,-1,-10):
        string=string+str(index).rjust(3)+"|"
        for k in procents1:
            if k>=index:
                string=string+" o "
            else:
                string=string+"   "
        string=string+'\n'
    string=string+"   "+'-'*(3*len(categories))+'-'+'\n'
    for x in range(categories):
        string=string+"   "






food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)