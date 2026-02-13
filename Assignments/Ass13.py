'''Create a class Book with the following attributes:
title
author
list of reviews

And add methods to:
-add a new review
-count reviews
-display all reviews'''

class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self,new_review):
        self.reviews.append(new_review)
        

    def count(self):
        
        print(f"Total Review counts: {len(self.reviews)}")

    def display(self):
        if not self.reviews:
            print("No REVIEWS yet!")
        else:
            print("Reviews:")
            for review in self.reviews:
                print("-", review)
        
b = Book("Alchemist","CJD")
b.add_review("good")
b.add_review("Nice")
b.add_review("Awesomeee")
b.add_review("Mind blowing")
b.count()
b.display()