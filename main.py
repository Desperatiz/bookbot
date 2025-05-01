def main():
    book = get_book_text("books/frankenstein.txt")
    count = word_count(book)

    print(f"{count} words found in the document")

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents
    
def word_count(book):
    book_split = book.split()
    words = []

    for word in book_split:
        words.append(word)

    word_count = len(words)
    return word_count
    
main()