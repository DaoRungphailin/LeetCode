'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        count = 0
        i = 0
        while(amount != 0):
            if amount >= coins[i]:
                print('amount: ',amount)
                # print('coin: ',coins[i])
                amount = amount - coins[i]
                count += 1
            else:
                i += 1
        return count


coin, amount = input('coins = '), input(', amount = ')
obj = Solution()
coins = []
# create coins list
for i in coin:
    if i.isdigit():
        coins.append(int(i))
print(obj.coinChange(coins, int(amount)))
