from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        heaviest = len(people) - 1
        lightest = 0

        boats = 0
        while lightest <= heaviest:
            if people[heaviest] + people[lightest] <= limit:
                boats += 1
                heaviest -= 1
                lightest += 1

            else:
                boats += 1
                heaviest -= 1

        return boats


print(Solution().numRescueBoats([1, 3, 3, 4], 4))
