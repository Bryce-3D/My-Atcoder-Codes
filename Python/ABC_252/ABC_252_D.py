#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
You only need to store the number of instances of each distinct value.
Then get the sum of all product of counts of 3 distinct values 
which can probably be done by recursioning it out.

Use a hash table (dict) to store the count of each value and iterate 
back out the counts when done.

CHANGE OF PLANS
Use math rather than recursion to get sum of products of triples
'''

#Finds the sum of all products of triples of elements of a list of integers
#Time complexity: O(len(l))
def tripletwise_product_sum(l):
    #Getting the sum of the (3,0,0) exponent terms
    cubes = [i**3 for i in l]
    sum_e_300_terms = sum(cubes)

    #Getting the sum of the (2,1,0) exponent terms
    Sum = sum(l)
    Homu = [ (l[i] ** 2) * (Sum - l[i]) for i in range(len(l)) ]
    sum_e_210_terms = 3 * sum(Homu)

    ans = (Sum**3 - sum_e_300_terms - sum_e_210_terms) // 6
    return ans


n = int(input())
l = [int(i) for i in input().split()]

#If i is in value_counts, value_counts[i] returns the number of instances of i
value_counts = {}
for i in l:
    if i in value_counts:   #Already appeared
        value_counts[i] += 1
    else:             #Hasn't appeared yet
        value_counts[i] = 1

#List of the counts of distinct values only
counts = []
for i in value_counts:
    counts.append(value_counts[i])

print(tripletwise_product_sum(counts))
