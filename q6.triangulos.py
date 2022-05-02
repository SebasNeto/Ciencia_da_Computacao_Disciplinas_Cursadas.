a = int(input())
b = int(input())
c = int(input())

soma = b + c 
soma2 = a + c
soma3 = a + b

if (a<soma) and (b<soma2) and (c<soma3):
    if (a == b) and (b == c):
        print("EQUILATERO") 
    elif (a == b) or (b == c) or (a == c):
        print("ISOSCELES")       
    elif (a != b) and (b != c) and (a != c):
        print ("ESCALENO")
else:
    print(a,b,c)
                
