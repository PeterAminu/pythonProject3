list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


# def listing(fn, pa):
#     return [fn[s::3] for s in range(pa)]
#
#
# print(listing(list, 3))
#
#
# def split(nums):
#     n = []
#     i = 3
#     for num in range(i):
#         n.append(nums[num::3])
#     return n
#
# print(split(list))
#
#
#
#
def split(nums):
    a = []
    b = 3
    for num in range(b):
        a.append(nums[num::3])
    return a


print(split(list))


# a = []
# b = 3
# for num in range(b):
#     a.append(list[num::3])
# print(a)
