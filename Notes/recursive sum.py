def sum(listy):
    if len(listy) == 1:
        return listy[0]
    elif len(listy) > 1:
        return listy[0] + sum(listy[1:])
    else:
        raise RuntimeError
