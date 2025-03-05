"""
File Name: books_data_challenge.py
Coder: Ethan Iwama
Purpose: Solution to Books Data Challenge
"""

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]


# Book Rating Checker
#""" # Simple
def check_rating(book):
    if (book.get('rating') > 4.5):
        return True
    else:
        return False
#"""
#""" # Advanced
def check_rating(book):
    if (book.get('rating') <= 4.0):
        return 'low'
    elif(book.get('rating') > 4.5):
        return 'high'
    else:
        return 'medium'
#"""

# Book Rater Tester
for book in books:
    rating = check_rating(book)
    print(book.get('title') + ': ' + str(rating))


# I might finish the rest later