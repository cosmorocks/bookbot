def get_num_words(booktext):
    count = len (booktext.split())
    return count

def get_num_chars(booktext):
    # lowercase all characters
    # loop through every single character 
    num_chars = {}
    for character in booktext.lower():
    # if not yet added to dict, add it
        if character not in num_chars:
            num_chars[character] = 1
    # if already in dict, add 1 to current count
        else: 
            num_chars[character] = num_chars.get(character) + 1
    # cleaning up dict (standardizing it)
    num_chars_formatted = []
    for char, count in num_chars.items():
        num_chars_formatted.append({"char":char, "num":count})

    return num_chars_formatted

def sort_on(items):
    return items["num"]

def sort_num_chars(num_chars):
    num_chars.sort(reverse=True,key=sort_on)
    return num_chars