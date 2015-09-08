#imports
from math import floor


def is_even(x) :
    if x %2 == 0 :
        return True
    else :
        return False

def is_int(x):
    if abs(x - floor(x)) > 0 :
        return False
    else :
        return True

def digit_sum(n):
	# returns sum of digits 
	# assuming input is positive
    x = str(n)
    sum =0
    for item in x:
        sum += int(item)
    return sum

# deletes vowels
def anti_vowel(text) :
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']
    result = text
    for letter in vowel :
        result = result.replace(letter, "")
        print result
    return result

# scrabble score calculator
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word) :
    try:
        word = word.lower()
        total = 0
        for letter in word :
            if letter in score :
                total+=score[letter]
        return total
    except:
    	print "Something's not write with your 'word'"
