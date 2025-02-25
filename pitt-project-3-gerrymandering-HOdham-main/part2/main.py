import dormbuilding as build

def main():
    fname = input("Enter the filename: ")
    dorm_building = build.DormBuilding(fname)

    print("\nBuilding Representation:\n")
    print(dorm_building)

    print("All expected votes:")
    votes = dorm_building.countAllVotes()
    for color, count in votes.items():
        print(f"{color}: {count}")

    print("\nProportional results:")
    proportional = dorm_building.proportionalResults()
    for color, result in proportional.items():
        print(f"{color}: {result}")

    print("\nPredicted results:")
    predicted = dorm_building.calculateExpectedResults()
    for color, result in predicted.items():
        print(f"{color}: {result}")


if __name__ == "__main__":
    main()