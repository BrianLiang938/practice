import fileinput

class Solution:
    def main():
        file = fileinput.input(files='C:/Users/Brian/git/practice-1/adventofCode2022/day4A.txt')
        counter = 0
        for line in file:
            pairs = line.split(',')
            temp = pairs[0].split('-')
            p1Low = int(temp[0])
            p1High = int(temp[1])
            temp = pairs[1].split('-')
            p2Low = int(temp[0])
            p2High = int(temp[1])
            if (p1Low <= p2Low and p1High >= p2High) or (p2Low <= p1Low and p2High >= p1High):
                print(type(p1Low))
                print(p1Low, p1High, p2Low, p2High)
                counter += 1
        print(counter)


    if __name__ == "__main__":
        main()