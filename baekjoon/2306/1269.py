n, m = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
print(len(arr1 - arr2) + len(arr2 - arr1))
