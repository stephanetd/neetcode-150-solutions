"""
121. Best Time to Buy and Sell Stock

Difficulty: Easy
Topics: Array, Dynamic Programming

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach:
Use Kadane's algorithm to track the minimum price seen so far and calculate the maximum profit at each step.

Key Insights:
1. The maximum profit is the difference between the current price and the minimum price seen so far.

Edge Cases:
1. If the array is empty or has only one element, return 0.

Complexity:
Time: O(n) - where n is the length of the input array, since we process each element once.
Space: O(1) - only using a constant amount of extra space.
"""

def solution(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    # Test cases
    pass
