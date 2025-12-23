"""
minimum no of days to make M bouquets

we have days in bloom array which gives the no of days will take to bloom the flower
m - no of bouquets we need
k is the no of flowers we need, just we need the adjacent flowers from the array
we cant take random bloomed flowers, to make a bouquet, the no of flowers should be
adjacent
"""


def main(bloomDay, m, k):
    # the impossible case where we have to give -1
    """
    the case is impossible when m * k is greater than the len(bloomday)
    means we dont have much flowers in the array to complete the bouquets
    so return -1
    """
    # tc - O(maxi - min + 1) * O(N)
    #       for loop(min_max)  (this is for possible_flowers)
    if len(bloomDay) < m * k:
        return -1

    for i in range(min(bloomDay), max(bloomDay) + 1):
        if possible_flowers(bloomDay, i, m, k):
            return i

    return -1


def possible_flowers(bloomDay, day, m, k):
    cnt = 0
    no_of_bouquets = 0
    for bloom in bloomDay:
        if bloom <= day:
            cnt += 1
        else:
            no_of_bouquets += cnt // k
            cnt = 0
    # we are doing this as in last when loop ends, need to check if cnt has something
    no_of_bouquets += cnt // k
    if no_of_bouquets >= m:
        return True
    else:
        return False


print(main([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))

# we can optimize this using binary search


def main1(bloomDay, m, k):

    # tc - O(N * log(max-min+1))
    # when sol is impossible
    if len(bloomDay) < m * k:
        return -1
    low = min(bloomDay)
    high = max(bloomDay)

    while low <= high:
        mid = low + ((high - low) // 2)

        if possible_flowers(bloomDay, mid, m, k):
            high = mid - 1

        else:  # if mid is not possible then any no before this is not possible
            low = mid + 1

    return low


print(main1([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
