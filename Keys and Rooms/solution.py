from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        opened_rooms = [False for i in range(len(rooms))]

        opened_rooms[0] = True

        self.helper(0,opened_rooms, rooms)

        for i in range(len(opened_rooms)):
            if not opened_rooms[i]:
                return False

        return True


    def helper(self, room_to_be_entered: int, opened_rooms : List[bool], rooms: List[List[int]]):

        keys = rooms[room_to_be_entered]

        for key in keys:
            if not opened_rooms[key]:
                opened_rooms[key] = True
                self.helper(key, opened_rooms, rooms)



s = Solution()
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

