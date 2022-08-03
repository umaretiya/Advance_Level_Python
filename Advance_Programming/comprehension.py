# Demonstrate how to use list comprehensions


def main() ->list:
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquared = list(map(lambda e: e**2, evens))
    print(evenSquared)
    evenfilter = list(map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
    print(evenfilter)
    
    # TODO: Derive a new list of numbers frm a given list
    evencomprehension = [e**2 for e in evens]
    print(evencomprehension)

    # TODO: Limit the items operated on with a predicate condition
    oddcomprehension = [e**2 for e in odds if e > 3 and e < 17 ]
    print(oddcomprehension)

def dict_main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary
    tempDict = {t:(t*9/5) + 32 for t in ctemps if t <= 100}
    print(tempDict)
    print(tempDict[12])
    # TODO: Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    
    newTeam = {k:v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)
    
def set_main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)
    # TODO: build a set of unique Fahrenheit temperatures

    # TODO: build a set from an input source
    sTamp = "The quick brown fox jumped over the lazy dog"
    charsUper = {c.upper() for c in sTamp if not c.isspace()}
    charsLowee = {c.lower() for c in sTamp if not c.isspace()}
    print(charsUper)
    print(charsLowee)
if __name__ == "__main__":
    # main()
    # dict_main()
    set_main()
