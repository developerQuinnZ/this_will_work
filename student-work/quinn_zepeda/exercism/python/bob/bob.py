def hey(string):
    string = string.strip()
    response = ""
    if string is "":
        response = "Fine. Be that way!"
    elif string.isupper():
        response = "Whoa, chill out!"
    elif string[-1] == "?":
        response = "Sure."
    else:
        response = "Whatever."
    return response
