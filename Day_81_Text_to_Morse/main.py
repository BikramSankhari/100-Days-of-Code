import re

exp = re.compile(r"[0-9A-Za-z/?.()\n ]*(, )*[0-9A-Za-z/?.()\n ]*")


def find_char(ch, target):
    index = []
    for i in range(len(target)):
        if target[i] == ch:
            index.append(i)

    return index


def mark_mismatch():
    print("Hint:")
    for i in range(len(lines)):
        if exp.fullmatch(lines[i]):
            continue
        else:
            splits = exp.split(lines[i])
            mismatch_index = []
            taken_care = []
            for char in splits:
                if char != '' and not char in taken_care:
                    to_be_added = find_char(char, lines[i])
                    mismatch_index += to_be_added
                    taken_care.append(char)

            print(f"At line {i + 1}:: {lines[i]}")

            if i > 9:
                print(" "*13, end='')
            else:
                print(" "*12, end='')

            for index in range(len(lines[i])):
                if index in mismatch_index:
                    print("^", end='')
                else:
                    print(" ", end='')

            print('')


def take_input():
    print("Enter the Text (Press 'Enter' with an empty line to Exit):")
    text = []
    while True:
        temp = input()
        if temp == '':
            break
        text.append(temp)

    return text


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '\n': '\n', ' ': '/'}

while True:
    lines = take_input()

    text = '\n'.join(lines)
    if exp.fullmatch(text) and text != '':
        break

    else:
        print("Please Enter valid AlphaNumeric Characters Only!")
        mark_mismatch()

text = text.upper()

for i in range(len(text)):
    if text[i] != ',':
        print(MORSE_CODE_DICT[text[i]], end=' ')
    else:
        print(MORSE_CODE_DICT[', '], end='')
        i += 1
