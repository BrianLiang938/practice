import fileinput

class Solution:
    def main():
        file = fileinput.input(files='c:/Users/gener/git/practice/adventofCode2022/day1A.txt')
        print("here")
        max = -1
        second = -1
        third = -1
        curr = 0
        for line in file:
            if line == "\n":
                if curr >= max:
                    max, second, third = curr, max, second
                elif curr >= second:
                    second, third = curr, second
                elif curr >= third:
                    third = curr
                print(max, second, third)
                curr = 0
            else:
                curr += int(line)
        print(max + second + third)
    if __name__ == "__main__":
        main()
