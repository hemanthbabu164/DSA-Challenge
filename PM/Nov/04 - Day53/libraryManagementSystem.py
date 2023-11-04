import json

class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1001  # Starting 4-digit ID

    def generate_unique_id(self):
        book_id = self.next_id
        self.next_id += 1
        return book_id

    def add_book(self, book):
        book['id'] = self.generate_unique_id()
        self.books.append(book)
        print(f"Book with ID {book['id']} has been added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} has been removed from the library.")
                return
        print(f"Book with ID {book_id} is not in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

    def view_book_details(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                print("Book details:")
                print(f"ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                if 'price' in book:
                    print(f"Price: ${book['price']}")
                else:
                    print("Price: Not available")
                return
        print(f"Book with ID {book_id} is not in the library.")

def load_sample_data(library):
    with open('sample_data.json', 'r') as file:
        data = json.load(file)
        for book_data in data:
            library.add_book(book_data)

def main():
    library = Library()
    
    load_sample_data(library)
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. List all books")
        print("4. View book details")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            ISBN = input("Enter ISBN: ")
            price = input("Enter price (optional): ")
            
            book = {
                'title': title,
                'author': author,
                'ISBN': ISBN
            }
            if price:
                book['price'] = price
            
            library.add_book(book)
        elif choice == "2":
            book_id = int(input("Enter the ID of the book to remove: "))
            library.remove_book(book_id)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            book_id = int(input("Enter the ID of the book to view details: "))
            library.view_book_details(book_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
