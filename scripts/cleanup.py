from sys import stdin
import string

DISALLOWED = ['½', 'æ', 'ℵ', '!', 'ʼ', '"', '', '[', ']', ',', 'ι']

# r'[a-zA-Z0-9]
for word in stdin.readlines():
    word = word.strip()

    # empty
    if not word:
        continue

    # specifically disallowed symbols
    word = ''.join(filter(lambda c: not c in DISALLOWED, word))

    # non alphanumeric symbols
    word = ''.join(filter(lambda c: c.isalpha(), word))

    # case
    word = ''.join(map(lambda c: c.lower(), word))

    # english and numbers
    word = ''.join(filter(lambda c: not c in string.ascii_letters + string.digits, word))

    print(word)
