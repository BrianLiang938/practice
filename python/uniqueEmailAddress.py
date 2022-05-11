import array
import bisect
import collections
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        processed = set()
        for i in emails:
            new = ""
            plus = 0
            local = 0
            for x in i:
                if local:
                    new += x  
                elif not(plus) and not(local):
                    if x == '+':
                        plus = 1      
                    elif x == '@':
                        local = 1
                        print("Here")
                        new += x             
                    elif x != '.':
                        new += x                  
                elif x == '@':
                    local = 1
                    print("Here")
                    new += x            
            processed.add(new)
        return len(processed)

def main():
    emails = ['test.email+alex@leetcode.com', 'test.email@leetcode.com']
    processed = set()
    for i in emails:
        new = ""
        plus = 0
        local = 0
        for x in i:                     
            if local:
                new += x  
            elif not(plus) and not(local):
                if x == '+':
                    plus = 1      
                elif x == '@':
                    local = 1
                    print("Here")
                    new += x             
                elif x != '.':
                    new += x                  
            elif x == '@':
                    local = 1
                    print("Here")
                    new += x
        processed.add(new)
        print(new)

if __name__ == "__main__":
    main()