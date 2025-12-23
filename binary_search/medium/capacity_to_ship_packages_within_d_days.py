# we need to ship all the weights, need to find the min capacity


def main(weights, days):
    for weight in range(max(weights), sum(weights)):
        temp = get_min_capacity(weights, weight)
        if temp <= days:
            return weight


def get_min_capacity(weights, ship_capacity):
    # this is the function which is used to find the capacity
    days = 1
    total_weight = 0
    for wt in weights:
        if wt + total_weight > ship_capacity:
            days += 1
            total_weight = wt
        else:
            total_weight += wt

    return days


def main1(weights, day):
    # tc = O(n * log) # sc - O(1)
    # binary search
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) // 2
        capacity = get_min_capacity(weights, mid)

        if capacity <= day:
            high = mid - 1
        else:
            low = mid + 1

    return low


# print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(main1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
