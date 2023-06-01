"""Exercise 10-10 (second try)"""

from pathlib import Path


def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than actual count.
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


filenames = [r'Chapter_10\Exercises\the_brothers_karamazov.txt',
             r'Chapter_10\Exercises\the_count_of_monte_cristo.txt',
             r'Chapter_10\Exercises\little_women.txt']
for filename in filenames:
    count_common_words(filename, 'the')
    count_common_words(filename, 'the ')
    print("\n")
