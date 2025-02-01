from enum import unique
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    report = character_sort(num_characters)
    report.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print(" ")
    for e in report:
        print(f"The '{e["char"]}' character was found {e["num"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
        words = text.split()
        return len(words)

def get_num_characters(text):
    lowered_text = text.lower()
    num_characters = {}
    for c in lowered_text:
        if c in num_characters:
            num_characters[c] += 1
        else:
            num_characters[c] = 1
    return num_characters

def sort_on(report):
    return report["num"]

def character_sort(num_characters):
    sorted = []
    for e in num_characters:
        if e.isalpha():
            char_dict = {"char": e, "num": num_characters[e]}
            sorted.append(char_dict)
        else:
            pass
    return sorted

main()
