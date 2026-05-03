class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        highest = -10000000000

        freq_sorted = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))

        #print(freq_sorted.keys())

        for i in range(k):
            ans.append(list(freq_sorted.keys())[i])
        
        return ans

        # for num, count in freq.items():
        #     if count > highest:
        #         ans.append(num)
        #     else:



