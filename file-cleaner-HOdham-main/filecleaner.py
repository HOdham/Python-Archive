#Hendrix Odham
def IsSpace(char):
    return char == ' ' or char == '\t' or char == '\n' or char == '\r' or char == '\f' or char == '\v'

def fileCleaner(fileSpec):
    cleaned_lines = []
    try:
        file = open(fileSpec, 'r')
        for line in file:
            cleaned_line = ''
            for char in line:
                if char.isalpha() or IsSpace(char) or char.isnumeric():
                    cleaned_line += char.lower()
                else:
                    cleaned_line += ' '

            cleaned_words = cleaned_line.split()
            cleaned_lines.append(cleaned_words)

        file.close()
    except FileNotFoundError:
        print(f"File '{fileSpec}' not found.")
        return None

    return cleaned_lines

def saveCleanedToFile(cleaned_lines,outfile):
    try:
        file = open(outfile, 'w')
        for line in cleaned_lines:
                for i in range(len(line)):
                    file.write(line[i])
                    if i < len(line) - 1:
                        file.write(' ')
                file.write('\n')
        print(f"Cleaned file saved to {outfile}")
    except Exception as e:
        print(f"Error saving cleaned file: {e}")

def printCleaned(cleaned_lines):
    for line in cleaned_lines:
        for i in range(len(line)):
            print(line[i], end=' ')
        print()

if __name__ == "__main__":
    fileSpec = "book.txt"
    cleaned_data = fileCleaner(fileSpec)

    if cleaned_data:
        printCleaned(cleaned_data)
        saveCleanedToFile(cleaned_data,"cleaned_file.txt")

