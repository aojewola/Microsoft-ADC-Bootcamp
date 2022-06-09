# Microsoft-ADC-Boootcamp
This repo contains solutions to the problem/challenge questions assigned on Data Structure and Algorithms throughout the bootcamp.

Question 1: 
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example:
  Input: nums = [1,1,0,1,1,1]
  Output: 3
  Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Question 2:
Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.
Example:
  Input: nums = [12,345,2,6,7896]
  Output: 2
  Explanation: 
  12 contains 2 digits (even number of digits). 
  345 contains 3 digits (odd number of digits). 
  2 contains 1 digit (odd number of digits). 
  6 contains 1 digit (odd number of digits). 
  7896 contains 4 digits (even number of digits). 
  Therefore only 12 and 7896 contain an even number of digits.

Question 3:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example:
  Input: nums = [-4,-1,0,3,10]
  Output: [0,1,9,16,100]
  Explanation: After squaring, the array becomes [16,1,0,9,100].
  After sorting, it becomes [0,1,9,16,100].

Question 4:
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
  
 Question 5:
 Best time to buy and sell stock
 You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

  Input: prices = [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
  Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
