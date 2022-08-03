# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    # TODO: deques support the len() function
    print(str(len(d)))
    # TODO: deques can be iterated over
    for elem in d:
        print(elem.upper(), end="  ")

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(5)
    # print(d)
    # TODO: rotate the deque
    print('\n\n')
    print(d)
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()
