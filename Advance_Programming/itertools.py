import itertools, collections

def testFunction(x):
    return x < 40 

def main():
    # cycle iterator can be used
    seq1 = [ "Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    
    # use count to creat a simper counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    # accumulator creats an iterator an accumultes values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))
    
    acc = itertools.accumulate(vals)
    print(list(acc))
    
    # chain functions 
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # drop while and takewhile
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    
if __name__ == "__main__":
    main()
    print(map.__doc__)
    print(collections.__doc__)