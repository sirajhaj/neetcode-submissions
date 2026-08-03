class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        email_map = set()
        

        for s in emails :
            cur_str = ""
            i = 0
            plus = False
            while s[i] != '@':
                if s[i] == '+':
                    plus = True
                elif not plus and s[i] != '.' :
                    cur_str += s[i]
                i+=1
            cur_str += s[i:]
            
            if cur_str not in email_map :
                email_map.add(cur_str)
        
        return len(email_map)