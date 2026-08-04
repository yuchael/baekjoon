def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        
        subset = array[i - 1:j]
        subset.sort()
        answer.append(subset[k - 1])
        
    return answer