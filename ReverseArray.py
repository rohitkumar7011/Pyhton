'''USING TWO POINTER APPROACH...'''
print("Enter the size of array:")
n= int(input())
li = []
for i in range(n):
    li.append((int(input())))
m = 0
n = len(li)-1
while m<n:
    temp = li[m]
    li[m] = li[n]
    li[n] = temp
    m = m+1
    n = n-1
for i in li:
    print(i)