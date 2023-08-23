# Given: 
# A positive integer n≤103
# and an array A[1..n] of integers.
#
# Return: 
# The number of swaps performed by insertion sort algorithm on A[1..n].

input = open("rosalind_ins.txt", "r").read().split("\n")
output = open("rosalind_ins_out.txt", "w")

n = int(input[0])
A = list(map(int, input[1].split()))

def insertion_sort(A):
    swaps = 0

    for i in range(1, len(A)):
        k = i

        while k > 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            swaps += 1
            k -= 1

    return swaps

output.write(str(insertion_sort(A)))
output.close()