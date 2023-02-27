print("enter the size of array:")
n = int(input())
li=[]
print("enter the elements:")
for i in range(n):
    li.append(int(input()))
first  = 0
second = 0
for ch in li:
    if ch > first:
        second = first
        first = ch
    elif ch > second and ch != first:
        second = ch
if second == 0:
    print("no second largest element")

else:
    print("the second largest element is:" , second)