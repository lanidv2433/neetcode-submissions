class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        ans = []
        word_bank = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in word_bank.keys():
                word_bank[sorted_word] = [word]
            else:
                word_bank[sorted_word].append(word)

        for i in word_bank.values():
            ans.append(i)
        return ans

            




        