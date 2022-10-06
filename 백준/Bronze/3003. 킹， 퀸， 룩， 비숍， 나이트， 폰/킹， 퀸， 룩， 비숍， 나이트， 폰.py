a=[x-y for x,y in zip([1,1,2,2,2,8],map(int,input().split()))]
print(str(a).strip("[]").replace(",",""))