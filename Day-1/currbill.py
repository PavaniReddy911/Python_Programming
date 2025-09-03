num=int(input("Enter the consumer num\n"))
name=input("Enter the consumer name\n")
pmr=int(input("Enter pmr\n"))
lmr=int(input("Enter lmr\n"))
tu=pmr-lmr
currbill=(tu*3.80)
print(num,name,pmr,lmr,tu,round(currbill,2))
print(num,f"hi {name} your currentbill is {currbill}")