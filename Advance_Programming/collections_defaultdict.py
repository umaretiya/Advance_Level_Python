# collections_defaultdict.py
from collections import defaultdict
# Demonstrate the usage of defaultdict objects


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = {}
    
    # Count the elements in the list
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    # using a collectins
    fruitCounterDict = defaultdict(int)
    for fruit in fruits:
        fruitCounterDict[fruit] += 1

    # lambda with default dict
    fruitCounterLambda = defaultdict(lambda: 100)
    for fruit in fruits:
        fruitCounterLambda[fruit] += 1
        
    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))
        
    for (k, v) in fruitCounterDict.items():
        print(k + ": " + str(v))

    for (k, v) in fruitCounterLambda.items():
        print(k + ": " + str(v))

if __name__ == "__main__":
    main()
