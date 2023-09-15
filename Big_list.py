# def big_list(num: int):
#     double = []
#   for i in range (num):
#       double.append(i * 2)
#   return double
#


# def generator_func(n):
#   for x in range(n):
#       yield x
#
# print()
#
#
#
# g = generator_func(100)
# for c in g:
#     pass

# x = range(100)
# print(x)


# x = [i for i in range(100) if i % 2 == 0]
# print(x)


# print(list(big_list(10000)))
#
# a =generator_func(1000)
# next(a)
# next(a)
# next(a)
# print(next(0))


# def design(fn):
#     print("******************")
#     fn()
#     print("******************")
#     return fn
#
# @design
# def show():
#     print("welcome to ace clans")
#


def design(fn):
        print("******************")
        fn()
        print("******************")
        return fn

def show():
        print("welcome to ace clans")


def performance_check(fn):
    def wrap(*args,**kawrgs):
        from time import time
        time1 = time()
        result = fn(*args,**kawrgs)
        time2 = time()
        print(f"It took {time2 - time1} to execute")
        return result
    return wrap


@performance_check
def big_list(num: int):
    double = []
    for i in range(num):
        double.append(i * 2)
    return double


big_list(10000)
