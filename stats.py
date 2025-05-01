def word_count(book):
    book_split = book.split()
    words = []

    for word in book_split:
        words.append(word)

    word_count = len(words)
    return word_count