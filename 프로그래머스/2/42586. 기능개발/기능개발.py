def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    remain = []
    
    for i in range(n - 1, -1, -1):
        if (100 - progresses[i]) % speeds[i] == 0:
            days = (100 - progresses[i]) // speeds[i]
        else:
            days = (100 - progresses[i]) // speeds[i] + 1
            
        remain.append(days)
    
    count = 1
    time = remain.pop()
    
    while remain != []:        
        if time >= remain[-1]:
            remain.pop()
            count += 1

        else:
            answer.append(count)
            time = remain.pop()
            count = 1
            
    answer.append(count)
    
    return answer