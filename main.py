def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    print(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text_string):
    text_list = text_string.split()
    return len(text_list)  

main()

    