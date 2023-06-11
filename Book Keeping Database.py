#================================================Bookstore-bookkeeping Simulator=========================================================
# import SQLlite
import sqlite3

# create database connection
conn = sqlite3.connect('ebookstore.db')

# create books table if it does not exist
conn.execute('''CREATE TABLE IF NOT EXISTS books
             (id INT PRIMARY KEY NOT NULL,
             title TEXT NOT NULL,
             author TEXT NOT NULL,
             qty INT NOT NULL);''')

# populate books table with initial values
conn.execute("INSERT INTO books (id, title, author, qty) VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30);")
conn.execute("INSERT INTO books (id, title, author, qty) VALUES (3002, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40);")
conn.execute("INSERT INTO books (id, title, author, qty) VALUES (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25);")
conn.execute("INSERT INTO books (id, title, author, qty) VALUES (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37);")
conn.execute("INSERT INTO books (id, title, author, qty) VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12);")
conn.commit()

#==================================================Functions===============================================================================
# function to add a book to the database
def add_book():
    id = input("\nEnter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = input("Enter book quantity: ")
    conn.execute(f"INSERT INTO books (id, title, author, qty) VALUES ({id}, '{title}', '{author}', {qty});")
    conn.commit()
    print("Book added successfully.")

# function to update a book in the database
def update_book():
    id = input("\nEnter book ID: ")
    field = input("Enter field to update (title, author, qty): ")
    value = input("Enter new value: ")
    conn.execute(f"UPDATE books SET {field}='{value}' WHERE id={id}")
    conn.commit()
    print("Book updated successfully.")

# function to delete a book from the database
def delete_book():
    id = input("\nEnter book ID: ")
    conn.execute(f"DELETE FROM books WHERE id={id}")
    conn.commit()
    print("Book deleted successfully.")

# function to search for a book in the database
def search_books():
    term = input("\nEnter the name/author of the book or hit 'Enter' to see all.(Add all appropriate punctuation):\n")
    results = conn.execute(f"SELECT * FROM books WHERE title LIKE '%{term}%' OR author LIKE '%{term}%'")
    for row in results:
        print(f"{row[0]} {row[1]} by {row[2]}, Qty: {row[3]}")

#==================================================Main Menu===============================================================================
# display main menu and execute selected option
print("Welcome to the bookstore!")

while True:
    print("\n1 - Enter book")
    print("2 - Update book")
    print("3 - Delete book")
    print("4 - Search books")
    print("0 - Exit")
    choice = input("Enter your choice: ")

# call Functin to add a book
    if choice == '1':
        add_book()

# call fucntion to update a book
    elif choice == '2':
        update_book()

# call function to dellete a book
    elif choice == '3':
        delete_book()

# call function to search for a book
    elif choice == '4':
        search_books()

# close program
    elif choice == '0':
        conn.close()
        print("Goodbye!")
        break

# if condition to let the user know that there is a issue
    else:
        print("Invalid choice. Please try again.")

#================================end======================================