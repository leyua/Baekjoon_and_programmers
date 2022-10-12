def solution(s):
    value=0
    for i in range(len(s)):
        if s[i]=="(":
            value+=1
        else:
            value-=1
        if value<0:
            return False
    if value !=0:
        return False 
    return True