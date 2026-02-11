class bankacct:
    def __init__(self,name, balance):
        self._name = name
        self.__balance = balance


    def get_balance(self):# Getter method to return the private value 
        return self.__balance
    
    def set_balance(self, Newbalance):# Setter method to set new private value 
        self.__balance = Newbalance

acc1 = bankacct("Aditya", 1_00_000)

print(acc1._name)
# print(acc1._name,acc1.__balance) ----> ERROR because balance is private 
print(acc1._bankacct__balance) # But Here we can access Private attribute 

print(acc1.get_balance()) 
