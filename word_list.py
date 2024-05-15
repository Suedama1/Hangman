import random
import csv
wordlist = []

# Open the words.csv file in read mode
words = open('words.csv', 'r')

# Create a CSV reader for the file
reader = csv.DictReader(words)

# Iterate over the rows in the file
for row in reader:

    # Append each row (which represents a word and its definition) to the wordlist
    wordlist.append(row)

# Closes the words.csv file
words.close()

complexWordlist = []

complexWords = open('ComplexWords.csv', 'r')

reader = csv.DictReader(complexWords)
for row in reader:
    complexWordlist.append(row)
complexWords.close()

# Testing wordlist

simpleIndex = random.randint(0, len(wordlist) - 1)
complexIndex = random.randint(0, len(complexWordlist) - 1)


def get_word():
    word = str(wordlist[simpleIndex]["Word"])
    return word.upper()


def word_meaning():
    meaning = str(wordlist[simpleIndex]["Meaning"])
    return meaning


def get_answer():
    word = get_word()
    meaning = word_meaning()
    print(word, meaning)


def get_complexWord():
    word = str(complexWordlist[complexIndex]["Word"])
    return word.upper()


def complex_word_meaning():
    meaning = str(complexWordlist[complexIndex]["Meaning"])
    return meaning


def complex_get_answer():
    word = get_complexWord()
    meaning = complex_word_meaning()
    print(word, meaning)

# Uncomment me to test if it's working!
# get_answer()
# complex_get_answer()
