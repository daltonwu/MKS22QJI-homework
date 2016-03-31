import string

def has_digits(p):
    return 1 in [1 for c in p if c in string.digits]

def has_lowercase(p):
    return 1 in [1 for c in p if c in string.ascii_lowercase]

def has_uppercase(p):
    return 1 in [1 for c in p if c in string.ascii_uppercase]


def threshold(p):
    return (
        has_digits(p)
        and has_lowercase(p)
        and has_uppercase(p)
    )

def strength(p):
    level = 0
    level += 1 if has_digits(p)
    level += 1 if has_lowercase(p)
    level += 1 if has_uppercase(p)
    level += len(p)
    return level
