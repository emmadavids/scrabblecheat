from cs50 import get_string
import itertools
from itertools import permutations
# import os
# import requests
# import urllib.parse
# from flask import redirect, render_template, request, session
# from functools import wraps

text = get_string("Input the scrabble letters you want to cheat with: ")
tiles = list(text)


values = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,
                'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
                's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

dictionary1 = open('dictionary.txt', "r")

dictionary = {}
dictionary = set()
for word in dictionary1:
    if len(word) <= 8:
        dictionary.add(word.rstrip('\n'))

def permootations(tiles):
    for L in range(0, len(tiles)+1): #iterates over the input of the user
        for subset in permutations(tiles, L): #
            wordz_array = [''.join(p) for p in permutations(subset)]
            word_array = sorted(wordz_array)
    return word_array


def array_maker(word_array):
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


print("Here is your list of scrabble words and value of letters: ")
def scorer(found_words):
    score = 0
    found_wordz = sorted(found_words, key=len, reverse=True)
    for item in found_wordz:
        for letter in item:
            value = values.get(letter)
            score = score + value
        print(item, ":", score)
        score = 0
    return found_wordz


possible_words = permootations(tiles)
matching_words = array_maker(possible_words)
scores = scorer(matching_words)