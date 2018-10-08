def euler1():
    list = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
    product = 0
    for i in list:
        product += i

    print(product)


def euler4():
    big = 0
    for i in range(999):
        for j in range(999):
            num = i * j
            if str(num) == str(num)[::-1]:
                if num > big:
                    big = num
    print(big)


def main():
    x = raw_input("euler #")
    probs = ["1", "4"]

    while x not in probs:
        x = raw_input("euler #")

    if x == "1":
        euler1()
    elif x == "4":
        euler4()

main()
