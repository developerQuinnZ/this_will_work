import re
import string

def is_isogram(word):
    first = prep_string_regex(word)
    second = "".join(first)
    fifth = {letter for letter in second}
    sixth = "".join(fifth)

## Used week 1 method to clean strings, but that left me with a list, I am comparing lists,
## but also wanted to compare lengths, first of cleaned up String that has not been run through a set,
## then compared that to the length of the list thats been turned into a string and had duplicates removed, if same word is isogram, if not it's not.

    if len(second) == len(sixth):
        return True
    return False



def prep_string_regex(sentence):
  # different way to prep a string using regex that Yerim suggested
  lowered = sentence.lower()
  sentence_list = re.findall(r"[\w']+", lowered)
  return sentence_list