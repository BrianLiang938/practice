import fileinput

class Solution:
    def main():
        file = fileinput.input(files='C:/Users/Brian/git/practice-1/adventofCode2022/day3A.txt')
        current = 0
        for line in file:
            line = line[:-1]
            left = line[:int(len(line) / 2)]
            right = line[int(len(line) / 2):]
            dict = set()
            for char in left:
                dict.add(char)
            for char in right:
                if current == 0:
                    print(ord('p') - ord('a') + 1)
                if char in dict:
                    if char.isupper():
                        current += ord(char) - ord('A') + 27
                    elif char.islower():
                        current += ord(char) - ord('a') + 1
                    break
        print(current)

    if __name__ == "__main__":
        main()