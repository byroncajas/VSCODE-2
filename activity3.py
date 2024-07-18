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

# Argumento predeterminado
def default_args_greet(name="Pame"):
    print(f"Hola, {name}")
default_args_greet("Pedro")