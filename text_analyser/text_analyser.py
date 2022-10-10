"""
text_analyser.py: první projekt do Engeto Online Python Akademie
author: Igor Polinskyi
email: igor.polinskyi@gmail.com
discord: Igor P.#5305
"""

from task_template import TEXTS

# List of users
login = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

print("_" * 50)
print("Please log in with your credentials:")
continue_to_analysing = False
username = input("USERNAME: ")
password = input("PASSWORD: ")

# Check if user is in our list of registred users and credentials are correct.
if login.get(username) == password:
    print(f"Welcome to the app, {username}")
    continue_to_analysing = True
else:
    print("Wrong username or password. FINISHING APPLICATION...........")
    quit()
print("_" * 50)


def text_analyser():
    """Analyser go through the text and then prints number of title case, uppercase, lowercase words and numbers."""
    # Variables to count different parameters of text
    global continue_to_analysing
    text = TEXTS[choice - 1]
    words = text.split()
    titlecase = 0
    uppercase = 0
    lowercase = 0
    numeric = 0
    numbers = []
    word_lenghts = {}

    for word in words:
        word = word.strip(" .,")
        if word.istitle():
            titlecase += 1
        if word.isupper():
            uppercase += 1
        if word.islower():
            lowercase += 1
        if word.isnumeric():
            numeric += 1
            numbers.append(int(word))
        word_length = len(word)
        word_lenghts[word_length] = word_lenghts.get(word_length, 0) + 1

    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {titlecase} titlecase words.")
    print(f"There are {uppercase} uppercase words.")
    print(f"There are {lowercase} lowercase words.")
    print(f"There are {numeric} numeric strings.")
    print(f"The sum of all the numbers: {sum(numbers)}")
    # Visual chart
    print(50 * "-")
    LEN = "LEN"
    OCCURENCES = "OCCURENCES"
    NR = "NR."
    print("{:<4}| {:<20}| {}".format(LEN, OCCURENCES, NR))
    print(50 * "-")
    lenghts = list(word_lenghts)
    lenghts.sort()

    for item in lenghts:
        print(f"{item:<4}| {word_lenghts[item] *  '*':<20}| {word_lenghts[item]}")
    print(50 * "-")
    continue_to_analysing = False


while continue_to_analysing:
    print(f"We have 3 texts to be analyzed.")
    number_of_texts = len(TEXTS)
    choice = int(input(f"Enter a number btw. 1 and {number_of_texts} to select: "))
    if 1 <= choice <= number_of_texts:
        print(50 * "-")
        text_analyser()
    else:
        print("\nInvalid character or number. Try once more time.\n")
print(50 * "-")
