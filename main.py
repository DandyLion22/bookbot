def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    print(f"{num_words} words found in the document")
    print(f"These are the letters and their occurences: {letter_count}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(book_text):
    new_dict = {}
    text_lower = book_text.lower()
    for letter in text_lower:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    return new_dict


main()



