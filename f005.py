num1 = float(input('digite um numero: '))
num2 = float(input('digite outro numero: '))
num3 = float(input('digite mais um numero: '))
num4 = float(input('digite o ultimo numero: '))

if num1 < num2 and num1 < num3 and num1 < num4:
    print(num1)
elif num2 < num1 and num2 < num3 and num2 < num4:
    print(num2)
elif num3 < num1 and num3 < num2 and num3 < num4:
    print(num3)
else:
    print(num4)