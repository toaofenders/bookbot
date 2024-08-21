def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(text)
    print(f"{len(words)} words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()