#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homu = [int(i) for i in input().split()]
n = Homu[0]
k = Homu[1]
tastiness = [int(i) for i in input().split()]    #Tastiness of the foods
dislikes = [int(i)-1 for i in input().split()]   #0-indexed indices of dislikes

max_taste = max(tastiness)   #Maximum tastiness among foods
#Check if any disliked food has max tastiness
safe = True
for i in dislikes:
    if tastiness[i] == max_taste:
        safe = False
        break

if safe:
    print('No')
else:
    print('Yes')
