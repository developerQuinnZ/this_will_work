def distance(a, b):
    count = 0
    if len(a) != len(b):
        raise ValueError
    for x, y in zip(a, b):
        if x != y:
            count += 1

    return count
