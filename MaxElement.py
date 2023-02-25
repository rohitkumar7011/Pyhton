print("Enter the size of array:")
n= int(input())
li = []
for i in range(n):
    li.append((int(input())))
max = li[0]
m = len(li)
while i<=m-1:
    if li[i] > max:
        max = li[i]
        i = i+1
    i = i+1

print("Max element is ", max)