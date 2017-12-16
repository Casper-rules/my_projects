import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
mx=0
mn=0
for i in range(4):
    mx+=arr[i]
    mn+=arr[5-i-1]
print(str(mn)+' '+str(mx))
