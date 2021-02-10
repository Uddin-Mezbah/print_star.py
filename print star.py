print("pattern printing")
num = int(input("Enter num how many rows you want:"))
print("Enter 1 or 0")
bool_val = input("1 for True value or o for False :")
if bool_val=="1":
    pattern = True
    if pattern:
        for i in range(0,num+1):
            print("*"*int(i))

if bool_val == "0":
    pattern = False
    if not pattern:
        for i in range(num,0,-1):
            print("*"*int(i))