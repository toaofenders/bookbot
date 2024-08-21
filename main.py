def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_length(text)
    print(text)
    print(f"{num_words} words")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_length(full_text):
    words = full_text.split()
    return len(words)


main()