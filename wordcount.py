"""Wordcount exercise

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


def get_words(filename):
    file_handle = open(filename, 'r')

    words = file_handle.readlines()
    words = ' '.join(words)
    words = words.lower()
    words = words.split()

    file_handle.close()

    return words


def word_count(words):
    word_dictionary = {}

    for word in words:
        if word not in list(word_dictionary.keys()):
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    return word_dictionary


def get_word_dictionary(filename):
    words = get_words(filename)
    return word_count(words)
    

def display_words(words, word_dict):
    for word in words:
        print('{} {}'.format(word, word_dict[word]))


def print_words(filename):
    word_dict = get_word_dictionary(filename)
    words = sorted(list(word_dict.keys()))
    display_words(words, word_dict)


def print_top(filename):
    word_dict = get_word_dictionary(filename)
    words = sorted(word_dict, key=word_dict.get, reverse=True)
    display_words(words, word_dict)


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
