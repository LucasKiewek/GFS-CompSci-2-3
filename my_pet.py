class Pet:

    def __init__(self, name, family, kind, color, quirk):
        self.name = name
        self.family = family
        self.kind = kind
        self.color = color
        self.quirk = quirk

def main():
    name = raw_input("What is your pet's name?\n")
    family = raw_input("Is your pet a mammal, reptile, bird, or insect?\n")
    if family.lower()[0] == "m":
        family = "mammal"
    elif family.lower()[0] == "r":
        family = "reptile"
    elif family.lower()[0] == "b":
        family = "bird"
    elif family.lower()[0] == "i":
        family = "insect"

    q = "What kind of %s is %s?\n" % (family, name)
    kind = raw_input(q)

    q = "What color is %s?\n" % (name)
    color = raw_input(q)

    q = "What is quirky about %s?\n" % (name)
    quirk = raw_input(q)
    peta = Pet(name, family, kind, color, quirk)
    print(peta.name, peta.family, peta.kind, peta.color, peta.quirk)


main()
