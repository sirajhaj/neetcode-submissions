class Solution:
    def maxDifference(self, s: str) -> int:

        count = Counter(s)
        max_f = 0
        min_f = float('inf')
        
        for l in count :
            if count[l]%2==1 and  count[l]>max_f :
                max_f = count[l]
            elif count[l]%2==0 and count[l]<min_f :
                min_f = count[l]
        return max_f - min_f
        

                 
