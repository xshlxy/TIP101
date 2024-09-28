'''
Problem 7:
Imagine you are working on a book review software like Goodreads. Write a function named highest_rated() 
that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. Each dictionary represents
data associated with a book, including its title, author, and rating. 
The function should return the dictionary for the book with the highest rating.
'''
def highest_rated(books):
    if books == None:
        return None
    else:
        highest_book = books[0]
        for book in books:
            if book["rating"] > highest_book["rating"]:
                highest_book=book
    return highest_book
#Example Input:

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))
#Expected Output:
'''
{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}
'''