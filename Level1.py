def occurance(s, n):
    arr = []
    for i in range(n):
        for len in range(i+1, n+1):
            sub = s[i:len]
            print(sub)
            if sub in s:
                arr.append(s[i: len])
    return arr


def solution(s):
    arr_occ = occurance(s, len(s))
    for i in arr_occ:
        for j in range(1, len(s)+1):
            trial = i * j
            if(trial == s):
                return(j)
