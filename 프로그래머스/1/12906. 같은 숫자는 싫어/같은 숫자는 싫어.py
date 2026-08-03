def solution(arr):
    n = len(arr)
    answer = [arr[0]]
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
        
    return answer