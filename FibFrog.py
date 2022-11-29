#extensive research on:
# Breadth First search Algorithm
#Depth First search Algorithm
def  fibN(N):
    fib=[0]*100
    fib[1]=1
    for i in range(2,100):
        fib[i]=fib[i-1]+fib[i-2]
        if fib[i]>N:
            return fib[2:i]
def solution(A):
    A.append(1)
    fib=fibN(len(A))
    reachsteps=[0]*(len(A))

    #leafs that can be reached in one step
    for j in fib:
        if A[j-1]==1:
            reachsteps[j-1]=1

    #search leafs with more than one step
    for i in range(len(A)):
        if A[i]==0 or reachsteps[i]>0:
            continue

        min_i=-1
        min_v=100000
        for j in fib:
            previousi=i-j
            if previousi<0:
                break
            if reachsteps[previousi]>0 and min_v>reachsteps[previousi]:
                min_v=reachsteps[previousi]
                min_i=previousi
            if min_i!=-1:
                reachsteps[i]=min_v+1
    if reachsteps[len(A)-1]>0:
        return reachsteps[len(A)-1]
    else:
        return-1
    pass
