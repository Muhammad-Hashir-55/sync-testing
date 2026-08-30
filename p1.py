t = int(input())
ans = []

for i in range(t):
    n = int(input())
    arr= list(map(int,input().split()))
    maxi = max(arr)
    ans.append(maxi*n)



for i in ans:
    print(i)
        