def word_count(book):
    book_split = book.split()
    words = []

    for word in book_split:
        words.append(word)

    word_count = len(words)
    return word_count

def character_count(book):
    characters = list(book.lower())
    char_count = {}

    for character in characters:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def sorted_dictionaries(dictionary):
    sorted = []
    for char in dictionary:
        sorted.append({"char": char, "num": dictionary[char]})
    
    def sort_on(dict):
        return dict["num"]

    sorted.sort(reverse=True, key=sort_on)
    return sorted