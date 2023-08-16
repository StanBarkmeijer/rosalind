# Given: 
# A positive integer k ≤2 0
# a positive integer n≤104
# and k arrays of size n containing positive integers not exceeding 105
#
# Return: 
# For each array, output an element of this array occurring strictly more than n/2 times if such element exists, 
# and "-1" otherwise.

input_file = open("rosalind_maj.txt", "r")
input_data = input_file.read().strip().split("\n")
input_file.close()

output_file = open("output.txt", "w")

def majority_element(array):
    elements = array.split(" ")
    elements = [int(element) for element in elements if element != '']  # skip empty strings
    n = len(elements)

    for i in range(n):
        if elements.count(elements[i]) > n / 2:
            return elements[i]
    return -1

for i in range(1, len(input_data)):
    array = input_data[i]
    majority = majority_element(array)
    output_file.write(str(majority) + " ")

output_file.close()