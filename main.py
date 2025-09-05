def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(booktext):
    count= len (booktext.split())
    return count

def main():
    booktext = get_book_text("./books/frankenstein.txt")
    print(f"{get_word_count(booktext)} words found in the document")

if __name__ == "__main__":
    main()