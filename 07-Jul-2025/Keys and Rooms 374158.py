# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    from collections import deque
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque()
        visited=set()
        visited.add(0)
        queue.append(0)
        r=1
        while(queue):
            a=queue.popleft()
            for x in rooms[a]:
                if x not in visited:
                    visited.add(x)
                    queue.append(x)
                    r+=1
        return r == len(rooms)
