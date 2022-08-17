def solution(s):
    a = []
    for x in s:
        if not a:
            a.append(x)
        elif x=='(':
            a.append(x)
        elif x==')' and a[-1]=='(':
            a.pop()
    
    return len(a)==0
