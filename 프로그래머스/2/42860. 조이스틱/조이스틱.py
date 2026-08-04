def solution(name):
    answer = 0
    n = len(name)

    for alphabet in name:
        diff = ord(alphabet) - ord('A')
        answer += min(diff, 26 - diff)
        
    # 좌우 이동
    move = n - 1

    for i in range(n):
        next = i + 1

        # 연속된 A 건너뛰기
        while next < n and name[next] == 'A':
            next += 1

        move = min(move,
                   2 * i + (n - next),
                   i + 2 * (n - next))

    answer += move    
    
    return answer