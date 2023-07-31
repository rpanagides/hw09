import pandas as pd
class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = book_list
        self.num_books = num_books
    
    def add_book(self, book_name, book_rating):
        
        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({'book_name':[book_name],
                                     'book_rating':[book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print("Your book has been added to our book list!")
        
        else:
            print("This book is already in the our book list.")
            
    def has_read(self, book_name):
        
        if book_name in self.book_list['book_name'].values:
            return True
        
        else:
            return False
        
    def num_books_read(self):
        
        books_read = len(self.book_list)
        return books_read
    
    def fav_books(self):
        
        favorites = self.book_list.query('book_rating > 3')
        return favorites
    
        
