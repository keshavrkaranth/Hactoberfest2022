lst = input().split(" ")
lst = list(map(int,lst))
lst.sort()
length = len(lst)
key = int(input("plz enter the key: "))
lb = 0
ub = length-1
while(lb<=ub):
    mid = (lb+ub)//2
    if(key==lst[mid]):
        print(f"element found at this position:{mid}")
        break
    elif(key<lst[mid]):
        ub = mid-1
    else:
        lb = lb+1
if(lb>ub):
    print("element not found")