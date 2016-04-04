def repeat(s):
    def n_times(n):
        return n * s
    return n_times

def r1(n):
    return repeat('hello')(n)

def r2(n):
    return repeat('goodbye')(n)

def main():
    print '>>> r1(2)'
    print r1(2)
    print '>>> r2(2)'
    print r2(2)
    print '>>> repeat("cool")(3)'
    print repeat("cool")(3)

if __name__ == '__main__':
    main()
