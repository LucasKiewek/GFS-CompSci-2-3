
def main():
    print("1:")

    binary = {1: 1,
              2: 10,
              3: 11,
              4: 100,
              5: 101,
              6: 110}

    binary[7] = 111
    print(binary)

    print("\n2:")

    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    fdic = dict(dic1, **dic2)
    fdic.update(dic3)
    print(fdic)

    print("\n3:")

    num = raw_input("check if number is in the binary dicitonary:\n")
    while not num.isdigit():
        num = raw_input("check if number is in the binary dictionary:\n")
    num = int(num)

    number = binary.get(num)
    if not number:
        print("sorry, the number is not in the binaryonary.")
        add = raw_input("do you want to add it? y/n\n")
        if add[0].lower() == "y":
            print(bin(num))
            binary[num] = int(bin(num)[2:])
        else:
            print("ok")
    else:
        print("the number is in the binaryonary")

    print("\n4:")
    for i in binary:
        print("the value of %i is %i" % (i, binary[i]))

    print("\n5:")

    print("acending:")
    print(sorted(binary.values()))
    print("decending")
    print(sorted(binary.values())[::-1])

    print("\n6:")

    squares = {}
    for i in range(1, 16):
        squares[i] = i**2
    print(squares)


main()
