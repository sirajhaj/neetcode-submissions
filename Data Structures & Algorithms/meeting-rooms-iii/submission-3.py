class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        rooms = [0]*n
        vacant_rooms = [(i,0)  for i in range(n)]
        heapq.heapify(vacant_rooms)
        used_rooms = []

        meetings.sort(key=lambda x:x[0])

        for meeting in meetings :
            
            while used_rooms and used_rooms[0][0]<= meeting[0]:
                end,room = heapq.heappop(used_rooms)
                heapq.heappush(vacant_rooms,(room,end)) 
            if not vacant_rooms:#delayed
                required_end = used_rooms[0][0]
                while used_rooms and required_end==used_rooms[0][0]:
                    end,room = heapq.heappop(used_rooms)
                    heapq.heappush(vacant_rooms,(room,end))

            room,end = heapq.heappop(vacant_rooms)
            
            if meeting[0] < end : #delayed
                heapq.heappush(used_rooms,(end+meeting[1]-meeting[0],room))   
            else :
                heapq.heappush(used_rooms,(meeting[1],room))
            rooms[room]+=1
        
        max_i,max_v = 0,0
        for i in range(n):
            if rooms[i]> max_v:
                max_v = rooms[i]
                max_i = i
        return max_i










        