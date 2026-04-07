n = int(input("enter a number"))
if 1<n<10:
    print("valid")
else:
    print("invalid")
    
p = input("enter passward")
if len(p)>=6:
    print("strong")
else:
    print("too weak")
    


email = input("enter mail")
if'@' in email and'.' in email:
    print("valid mail")
else:
    print("invalid mail")
    
