"""operadores"""
#operadores aritmeticos
print(f"suma:10+3={10+3}")
print(f"resta:10-3={10-3}")
print(f"multiplicacion:10*3={10*3}")
print(f"division:10/3={10/3}")
print(f"modulo:10%3={10%3}")
print(f"exponente:10**3={10**3}")
print(f"división entera:10//3={10//3}")

#operadores de comparación
print(f"igualdad:10==3 {10==3}")
print(f"desigualdad:10!=3 es {10!=3} ")
print(f"mayor que: 10 > 3 es {10>3}")
print(f"menor que: 10 < 3 es {10<3}")
print(f"mayor o igual que: 10 >= 3 es {10>=3}")
print(f"menor o igual que: 10 <= 3 es {10<=3}")

#operadores logicos
print(f"AND &&:10+5==15 and 10-2=8 es {10+5==15 and 10-2==8}")
print(f"OR ||:10+5==14 or 10-2=7 es {10+5==14 or 10-2==7}")
print(f"NOT !:not 10-2=8 es {not 10-2==8}")

#operadodes de asignación
my_number=2
print(my_number)
my_number+=4
print(my_number)
my_number-=1
print(my_number)
my_number*=2
print(my_number)
my_number/=5
print(my_number)
my_number%=3
print(my_number)
my_number**=2
print(my_number)
my_number//=2
print(my_number)

#operadores de identidad
my_new_number=my_number
print(f"my_number is my_new_number {my_number is my_new_number}")
print(f"my_number is not my_new_number {my_number is not my_new_number}")

#operadores de pertenencia
print(f"'u'in'barco'= {'u'in 'barco'}")
print(f"'c'in'cajas'= {'c'in'cajas'}")

#operadores de bit
a=10  #1010
b=3    #0011
print(f"and: a & b = {a & b}")
print(f"or: a|b ={a|b}")
print(f"xor: a^b = {a^b}")
print(f"not:~10 = {~10}")
print(f"desplazamiento a la derecha: 10>>2 = {10 >> 2}")
print(f"desplazamiento a la izquierda: 10<<2 = {10 << 2}")

"""Estructura de control"""

#consicionales

my_string= "byron"
if my_string == "byron":
    print("my string es byron")
elif my_string == "geovanny":
    print("my string es geovanny")
else:
    print("my string no es byron ni geovanny")

#iterativas

for j in range(11):
    print(j)

i=20
while i<=10:
    print(1)

#manejo de excepciones
try:
    print(10/0)
except:
    print("se ha producido un ellor")
finally:
    print("ha finalizado el manejo de excepciones")

#extra
for i in range (10,56):
    if i %2==0 and i !=16 and i %3!=0:
     print(i)
