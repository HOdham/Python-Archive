import dormbuilding as build
#prints out entier color name not just the first letter.
#23/25


def main():
    fname = input("Enter the filename: ")
    dorm_building = build.DormBuilding(fname)

    print("Building Representation:")
    print(dorm_building)

if __name__ == "__main__":
    main()