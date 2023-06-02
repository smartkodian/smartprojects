books = [] # create an empty array to store the books

# Ask the user to add books
while True:
    title = input("Enter book title: ")
    author = input("Enter author Name: ")
    classification = input("Enter book classification: ")
    
    book = {"Title": title, "Author": author, "Classification": classification} # create a dictionary to store the book details
    books.append(book) # add the book to the list 
    
    num_books = len(books) # get the number of books in the list
    print(f"Books List:\n")

    for i, book in enumerate(books):
        print(f"Book No:{i+1} \n Book Title:{book['Title']} \n Author Name: {book['Author']}  \n Book Classification: {book['Classification']}\n")
        print("-------------------------------------------------------\n")

    add_another = input("Do you want to add another book? (Y/N) ").lower()
    if add_another == "n":
        break

# print all the books added by the user
num_books = len(books)
print(f"\nYou have added {num_books} book(s) to your library:")
for i, book in enumerate(books):
    print(f"Book No:{i+1}. \n Book Title:{book['Title']} \n Author Name: {book['Author']}  \n Book Classification: {book['Classification']}\n")
    print("-------------------------------------------------------\n")

# ask the user if want to delete a book
while True:
    delete_book = input("Do you want to delete a book? (Y/N) ").lower()
    if delete_book == "n":
        break
    elif delete_book == "y":
        # get the index of the book to delete
        index = int(input("Enter the number of the book to delete: ")) - 1
        if index >= 0 and index < len(books):
            # delete the book at the specified index
            deleted_book = books.pop(index)
            print(f"{deleted_book['Title']} by {deleted_book['Author']} ({deleted_book['Classification']}) has been deleted from your library.")
            num_books = len(books)
            print(f"You now have {num_books} book(s) in your library.")
        else:
            print("Invalid book number.")
    else:
        print("Invalid input.")

# print all the books in the list after delete
num_books = len(books)
print(f"\nYou have {num_books} book(s) in your library:")
for i, book in enumerate(books):
    print(f"Book No.{i+1}. \n Book Title:{book['Title']} \n Author Name: {book['Author']}  \n Book Classification: {book['Classification']}\n")
    print("-------------------------------------------------------\n")







