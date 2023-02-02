N = int(input())
result=0
answer=N
while True:
    if N<10:
        N=N*10+N
        result+=1
        if answer==N:
            break
    N=(N%10)*10+(N//10+N%10)%10
    result+=1
    if answer==N:
        break

print(result)
