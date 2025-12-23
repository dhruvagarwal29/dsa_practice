# we need to place cows such that the distance between 2 cows is maximum


def main(stalls, cows):
    # first we need to sort the stalls
    # tc - O(nlogn) + O(max-min(n) * n) ~ O(n^2)
    stalls.sort()

    possible_range = max(stalls) - min(stalls)
    # this is the maximum distnace where i can place 2 cows
    for min_dis in range(1, possible_range):

        if place_cows(stalls, min_dis, cows):
            continue
        else:
            # return the previous min dis till where we can place cows
            return min_dis - 1


def place_cows(stalls, min_dis, cows):
    # we have to place first cow at first stall, to start with it
    cows_counter = 1
    last_cow_position = stalls[0]

    for i in range(1, len(stalls)):

        if stalls[i] - last_cow_position >= min_dis:
            # means if the distnce between current stall and the last stall is
            # greater than the min_dis then place the cow and update the last_cow_position
            cows_counter += 1
            last_cow_position = stalls[i]

            if cows_counter == cows:
                return True
        else:
            continue

    return False


print(main(stalls=[0, 3, 4, 7, 10, 9], cows=4))


def main1(stalls, cows):
    stalls.sort()  # sort the stalls
    low = 1
    high = stalls[-1] - stalls[0]  # max - min

    while low <= high:
        mid = (low + high) // 2

        if place_cows(stalls, mid, cows):
            low = mid + 1  # go to more distances
        else:
            high = mid - 1

    return high


print(main1(stalls=[0, 3, 4, 7, 10, 9], cows=4))
