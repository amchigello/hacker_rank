k = 1
arr = [[19, 8, 7], [9, 8, 7], [4, 10, 6]]
sorted_arr = sorted(arr, key=lambda x: x[k], reverse=True)
print(arr)
print(sorted_arr)
for x in sorted_arr:
    print(*x)
