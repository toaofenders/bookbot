def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_length(text)
    character_count = get_character_count(text)
    sorted_count = sort_character_count(character_count) 
    sorted_count.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words in the document")
    print("")
    for item in sorted_count:
        letter = item["letter"]
        count = item["num"]
        print(f"The letter '{letter}' was found {count} times")
    print(f"--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_length(full_text):
    words = full_text.split()
    return len(words)

def get_character_count(string_text):
    lowered_string = string_text.lower()
    letters= {}
    for char in lowered_string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

def sort_character_count(unsorted_count):
    unsorted_count_list = []
    for letter in unsorted_count:
        if letter.isalpha():
            temp_dict = {"letter": letter, "num": unsorted_count[letter]}
            unsorted_count_list.append(temp_dict)
    return unsorted_count_list


def sort_on(dict):
    return dict["num"]

main()