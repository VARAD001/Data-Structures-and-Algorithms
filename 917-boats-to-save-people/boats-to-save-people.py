class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        L = 0
        R = len(people) - 1
        boats = 0
        while L <= R:
            total_weight = people[L] + people[R]
            if total_weight > limit:
                boats += 1
                R -= 1
            else:
                boats += 1
                R -= 1
                L += 1
        return boats