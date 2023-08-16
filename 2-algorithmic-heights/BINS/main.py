# Given: 
# Two positive integers n ≤ 105 and m ≤ 105
# a sorted array A[1..n] of integers from −105 to 105
# and a list of m integers −105 ≤ k1, k2, …, km ≤ 105.
# 
# Return: 
# For each ki, output an index 1 ≤ j ≤ n s.t. A[j]=ki 
# or "-1" if there is no such index.

input = open('rosalind_bins.txt', 'r').read()
input = input.split("\n")
output = open('output.txt', 'w')

n = int(input[0])
m = int(input[1])
A = list(map(int, input[2].split()))
k = list(map(int, input[3].split()))

def binary_search(A, k):
    start = 0
    end = len(A) - 1

    while start <= end:
        middle = (start + end) // 2

        if A[middle] == k:
            return middle + 1
        elif A[middle] < k:
            start = middle + 1
        else:
            end = middle - 1

    return -1

for i in k:
    output.write(str(binary_search(A, i)) + " ")