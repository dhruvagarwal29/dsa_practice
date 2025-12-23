"""
The string "PAYPALISHIRING" is written in a zigzag pattern on
a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)


P   A   H   N
A P L S I I G
Y   I   R
"""


def convert(s, noofRows):
    if len(s) == 1:
        return s

    result = [[] for _ in range(noofRows)]
    flip = False
    index = 0

    for c in s:
        result[index].append(c)
