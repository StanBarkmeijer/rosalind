# Given: 
# A positive integer n ≤ 25.
#
# Return: 
# The value of Fn.

def fib(num):
    list = [0, 1]

    for i in range(len(list) - 1, num):
        list.append(list[i] + list[i - 1])

    return list[num]

input = open("rosalind_fibo.txt", "r").read()
output = open("output.txt", "w").write(str(fib(int(input))))