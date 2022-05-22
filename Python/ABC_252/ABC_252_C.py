#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Just record the number of times digit i appears in position j for 0 <= i,j <= 9
Then check how long it'd take to make all end at digit i for 0 <= i <= 9
Then take max

Suppose a digit appears at position i a_i times
Then take the max a_i
If there's a tie, take the largest index among max a_i's
This is the limiting position and will be the time it takes
'''

#Given a list l of length 10 and a number e in l, returns the 
#max index i such that l[i] = e
def max_index_10(l,e):
    for i in range(9,-1,-1):
        if l[i] == e:
            return i


#record[i][j] returns the number of times digit i appears in position j, 
#where both i and j are 0-indexed
record = []
for i in range(10):
    record.append([0 for i in range(10)])

#Process each reel
for Homu in range(int(input())):
    reel = input()
    for pos in range(10):       #Position
        dig = int(reel[pos])    #Digit 
        record[dig][pos] += 1   #Record

#min_time[i] returns the min time taken to make all stop at digit i
min_time = [0 for i in range(10)]

#Solve min_time for each digit
for dig in range(10):
    counts = record[dig]                    #Number of times it appears per position
    max_count = max(counts)                 #Maximum count
    ind = max_index_10(counts, max_count)   #Max index of max count
    time = 10 * (max_count-1) + ind         #Time to handle this limiting factor
    min_time[dig] = time                    #Record in min_time

print(min(min_time))
