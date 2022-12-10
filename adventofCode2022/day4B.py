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
            inside = p1High - p2Low
            outside = p1Low - p2High
            if (inside <= 0 and outside >= 0) or (inside >= 0 and outside <= 0):
                
                counter += 1
        print(counter)


    if __name__ == "__main__":
        main()