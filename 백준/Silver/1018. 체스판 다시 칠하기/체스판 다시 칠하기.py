M, N = map(int, input().split())

chess = [] 
for _ in range(M):
    chess.append(list(input()))
    
res = 1e9

for i in range(M-7):
    for j in range(N-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] == "B":
                        white += 1
                    else:
                        black += 1
                else:
                    if chess[k][l] == "W":
                        white += 1
                    else:
                        black += 1
        res = min(white, black, res)

print(res)