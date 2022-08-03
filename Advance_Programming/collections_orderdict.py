# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict
from turtle import st


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    print(sortedTeams)
    # TODO: create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)
    # TODO: Use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print(tm, wl)
    # TODO: What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break
    # TODO: test for equality
    a = OrderedDict({"a":1, "b": 2, "c": 3})
    b = OrderedDict({"a":1, "b": 2, "c": 3})
    c = OrderedDict({"a":1, "c": 3, "b": 2})
    d = {"a":1, "b": 2, "c": 3}
    e = {"a":1, "c": 3, "b": 2}

    print("Equility Test: ", a==b)
    print("Equility Test: ", a==c)
    print("Equility Test: ", a==d)
    print("Equility Test: ", c==d)
    print("Equility Test: ", a==e)
    print("Equility Test: ", d==e)
if __name__ == "__main__":
    main()


