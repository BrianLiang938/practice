import fileinput

class Solution:
    def main():
        file = fileinput.input(files='C:/Users/Brian/git/practice-1/adventofCode2022/day2A.txt')
        current = 0
        counter = 0
        for line in file:
            counter += 1
            input = line.split(' ')
            input[1] = input[1].strip()
            if input[1] == 'Y':
                current += 3
            elif input[1] == "X":
                current += 0
            elif input[1] == "Z":
                current += 6
            else:
                print("fuck you")
                quit
            if (input[0] == 'A' and input[1] == 'Y') or (input[0] == 'B' and input[1] == 'X') or (input[0] == 'C' and input[1] == 'Z'):
                current += 1 
            elif (input[0] == 'A' and input[1] == 'Z') or (input[0] == 'B' and input[1] == 'Y') or (input[0] == 'C' and input[1] == 'X'):
                current += 2 
            elif (input[0] == 'A' and input[1] == 'X') or (input[0] == 'B' and input[1] == 'Z') or (input[0] == 'C' and input[1] == 'Y'):
                current += 3 
        print(current)

    if __name__ == "__main__":
        main()