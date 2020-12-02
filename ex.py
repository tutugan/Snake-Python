def mergelists(a,b):
    finalList=list1+list2
    finalList.sort()
    leng=len(finalList)
    for i in range(leng-2):
        if finalList[i]==finalList[i+1]:
            finalList.pop(i)
    return finalList

def funcsum(list1):
    s=0
    for i in list1:
        s=s+i
    return s

def split(list1):
    evenList=[]
    oddList=[]
    for i in list1:
        if(i%2==0):
            evenList.append(i)
        else:
            oddList.append(i)
    return [evenList,oddList]

def prime_number(x):
    ok=0
    d=2
    if(x>2):
        while d*d<=x:
            if(x%d==0):
                ok=1
            if(x%(x/d)==0):
                ok=1
            d=d+2
    return ok

def prime(list1):
    primeList=[]
    for i in list1:
        ok=prime_number(i)
        if(ok==0):
            primeList.append(i)
    return primeList

def split_also_printed(list1):
    evenList=[]
    oddList=[]
    for i in list1:
        if(i%2==0):
            evenList.append(i)
        else:
            oddList.append(i)
    print(evenList)
    print(oddList)

def sum_list(list1):
    evensum=0
    oddsum=0
    s=0
    for i in list1:
        s=s+i
        if(i%2==0):
            evensum=evensum+i
        else:
            oddsum=oddsum+i
    print(s)
    print(evensum)
    print(oddsum)

def print_primes(list1):
    for i in (list1):
        ok=prime_number(i)
        if(ok==0 and i!=2):
            print(i)



list1=[1,2,3,4]
list2=[4,6,7]
finalList=[]

print_primes(list1)