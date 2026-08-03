from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    
    answer = list((participant - completion).keys())[0]
    return answer