from flask import Flask, render_template, request
from cs50 import get_string
import itertools
from itertools import permutations

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


tiles = []

dictionary1 = open('dictionary.txt', "r")

dictionary = {}
dictionary = set()
for word in dictionary1:
    if len(word) <= 8:
        dictionary.add(word.rstrip('\n'))

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get("tiles")
        print(text)
        tiles = list(text)
        possible_words = permootations(tiles)
        matching_words = array_maker(possible_words, tiles)
        scores = scorer(matching_words)
        print(matching_words)
        return render_template("scrabble.html", scores=scores)
    else:
        return render_template("index.html")


values = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,
                'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
                's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}



def permootations(tiles):
    for L in range(0, len(tiles)+1): #iterates over the input of the user
        for subset in permutations(tiles, L): #
            wordz_array = [''.join(p) for p in permutations(subset)]
            word_array = sorted(wordz_array)
    return word_array


def array_maker(word_array, tiles):
    res = []
    wordz = []
    found_words = {}
    found_words = set()
    for i in tiles:
        res = [idx for idx in word_array if idx[0].lower() == i.lower()] #creates temp array of all permutations that begin with certain letter
        wordz = [idx for idx in dictionary if idx[0].lower() == i.lower()]
        for word in wordz:
            for item in res:
                if item.startswith(word):
                    found_words.add(word)
    return found_words


def scorer(found_words):
    score = 0
    found_wordz = sorted(found_words, key=len, reverse=True)
    for index, item in enumerate(found_wordz):
        for letter in item:
            value = values.get(letter)
            score = score + value
        found_wordz[index] = item + ": " + str(score)
        print(item)
        score = 0

    return found_wordz
if __name__ == "__main__":
    app.run(debug=True)