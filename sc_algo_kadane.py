def test_function():
    pass


arr = [-4, 8, 1, 6]
m = len(arr) // 2
print(m)
print(arr[:m])
print(arr[m:])

left_max = -2
right_max = 7

sum = 0
right_sum = -100
left_sum = -100

# Traverse the array from the middle to the right
for i in range(m, len(arr)):
    sum += arr[i]
    right_sum = max(right_sum, sum)

sum = 0

for i in range(m - 1, -1, -1):
    sum += arr[i]
    left_sum = max(left_sum, sum)

print(left_sum)
print(right_sum)

cross_max = left_sum + right_sum

print(cross_max)
print(max(cross_max, max(left_max, right_max)))
# left_max = maxSubArraySum(arr[:m])

#     # Find the maximum subarray sum in the right half
# right_max = maxSubArraySum(arr[m:])
