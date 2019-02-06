def binary_search(box, num):
    i = len(box)/2
    times = 4
    while num != box[i-1]:
        if box[i] > num:
            i -= len(box)/times
        else:
            i += len(box)/times
        times *= 2
    return i-1


def main():
    box = range(1, 101)
    num = raw_input("enter a number 1-100: ")
    while not num.isdigit():
        num = raw_input("enter a number 1-100: ")
    num = int(num)

    location = binary_search(box, num)
    print "it is in the index", location


main()
