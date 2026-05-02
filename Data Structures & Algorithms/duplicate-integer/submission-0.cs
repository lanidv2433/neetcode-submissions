public class Solution {
    public bool hasDuplicate(int[] nums) {
        Dictionary<int, int> dic = new Dictionary<int,int>();

        foreach (int num in nums){
            if (!dic.ContainsKey(num)){
                dic[num] = 1;
            }else{
                return true;
            }

        }

        return false;
    }
}
