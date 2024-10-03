def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    char_counted = char_count(text)
    report(book_path, words, char_counted)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text_string):
    text_list = text_string.split()
    return len(text_list)

def char_count(text_string):
    lowered_string = text_string.lower()
    text_list_lowered = lowered_string.split()
    char_counting = {}    
    for word in text_list_lowered:
        for char in word:
            if char in char_counting:
                char_counting[char] += 1
            else:
                char_counting[char] = 1
    return char_counting

def report(book_path, words_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print("")
    list_char_count = list(char_count.items())
    list_char_count.sort(reverse=True, key=lambda x: x[1])
    for pair in  list_char_count:
        if pair[0].isalpha():
            print(f"The {pair[0]} character was found {pair[1]} times")
    print("--- End report ---")
 
main()

    