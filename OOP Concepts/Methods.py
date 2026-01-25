class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,Storage):
        self.RAM =RAM
        self.Storage = Storage

    
    @classmethod
    def get_storage_type(cls):      # cls is first parameter for Class method
        print(f"Storage type = {cls.storage_type}")

    def get_info(self):     # Instance Method - uses Instance attributes 
        print(f"Laptop has {self.RAM} RAM & {self.Storage} {self.storage_type}")# We can also access Class attribute by self 

l1 = Laptop("16gb","1tb")
l2 = Laptop("8gb", "256gb")

l1.get_info()
l2.get_info()
Laptop.get_storage_type()    # Class method can be accessed by Class as well as Objects too
l1.get_storage_type()       # Here its accessed by object


'''Class methods can only access Class attributes but
    Instance methods can access both class as well as Object attributes!!'''