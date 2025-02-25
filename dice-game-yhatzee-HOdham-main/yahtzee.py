class Yahtzee:
    def __init__(self): 
        self.__scorecard = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Chance": None,
            "Yahtzee": None
        }
        
    def score_lower(self,dice):
        print(self.score_three_of_a_kind(dice))
        print(self.score_four_of_a_kind(dice))
        print(self.score_full_house(dice))
        print(self.score_small_straight(dice))
        print(self.score_large_straight(dice))
        print(self.score_chance(dice))
        print(self.score_yahtzee(dice))

    def score_upper(self,dice):
        for i in range(1, 7):
            total = 0
            for die in dice:
                if die.value == i:
                    total += die.value
            category = {
                1: "Ones",
                2: "Twos",
                3: "Threes",
                4: "Fours",
                5: "Fives",
                6: "Sixes"
            }
            if category[i] in self.__scorecard:
                print(f"{category[i]}: {total}")

    def score_three_of_a_kind(self,dice):
        counts = [0, 0, 0, 0, 0, 0]
        for die in dice:
            counts[die.value() - 1] += 1 #changed to a getter function
        for i in range(len(counts)):
            if counts[i] >= 3:
                total = 0
                for die in dice:
                    total += die.value
                return f"Three of a Kind {total}"
            else:
                return f"Three of a Kind 0"
                

    def score_four_of_a_kind(self,dice):
        counts = [0, 0, 0, 0, 0, 0]
        for die in dice:
            counts[die.value() - 1] += 1 #changed to getter function
        for i in range(len(counts)):
            if counts[i] >= 4:
                total = 0
                for die in dice:
                    total += die.value
                return f"Four of a Kind {total}"
            else:
                return f"Four of a Kind 0"
                

    def score_full_house(self,dice):
        counts = [0, 0, 0, 0, 0, 0]
        for die in dice:
            counts[die.value() - 1] += 1 #changed to getter function
        if 2 in counts and 3 in counts:
            return f"Full House 25"
        else:
             return f"Full House 0"

    def score_small_straight(self,dice):
        dice_values = []
        for die in dice:
            dice_values.append(die.value)
        dice_values.sort() #TypeError: '<' not supported between instances of 'method' and 'method'
        found_straight = False
        for i in range(len(dice_values) - 1):
            if dice_values[i + 1] - dice_values[i] >= 2:
                found_straight = True
                break
        return f"Small Straight: {0 if found_straight else 30}"


    def score_large_straight(self,dice):
        dice_values = []
        for die in dice:
            dice_values.append(die.value)
        dice_values.sort()
        straight_condition = len(set(dice_values)) == 5 and (max(dice_values) - min(dice_values) == 4)
        return f"Large Straight: {40 if straight_condition else 0}"


    def score_chance(self,dice):
        total = 0
        for die in dice:
            total += die.value
        return f"Chance: {total}"
        

    def score_yahtzee(self,dice):
        counts = [0, 0, 0, 0, 0, 0]
        for die in dice:
            counts[die.value - 1] += 1
        return f"Chance: {50 if max(counts) >= 5 else 0}"

    def set_score(self, category, value):
       self.__scorecard[category] = value

    def print_scorecard(self):
        print("╔═══════════════╦═══════╗")
        print(f"║{'Category':<15}║{'Score':^7}║")
        print("╚═══════════════╩═══════╝")
        for category, score in self.__scorecard.items():
            print("╔═══════════════╦═══════╗")
            print(f"║{category or 0:<15}║{score or 0:^7}║")
            print("╚═══════════════╩═══════╝")


