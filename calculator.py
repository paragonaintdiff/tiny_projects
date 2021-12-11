nyan = input("Input first number to calcuate > ")
if nyan.isdigit():
    nyan = int(nyan)
else:
    print("Please input only integer.")
    quit()

mthc = input("Input second number to calculate > " )
if mthc.isdigit():
    mthc = int(mthc)
else:
    print("Please input only integer.")
    quit()

sign = input("Input a sign to calulate add(1),substrat(2),multiply(3) and divide(4) > ")
if sign.isdigit():
    sign = int(sign)
else:
    print("Please input only integer.")
    quit()

if sign == 1:
    print(f"{nyan} + {mthc} is",str(nyan + mthc))
elif sign == 2:
    print(f"{nyan} - {mthc} is",str(nyan - mthc))
elif sign == 3:
    print(f"{nyan} * {mthc} is",str(nyan * mthc))
elif sign == 4:
    print(f"{nyan} / {mthc} is",str(nyan / mthc))
else:
    print("The conditions required did not meet..")