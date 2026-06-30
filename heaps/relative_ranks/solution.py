from typing import List
import heapq

class RelativeRanksSolution:
    def find_relative_ranks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [""] * n

        pq = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(pq)

        position = 1
        while pq:
            s, player_index = heapq.heappop(pq)
            if position == 1:
                res[player_index] = "Gold Medal"
            elif position == 2:
                res[player_index] = "Silver Medal"
            elif position == 3:
                res[player_index] = "Bronze Medal"
            else:
                res[player_index] = str(position)
            position += 1

        return res
