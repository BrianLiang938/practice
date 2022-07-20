class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        word_dict = defaultdict(list)
        for word in words:
            word_dict[word[0]].append(word)
        for char in s:
            word_temp = word_dict[char]
            word_dict[char] = []
            for word in word_temp:
                if len(word) == 1:
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return count