a, b, c = map(float, input("enter 3 sides:").split())
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("the area is:" ,area)

