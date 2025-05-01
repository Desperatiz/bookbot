from stats import word_count
from stats import character_count

def main():
    book = get_book_text("books/frankenstein.txt")
    count = word_count(book)
    char_count = character_count(book)

    print(f"{count} words found in the document")
    for char in char_count:
        print(f"'{char}': {char_count[char]}")

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents
        
main()