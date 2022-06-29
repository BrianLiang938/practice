class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        maxi = 0
        maxCount = 0
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
            if maxi == freq[ord(task) - ord("A")]:
                maxCount += 1
            elif maxi < freq[ord(task) - ord("A")]:
                maxi = freq[ord(task) - ord("A")]
                maxCount = 1
        partCount = maxi - 1
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength
        availableTasks = len(tasks) - maxi * maxCount
        idles = max(0, emptySlots - availableTasks)
        return len(tasks) + idles