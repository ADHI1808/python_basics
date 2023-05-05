arr=eval (input("enter an array:"))
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min = arr[i]
    if arr[i]>max:
        max = arr[i]
print("minimum number:",min)
print("maximum number:",max)
        
