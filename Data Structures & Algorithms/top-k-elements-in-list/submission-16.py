class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)
        sorted_counter = sorted(counter.items(), key = lambda x:x[1], reverse=True)
        for i in range(k):
            #extracts the key of that very first item.
            res.append(sorted_counter[i][0])
        return res