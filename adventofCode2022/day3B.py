import fileinput

class Solution:
    def main():
        file = fileinput.input(files='C:/Users/Brian/git/practice-1/adventofCode2022/day3A.txt')
        current = 0
        fileArr = []

        for line in file:
            fileArr.append(line)
        print(int(len(fileArr) / 3))
        for i in range(int(len(fileArr) / 3)):
            first = fileArr[3 *i]
            second = fileArr[3 *i+1]
            third = fileArr[3 * i+2]
            dict = set()
            seconddict = set()
            for char in first:
                dict.add(char)
            for char in second:
                seconddict.add(char)
            for char in third:
                if char in dict and char in seconddict:
                    if current == 0:
                        print(char)
                    if char.isupper():
                        current += ord(char) - ord('A') + 27
                    elif char.islower():
                        current += ord(char) - ord('a') + 1
                    break
        print(current)

    if __name__ == "__main__":
        main()