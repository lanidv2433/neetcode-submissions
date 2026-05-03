class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        freq_sorted = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))

        for i in range(k):
            ans.append(list(freq_sorted.keys())[i])
        
        return ans




