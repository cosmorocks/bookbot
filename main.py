from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    booktext = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_num_words(booktext)} total words")
    print("--------- Character Count -------")
    formatted_num_chars = get_num_chars(booktext)
    sort_num_chars(formatted_num_chars)
    for char in formatted_num_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

if __name__ == "__main__":
    main()