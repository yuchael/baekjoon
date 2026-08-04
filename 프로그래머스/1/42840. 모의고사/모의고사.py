def solution(answers):
   
    i, j, k = 0, 0, 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    
    for answer in answers:
        if answer == one[i]:
            cnt_1 += 1
            
        i += 1

        if i % 5 == 0:
            i = 0
            
        if answer == two[j]:
            cnt_2 += 1
            
        j += 1

        if j % 8 == 0:
            j = 0
            
        if answer == three[k]:
            cnt_3 += 1
            
        k += 1

        if k % 10 == 0:
            k = 0           
    
    m = max(cnt_1, cnt_2, cnt_3)
    result = []
    
    if cnt_1 == m:
        result.append(1)
    if cnt_2 == m:
        result.append(2)
    if cnt_3 == m:
        result.append(3)
    
    return result