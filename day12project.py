# - Users should be able to add a book to their reading list by providing a book title,
# an author's name, and a year of publication.
# - The program should store information about all of these books in a Python list.
# - Users should be able to display all the books in their reading list,
# and these books should be printed out in a user-friendly format.
# - Users should be able to select these options from a text menu,
# and they should be able to perform multiple operations without restarting the program.

reading_list = []

def main():
    while True:
        print("Hello there, what would you like to do?")
        print("1. Add book to your reading list.")
        print("2. Display all books in your reading list.")
        print("3. Delete a book from your reading list.")
        choice = input("Enter the number of your desired option (or 'q' to quit): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            delete_book()
        elif choice == "q" or choice == "Q":
            break
        else:
            print("Invalid selection! Please try again.\n")

def add_book():
    book_title = input("\nPlease enter the book's title: ").title().strip()
    author = input("Now enter the author's name: ").title().strip()
    pub_year = int(input("And finally, please enter the year it was published: "))
    book = {
        "title": book_title,
        "author": author,
        "published": pub_year
    }
    reading_list.append(book)
    print(f"Successfully added '{book_title}' to your reading list!\n")
    # print(reading_list)

def display_books():
    if len(reading_list) == 0:
        print("\nYour reading list is empty. Add book? (y/n) ")
        if  input().lower() == "y":
            add_book()
        else: 
            return
    else:
        for i in range(len(reading_list)):
            print(f"{reading_list[i]['title']} by {reading_list[i]['author']}, {reading_list[i]['published']}\n")

def delete_book():
    if len(reading_list) == 0:
        print("\nNo books to delete.\n")
    else:
        display_books()
        book_title = input("\nEnter the book title to delete: ").title().strip()
        for item in reading_list:
            if item["title"] == book_title:
                reading_list.remove(item)
                print(F"{book_title} has been deleted.\n")
            else:
                print("Invalid entry.\n")

main()