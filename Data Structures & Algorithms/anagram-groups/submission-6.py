class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]
        seen = defaultdict(list) # key is each unique freq array, val is list of words
        for str in strs:
            freq = [0] * 26
            for char in str:
                freq[ord(char) - ord('a')] += 1
            seen[tuple(freq)].append(str)
            
        return list(seen.values())