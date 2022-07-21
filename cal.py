def cal(a,b,op):
    if(op=='+'):
        return(a+b)
    elif(op=='-'):
        return(a-b)
    elif(op=='*'):
        return(a*b)
    elif(op=='/'):
        return(a/b)
a=int(input("First no:"))
b=int(input("Second no:"))
c=input("Enter function:")
print(cal(a,b,c))