N, M = map(int, input().split())

trees = list(map(int, input().split()))

l, r = 0, max(trees)
while l < r:
    mid = (l+r)//2
    total = sum(tree - mid for tree in trees if tree > mid)
    if total >= M:
        l = mid+1
    else:
        r = mid
        
print(l-1)