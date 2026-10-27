'''a=int(input("Enter a number: "))
for i in range(1, 11):
    print(a*i)'''

'''a=0
while a<=10:
    if (a==7):
        a+=1
        continue
    print(a)
    a+=1'''

'''def sum(a,b):
    return a*b
print(sum(2,3))

print(sum(55,6))'''

'''n= int(input("Enter a number: "))
def a(n):
    b=1
    for c in range(1,n+1):
        b=b*c
    return b
print(a(n))'''

'''for i in range(1, 11):
    print("winnnnnnn")
else:
    print("jeet")
'''

'''print("Enter a number:",end="bbb")'''

'''def a(i):
    if (i==0):
        return 
    print(i)
    a(i-1)
    print("wiiiinnnnnnnnn")

a(10)'''

'''print("tum","" ,end="")
print("bolo")'''

def a(n):
    if (n==0 or n==1):
        return 1
    return a(n-1)*n


print(a(8))

