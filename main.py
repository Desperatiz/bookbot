def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents
    
main()