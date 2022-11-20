num = int((input(" enter the number :")))
num1 = 0
num2 = 1
count = 0
while count < num :
    print(num1)
    nth = num1+num2
    num1 = num2
    num2 = nth
    count += 1


