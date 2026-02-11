# class Store:
#     total_products = 0

#     def __init__(self,name,prize):
#         self.name = name
#         self.prize = prize
#         Store.total_products += 1

        

#     @staticmethod
#     def cal_discount(prize,discount):
#         final_prize = prize - (discount * prize /100) 
#         print(f"Discounted prize = {final_prize}")

# s1 = Store("Hairwash",400)
# s1.cal_discount(400,10)
# s2 = Store("soap",20)
# s3 = Store("toothpaste",30)
# s4 = Store("pen",50)

# print(s1.total_products)


class product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count +=1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total number of products in store is {cls.count}")

    @staticmethod
    def cal_discount(price, percentage):
        final_price = price - (price * percentage / 100)
        print(f"Final price is {final_price}")

p1 = product("Phone", 30_000)
p2 = product("Laptop", 50_000)
p3 = product("TV", 45_000)

p1.get_info()
p1.cal_discount(30_000,15)
p2.get_info()
p2.cal_discount(50_000,12)
p3.get_info()
p3.cal_discount(45_000,10)

product.get_count()