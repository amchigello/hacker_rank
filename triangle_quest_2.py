n=3
for i in range(1,n+1):
    # l1=[str(i) for i in range(i+1) if i!=0]+[str(i) for i in reversed(range(i)) if i!=0]
    # print(''.join(l1))
    print(pow(((pow(10,i)-1)//9),2))
