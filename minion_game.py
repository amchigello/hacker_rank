import re


def calculate_points(substrings, string):
    points = 0
    for word in substrings:
        # print(word + ":" + str(string.count(word)))
        # points += string.count(word)
        x = sum(1 for i in range(len(string)) if string.startswith(word, i))
        #print(word + ":" + str(x))
        points += x
    return points


def minion_game(string):
    xlist = set([string[x:y] for x in range(len(string)) for y in range(len(string) + 1) if string[x:y] != ''])
    # print(xlist)
    kevin_strings = [x for x in xlist if x[0] in ['A', 'E', 'I', 'O', 'U']]
    stuart_strings = [x for x in xlist if x[0] not in ['A', 'E', 'I', 'O', 'U']]
    print(kevin_strings)
    print(stuart_strings)
    k = calculate_points(kevin_strings, string)
    #print("Kevin " + str(k))
    s = calculate_points(stuart_strings, string)
    #print("Stuart " + str(s))
    if k > s:
        print("Kevin " + str(k))
    elif k < s:
        print("Stuart " + str(s))
    else:
        print("Draw")


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
