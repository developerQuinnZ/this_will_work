def detect_anagrams(string, array):
    lst = []

    for word in array:
        if word == string:
            continue
        if len(string) != len(word):
            continue
        for letter in word:
            if letter not in string:
                continue

        s = set(string)
        w = set(word)
        if len(w) == len(s):
            lst.append(word)
    return lst
