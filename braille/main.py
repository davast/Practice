import argparse
import json
import sys


def start(words: str) -> list:
    out = []
    for word in words.split():
        out.append(word)
    return out

def numbers(words: str) -> list:
    combin = []
    if words[0].isdigit():
        combin.extend(json_["alp"][0]["number"])
        combin.extend(json_["alp"][0][words[0]])
    elif words[0].isupper():
        combin.extend(json_["alp"][0]["CAPS"])
        combin.extend(json_["alp"][0][words[0].lower()])
    else:
        combin.extend(json_["alp"][0][words[0]])

    for item in range(1, len(words)):
        if words[item].isdigit() and words[item - 1].isdigit():
            combin.extend(json_["alp"][0][words[item]])
        elif  words[item].isdigit():
            combin.extend(json_["alp"][0]["number"])
            combin.extend(json_["alp"][0][words[item]])
        else:
            combin.extend(words[item])
    combin.append(json_["alp"][0][" "])
    return combin

def punctuation(words: str) -> list:
    punctuations = ("!","(",")","-","[","]","{","}",";",":")
    for idx, item in enumerate(words):
        if item in punctuations:
            words[idx] = json_["alp"][0][item]
    return words

def lett(words: str) -> list:
    for idx, item in enumerate(words):
        if isinstance(item, str) and item.isupper():
            words[idx] = json_["alp"][0]["CAPS"] + json_["alp"][0][item.lower()]
        elif isinstance(item, str):
            words[idx] = json_["alp"][0][item.lower()]

    return words


def main(string: str) -> list:
    temp = []
    words = start(string)
    for word in words:
        word = numbers(word)
        word = punctuation(word)
        word = lett(word)
        temp.extend(word)
    return temp


def text_to_braille(word: str) -> list:
    final = []
    first_line = []
    second_line = []
    third_line = []
    for item in main(word):
        if isinstance(item[0], list):
            for char in item:
                final.append(char)
        else:
            final.append(item)

    for item in range(0, len(final), 3):
        first_line.append(final[item:item+3][0])
        second_line.append(final[item:item+3][1])
        third_line.append(final[item:item+3][2])

    first_line = first_line[:len(first_line) - 1]
    second_line = second_line[:len(second_line) - 1]
    third_line = third_line[:len(third_line) - 1]


    return "{}\n{}\n{}".format(first_line, second_line, third_line)


def letter_to_braille(word: str) -> list:
    final = []
    first_line = []
    second_line = []
    third_line = []
    for item in main(word):
        if isinstance(item[0], list):
            for char in item:
                final.append(char)
        else:
            final.append(item)

    for item in range(0, len(final), 3):
        first_line.append(final[item:item+3][0])
        second_line.append(final[item:item+3][1])
        third_line.append(final[item:item+3][2])

    first_line = first_line[:len(first_line) - 1]
    second_line = second_line[:len(second_line) - 1]
    third_line = third_line[:len(third_line) - 1]


    return "{}\n{}\n{}".format(first_line, second_line, third_line)


def parsing():
    parser = argparse.ArgumentParser(description="This program is designed to \
    convert English to Braille")
    parser.add_argument("-f", "--file", metavar="", help="Conversion trough \
    .txt file", type=argparse.FileType('r'))
    parser.add_argument("-t", "--text", metavar="", help="Conversion through \
    command line text")
    parser.add_argument("-o", "--output", help="Output the result to a file", \
    type=argparse.FileType('w'))
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    if sys.argv[1] not in ("-f", "-t", "--file", "--text"):
        parser.error("-f or -t is required options for this program")
    args = parser.parse_args()

    if args.file:
        file_content = args.file.read()
        args.file.close()

    if args.text:
        file_content = args.text

    if args.output:
        if args.file:
            args.output.write(str(text_to_braille(file_content)))
            args.output.close()
            return str(text_to_braille(file_content))
        elif args.text:
            args.output.write(str(text_to_braille(file_content)))
            args.output.close()
            return str(text_to_braille(file_content))
    else:
        return str(text_to_braille(file_content))


with open("letter_holder.json") as letter_holder:
    json_ = json.load(letter_holder)

print(parsing())
