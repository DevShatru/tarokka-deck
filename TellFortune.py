import os
import re
from random import randint
from Constants import COMMON_DECK, HIGH_DECK, FORTUNE_TEXT

# Create lists from the keys of the card decks
CommonDeck = list(COMMON_DECK.keys())
HighDeck = list(HIGH_DECK.keys())

# Dict to track the results of the cards drawn
FORTUNE_RESULTS = {
    "BOOK": {
        "NAME": "",
        "VAL": "",
        "FORTUNE": "",
    },
    "SYMBOL": {
        "NAME": "",
        "VAL": "",
        "FORTUNE": "",
    },
    "SWORD": {
        "NAME": "",
        "VAL": "",
        "FORTUNE": "",
    },
    "ALLY": {
        "NAME": "",
        "FORTUNE": "",
    },
    "LOCATION": {
        "NAME": "",
        "FORTUNE": "",
    },
}

# If the "chosen" value is a string, return as is
# If it's an array, pick a random entry from the array's length
def resolveValue(obj):
    if type(obj) is str:
        return obj
    else:
        return obj[randint(1, len(obj)) - 1]

# Once the card names are final, populate other parameters (VAL, FORTUNE)
def populateResultsDict():
    for resultsKey in FORTUNE_RESULTS:
        if resultsKey in ["BOOK", "SYMBOL", "SWORD"]:
            FORTUNE_RESULTS[resultsKey]["VAL"] = COMMON_DECK[FORTUNE_RESULTS[resultsKey]["NAME"]]["VAL"]
            FORTUNE_RESULTS[resultsKey]["FORTUNE"] = COMMON_DECK[FORTUNE_RESULTS[resultsKey]["NAME"]]["FORTUNE"]
            continue
        FORTUNE_RESULTS[resultsKey]["FORTUNE"] = resolveValue(HIGH_DECK[FORTUNE_RESULTS[resultsKey]["NAME"]][resultsKey])

# Check if the string needs to have a variable replaced and do so
def parseString(string):

    # Early return if underscore isn't found (underscores only used for variables)
    if not "_" in string:
        return string

    # Iterate word-by-word
    stringAsArray = string.split()
    for index in range(len(stringAsArray)):
        word = stringAsArray[index]

        # Not a variable, continure
        if not "_" in word:
            continue
            
        # Strip any special characters except underscore
        word = re.sub(r'[^a-zA-Z0-9_]', '', word)

        # Split variable into parameters, feed them into our results dictionary, and replace the variable with the correct value
        params = word.split("_")
        stringAsArray[index] = stringAsArray[index].replace(word, FORTUNE_RESULTS[params[0]][params[1]])
    return " ".join(stringAsArray)

    
    
# Print a string and wait for input to continue
def printAndPause(string):
    print(string)
    input()

def tell_fortune():

    # Find locations for the three items (Book, Holy Symbol, and Sword), starting with the book and symbol
    FORTUNE_RESULTS["BOOK"]["NAME"] = CommonDeck[randint(1, len(CommonDeck)) - 1]
    FORTUNE_RESULTS["SYMBOL"]["NAME"] = CommonDeck[randint(0, len(CommonDeck)) - 1]

    # If they have the same card, keep re-drawing for the symbol until it's different
    while FORTUNE_RESULTS["BOOK"]["NAME"] == FORTUNE_RESULTS["SYMBOL"]["NAME"]:
        FORTUNE_RESULTS["SYMBOL"]["NAME"] = CommonDeck[randint(0, len(CommonDeck)) - 1]

    # Repeat for the sword, draw cards until we get one that's different from the ones for the book and symbol
    FORTUNE_RESULTS["SWORD"]["NAME"] = CommonDeck[randint(1, len(CommonDeck)) - 1]
    while FORTUNE_RESULTS["BOOK"]["NAME"] == FORTUNE_RESULTS["SWORD"]["NAME"] or FORTUNE_RESULTS["SYMBOL"]["NAME"] == FORTUNE_RESULTS["SWORD"]["NAME"]:
        FORTUNE_RESULTS["SWORD"]["NAME"] = CommonDeck[randint(1, len(CommonDeck)) - 1]

    # Same process with the High Deck to get the cards for the chosen and the showdown location, keep drawing till we get two different cards
    FORTUNE_RESULTS["ALLY"]["NAME"] = HighDeck[randint(1, len(HighDeck)) - 1]
    FORTUNE_RESULTS["LOCATION"]["NAME"] = HighDeck[randint(1, len(HighDeck)) - 1]
    while FORTUNE_RESULTS["ALLY"]["NAME"] == FORTUNE_RESULTS["LOCATION"]["NAME"]:
        FORTUNE_RESULTS["LOCATION"]["NAME"] = HighDeck[randint(1, len(HighDeck)) - 1]

    # Populate results dictionary and run through the fortune with all values replaced
    populateResultsDict()
    for fortuneKey in FORTUNE_TEXT:
        printAndPause(parseString(FORTUNE_TEXT[fortuneKey]))

tell_fortune()