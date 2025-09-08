from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    booktext = get_book_text("./books/frankenstein.txt")
    print(f"{get_num_words(booktext)} words found in the document")
    print(get_num_chars(booktext))

if __name__ == "__main__":
    main()