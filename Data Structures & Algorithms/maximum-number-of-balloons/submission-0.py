class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        
        num_min = count['b']

        for l in "balon" :
            if l == 'l' or l == 'o' :
                num_min = min(num_min,count[l]//2)
            else :
                num_min = min(num_min,count[l])
        return num_min