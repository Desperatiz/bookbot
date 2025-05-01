import sys
from stats import word_count
from stats import character_count
from stats import sorted_dictionaries

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book = get_book_text(sys.argv[1])
    count = word_count(book)
    char_count = character_count(book)
    sorted_dicts = sorted_dictionaries(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for dict in sorted_dicts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents
        
main()