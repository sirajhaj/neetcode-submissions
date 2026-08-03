class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()
        curr = ""
        res = []
        n = len(folder)
        len_curr = 1

        for i in range(n):
            
            if folder[i][:len_curr+1] != (curr+"/") :
                curr = folder[i]
                res.append(curr)
                len_curr = len(curr)

        return res 
        