#defining the problem
"""
This program uses dynamic programming. We have n items. Each item has a weight and corresponding value. We have to find the number of items at or under the capacity W that maximize the value and find the solution optimally. The class Item and Capacity describe the attributes name, weight, values and number of items. The function knapsack solves the 0/1 knapsack problem.

Input

We have been given the number of items in the subset that can be achieved at dog height or given capacity. The seconds line shows the capacity which is the the maximum weight limit. The rest of the lines show information in the form name, weight, value.

Output

The first few line contain the names of the items selected as part of the solution and the last line has the maximized solution values of items combined if the weights combined are within the capacity.

Explanation for O(nW) time complexity

n stands for number of items with weight that are being considered and W represents the maximum weight or capacity from 0 to W in the range. There is a loop that iterates from 1 to n(total number of items) in O(n) time. Another loop goes from 1 to W and it takes time of O(W). The time is dependent on the capacity of W. It is not linear time. W increases exponentially along with the time complexity. n*W subproblems are solved to get to solution.
O(nW) is pseudo-polynomial time.

"""
