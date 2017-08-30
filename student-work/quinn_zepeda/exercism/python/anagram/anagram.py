def detect_anagrams(string, array):
    lst = []

    for word in array:
        if word.lower() == string.lower():
            continue
        if len(string) != len(word):
            continue
        for letter in word:
            if letter not in string:
                continue

        s = sorted(string.lower())
        w = sorted(word.lower())
        if s == w:
            lst.append(word)
    return lst
