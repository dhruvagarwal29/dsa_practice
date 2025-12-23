# koko eating bananas - return the min integer k such that koko can eat all bananas in
# h hours
# we need to give min no of bananas koko can eat to match h
# piles = [3,6,7,11], h = 8


def require_time(piles, hour):
    total_hours = 0

    for i in piles:
        # to find ceil we can use
        if i % hour == 0:
            temp = i // hour
        else:
            temp = (i // hour) + 1
        total_hours += temp

    return total_hours


def main(piles, h):
    # tc - O(N)
    # sc - O(1)
    for i in range(1, max(piles)):

        req_time = require_time(piles, i)
        if req_time <= h:
            return i


# will use binary search here


def main1(piles, h):
    # tc - O(n) * o(logn)
    low = 1
    high = max(piles)
    ans = 1
    while low <= high:
        mid = low + ((high - low) // 2)

        temp = require_time(piles, mid)

        if temp <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return low


"""
 we can return low ; as low will start from the numbers which
 can not be the answers so it will increase to the optimal sol eventually
"""

print(main([3, 6, 7, 11], 8))
print(main1([3, 6, 7, 11], 8))
