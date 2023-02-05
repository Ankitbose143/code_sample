def decor1(func):
    def inner():
        print("decor1")
        x = func()
        print(x*x)
        return x * x

    return inner


def decor(func):
    def inner2():
        print("decor")
        x = func()
        print(2*x)
        return 2 * x

    return inner2


@decor1
@decor
def num():
    return 10


print(num())