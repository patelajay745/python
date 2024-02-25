n=int(input("Enter the n:"))
mn=int(input("enter minimum:"))
mx=int(input("enter max:"))

for i in range(mn,mx+1):
    if(n%mn==0):
        print(f"{mn} is divisor of {n}")
    mn+=1

