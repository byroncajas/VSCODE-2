"""funciones definidas por el usuario"""
# Simple

def saludo():
    print("Hola byron")
    
saludo()

# Con retorno
def return_greet():
    return("hola pame")

print(return_greet())

# Con argumento
def arg_greet(name):
    print(f"hola, {name}")
arg_greet("sofy")

# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}")
args_greet("Ola", "Byron")
args_greet(name="Rosy",greet="oli")

# Argumento predeterminado
def default_args_greet(name="Pame"):
    print(f"Hola, {name}")
default_args_greet("Pedro")
default_args_greet()    #por defecto Pame

# Con argumentos y return
def return_args_greet(greet,name):
    return f"{greet},{name} como estás"
print(return_args_greet("oli","Rosy"))

# Con retorno de varios valores
def multiple_return_greet():
    return "Ola","Mundo"
greet,name=multiple_return_greet()
print (greet)
print( name)

#con un numero variable de argumentos

def variable_argument_greet(*names):
    for name in names:
        print (f"hola  {name}")
variable_argument_greet("Rosy","Pame","Sofi","Anita","Byron")

#con un numero variable de argumentos con palabra clave

def variable_argument_greet(**names):
    for key, value in names.items():
        print (f"{value} ({key})")
variable_argument_greet(
    name="Byron",
    age=28,
    country="Ecuador",
    color= "rojo")

# Funciones dentro de funciones
def outer_function():
    def inner_function():
        print("llamada de mi función interna")
    inner_function()
outer_function()

# Funciones del lenguaje (build in)
print(len("Byron"))
print(type(32))
print("Byron".upper())

# Variables locales y globales
global_variable="Python"
print(global_variable)

def hello_python():
    local_var="Que tal"
    print(f"{local_var} {global_variable}")
print(global_variable)
hello_python()
#print(local_var) no se puede por que solo ejecuta variable global

# EXTRA (ejercicio de logica fizz buzz)
def str_float(string1 , string2):
    count=0
    for i in range(31):
        if i%3==0 and i%5==0:
            print(string1,string2)
        elif i%5==0:
            print(string2)
        elif i%3==0:
            print(string1)
        else:
            print(i)
            count+=1
    return count
print(str_float("cadena 1","cadena 2")) 


