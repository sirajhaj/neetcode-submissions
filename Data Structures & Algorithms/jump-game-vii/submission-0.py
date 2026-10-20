class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1' :
            return False
        n = len(s)
        mx = 0
        que = deque()
        que.append(0)
        while que :
            for i in range(len(que)):
                cur = que.popleft()
                for j in range(max(cur+minJump,mx+1),min(cur+maxJump+1,n)):
                    if s[j] == '0':
                        if j == n-1 :
                            return True
                        que.append(j)
                mx = cur + maxJump
        
        return False
        