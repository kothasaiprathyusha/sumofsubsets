arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
ans=[]
for i in range(0,n):
    for j in range(i,n):
        ans.append(arr[i:j+1])
maxlen=0
for lst in ans:
    if(sum(lst)==k):
        if len(lst)>maxlen:
            maxlen=len(lst)
print(maxlen)                 
# i/p 10 5 2 7 1 -10 k=15 o/p=6

