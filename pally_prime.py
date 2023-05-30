
## Check Pally Prime or not???

n=int(input("Enter n value: "))
num=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if num == rev:
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                print("Not Pally Prime")
                break
        else:
            print("Pally Prime")
    else:
        print("Not Pally Prime")
else:
    print("Not Pally Prime")
