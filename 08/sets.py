import copy

def union(a, b):
    '''
    Returns: list of all elements that are members of a, b, or both
    '''
    '''union = copy.deepcopy(a)
    for foo in b:
        if foo not in union:
            union.append(foo)
    return union'''
    return a + set_difference(b, a)

def intersection(a, b):
    '''
    Returns: list of all elements that are members of both a and b
    '''
    '''intersection = []
    for foo in a:
        if foo in b:
            intersection.append(foo)
    return intersection'''
    return [foo for foo in a if foo in b]

def set_difference(a, b):
    '''
    Returns: list of all members of a that are not members of b
    '''
    '''set_difference = []
    for foo in a:
        if foo not in b:
            set_difference.append(foo)
    return set_difference'''
    return [foo for foo in a if foo not in b]

def symmetric_difference(a, b):
    '''
    Returns: list of all members of exactly one of a and b
    '''
    return set_difference(a, b) + set_difference(b, a)

def cartesian_product(a, b):
    '''
    Returns: list of all ordered pairs (foo, bar) such that
             foo is in a and bar is in b
    '''
    return [(foo, bar) for foo in a for bar in b]

if __name__ == '__main__':
    a = [1, 2, 3]
    b = ['red', 'white', 3]
    print 'a =', a
    print 'b =', b
    print
    print 'union(a, b) =', union(a, b)
    print 'intersection(a, b) =', intersection(a, b)
    print
    print 'set_difference(a, b) =', set_difference(a, b)
    print 'set_difference(b, a) =', set_difference(b, a)
    print
    print 'symmetric_difference(a, b) =', symmetric_difference(a, b)
    print 'symmetric_difference(b, a) =', symmetric_difference(b, a)
    print
    print 'cartesian_product(a, b) =', cartesian_product(a, b)
