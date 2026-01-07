S = input()
T = input()

if S == T:
    print(1)
elif len(S) > len(T):
    print(0)
else:  
    while len(S) != len(T):
        if(T[-1] == 'A'):
            T = T[:-1]
        elif(T[-1] == 'B'):
            T = T[:-1]
            T = T[::-1]
    
    if S == T:
        print(1)
    else:
        print(0)
