n = int(input("Enter the size of the array: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

target = int(input("Enter a number to be searched: "))

count = 0
for num in arr:
    if num == target:
        count += 1

if count > 0:
    print(f"The number appears {count} times in the array.")
else:
    print("The number is not found in the array.")

