def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_length(text)
    character_count = get_character_count(text)
    print(text)
    print(f"{num_words} words")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_length(full_text):
    words = full_text.split()
    return len(words)

def get_character_count(string_text):
    lowered_string = string_text.lower()
    count = 0
    letters= {}
    for char in lowered_string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters
main()