import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        
        value = "The Shining" in exbook.book_list['book_name'].values
        
        # Test
        expected = True
        self.assertEqual(value, expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        exbook.add_book("The Shining", 4)
        
        # Test
        expected = 1
        self.assertEqual(len(exbook.book_list), expected)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        exbook.add_book("The Will to Change", 5)
                
        # Test
        expected = True
        self.assertEqual(exbook.has_read("The Shining"), expected)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        exbook.add_book("The Will to Change", 5)
                
        # Test
        self.assertFalse(exbook.has_read("Lord of the Rings"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        exbook.add_book("The Will to Change", 5)
        exbook.add_book("Lord of the Flies", 2)
                
        # Test
        expected = 3
        self.assertEqual(exbook.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        exbook = BookLover('reanna', 'rkp3em@gmail.com', 'thriller')
        exbook.add_book("The Shining", 4)
        exbook.add_book("The Will to Change", 5)
        exbook.add_book("Lord of the Flies", 2)
                
        # Test
        expected = 2
        self.assertEqual(len(exbook.fav_books()), expected)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
        
        
        