import dormroom as r
    
class DormBuilding:
    def __init__(self, fname):
        self.__rooms = []
        self.__reps = {}
        self.__load(fname)
        
    def __open(self, fname):
        file = None
        valid_file = False
        while not valid_file:
            try:
                file_name = fname
                file = open(file_name, 'r')
                valid_file = True 
            except FileNotFoundError:
                print("File not found.")
                fname = input("Please enter a valid file name: ")
            except Exception as e:
                print(f"Error: {e}")
                break
        return file

    def __parse(self, line):
        floor = []
        for room_data in line.strip().split(','):
            color_abbrev, rep = room_data[0], int(room_data[1:])
            room = r.DormRoom(color_abbrev, rep)
            floor.append(room)
            self.__updateReps(rep, color_abbrev)
        self.__rooms.append(floor)

    def __updateReps(self, rep, color_abbrev):
        color = "Blue" if color_abbrev == "B" else "Gold"
        if rep not in self.__reps:
            self.__reps[rep] = {color: 1}
        else:
            if color not in self.__reps[rep]:
                self.__reps[rep][color] = 1
            else:
                self.__reps[rep][color] += 1

    def __close(self, file):
        if file:
            file.close()

    def __load(self, fname):
        file = self.__open(fname)
        for line in file:
            self.__parse(line)
        self.__close(file)
          
    def __str__(self):
        building_str = ""
        for floor in self.__rooms:
            for room in floor:
                roomstr = str(room)
                building_str += roomstr[0] + roomstr[4:] + ":"
            building_str = building_str[:-1]
            building_str += "\n"
        return building_str