# given an string like Twenty One Thousand, should return 21, 000


def main(s):
    ones = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    twos = {"ten": 10, "eleven": 11, "twelve": 12}
    teens = {
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
    }
    numty = {
        "twenty": 20,
        "thirty": 30,
        "fourty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    levels = {"thousand": 1000, "million": 1000000}

    s = s.lower()
    # split s
    array_s = s.split(" ")
    num = 0
    res = 0

    for s in array_s:
        if s in ones:
            num += ones[s]
        if s in twos:
            num += twos[s]
        if s in numty:
            num += numty[s]
        if s == "hundred":
            num = num * 100
        if s in levels:
            res += num * levels[s]
            num = 0

    res = res + num
    return res


print(main("Two hundred"))
print(main("Two hundred twenty one thousand"))
print(main("twelve thousand three hundred fourty five"))
print(main("five"))
print(main("twenty leetcode five"))
print(main("fourty six million"))
print(main("fourty six million five thousand three hundred eighty six"))
