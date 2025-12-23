# stalls = [0,3,4,7,10,9]
# cows = 4


def main(cows, stalls):

    stalls.sort()
    stalls_range = max(stalls) - min(stalls)
    for i in range(1, stalls_range):

        if valid_distance(i, stalls, cows):
            continue
        else:
            return i - 1


def binary_search(cows, stalls):
    stalls.sort()
    low = 1
    high = max(stalls) - min(stalls)

    while low <= high:
        mid = (low + high) // 2

        if valid_distance(mid, stalls, cows):
            low = mid + 1
        else:
            high = mid - 1

    return high


def valid_distance(dis, stalls, cows):

    total_cows = 1
    last_cow = stalls[0]

    for i in range(1, len(stalls)):

        if stalls[i] - last_cow >= dis:
            total_cows += 1
            last_cow = stalls[i]
        else:
            continue

        if total_cows == cows:
            return True

    return False


print(main(4, [0, 3, 4, 7, 10, 9]))
print(binary_search(4, [0, 3, 4, 7, 10, 9]))
