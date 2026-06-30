from typing import List

class CoinChangeSolution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        memo = [-2] * (amount + 1)
        return self._coin_change_helper(coins, amount, memo)

    def _coin_change_helper(self, coins: List[int], amount: int, memo: List[int]) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if memo[amount] != -2:
            return memo[amount]

        min_coins = -1
        for c in coins:
            res = self._coin_change_helper(coins, amount - c, memo)
            if res != -1 and (min_coins == -1 or res < min_coins):
                min_coins = res + 1

        memo[amount] = min_coins
        return min_coins
