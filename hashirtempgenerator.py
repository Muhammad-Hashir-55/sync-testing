t = int(input())
ans = []

for i in range(t):
    n,m = list(map(int,input().split()))
    s = set()
    for j in range(n):
        x = input()
        s.add(x[0].upper())
    c = True
    for j in range(m):
        x = input()
        for k in x:
            if(k not in s):
                c = False
                break
        if(c == False):
            break
    if(c):
        ans.append('YES')
    else:
        ans.append('NO')

    
    

    ans.append(tot)

    
for i in ans:
    print(i)
        