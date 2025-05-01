from stats import word_count

def main():
    book = get_book_text("books/frankenstein.txt")
    count = word_count(book)

    print(f"{count} words found in the document")

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents
        
main()