class Matlib:

    def main(self):
        name: str = input("Input a name: ")
        place: str = input("Input a place: ")
        noun: str = input("Input a noun: ")
        name2: str = input("Input a name: ")
        noun2: str = input("Input a noun: ")
        name3: str = input("Input a name: ")

        madlib = f"Once upon a time, a silly person named {name} went on a wacky vacation to {place}. " \
                 f"Armed with humor and a trusty {noun}, they embarked on their adventure. " \
                 f"From hilarious belly flops while attempting to surf, to accidentally causing comical chaos in a museum, " \
                 f"{name2} embraced the laughter at every turn. They joined a dance class, leaving everyone in stitches with their goofy moves. " \
                 f"And during a silly scavenger hunt, they stumbled upon unexpected places and a treasure chest filled with " \
                 f"{noun2} balloons. With memories of laughter and silliness, {name3} returned home, cherishing the comical moments of their wacky adventure. " \
                 f"The end."
        print(madlib)


if __name__ == "__main__":
    madlib = Matlib()
    madlib.main()