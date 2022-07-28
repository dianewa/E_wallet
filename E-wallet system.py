class xyzcompany:
    def __init__(self, initial_balance=1000):
        self.initial_balance = initial_balance


class user1(xyzcompany):
    def __init__(self, transaction_fee):
        super().__init__()
        self.transaction_fee = transaction_fee
    def fees(self):
        for i in range(1,10000):
          return fees
class user2(xyzcompany):
    def __init__(self, transaction_fee):
        super().__init__()
        self.transaction_fee = transaction_fee

    def fees(self):
        for i in range(10000,100000):
           return 200
class user3(xyzcompany):
    def __init__(self, transaction_fee):
        super().__init__()
        self.transaction_fee = transaction_fee

    def fees(self):
        for i in range(100000,i+1):
         return 1000
w = user2(100000)
b = w.transaction_fee()
print(b)
z = user3(123, 58)
r = z.transaction_fee()
print(r)

