n = int(input())

liq = list(map(int, input().split()))
res = 1e9

l, r = 0, n-1

while l < r:
    mix = liq[l] + liq[r]
    if abs(res) > abs(mix):
        res = mix
    
    if mix == 0:
        break
    elif mix > 0:
        r -= 1
    else:
        l += 1

print(res)