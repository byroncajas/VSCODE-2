"""# Listas
my_list=["Pame","Rosy","Sofy","Byron"]
print(my_list)
my_list.append("Anita")  #inserción
print(my_list)
my_list.remove("Byron")     #borrado
print(my_list)
print(my_list[1])
my_list[0]="Vanessa"     #actualización
print(my_list)
my_list.sort()          #ordenación
print(my_list)

# TUPLAS inmutable(no puede ni se puede mudar)
my_tuple=("Byron","Cajas","28","Carchi")
print(my_tuple[1])      #Acceso
print(my_tuple[3])
print(sorted(my_tuple))     #ordenacion
print(type(my_tuple))

# SETS llaves no se puede ordenar (evita duplicados)
my_set={"Byron","Cajas","28","Carchi"}
my_set.add("Geovanny")              #insercion
my_set.add("Geovanny")
my_set.remove("Cajas")             #eliminacion
print(my_set)
print(type(my_set))

# DICCIONARIO no son ordenados, entre llaves
my_dict={"name":"Byron","last name":"Cajas",
         "age":"28","province":"Carchi"}
my_dict["email"]="byron@gmail.com"      #insercion
my_dict["age"]="29"         #actualizacio
del my_dict["last name"]        #eliminacion

print(my_dict["name"])          #acceso

my_dict=dict(sorted(my_dict.items()))  #ordenacion
print(my_dict)
print(type(my_dict))

"""
# EXTRA

def my_agenda():

    def insert_number():
        phone=input("Introduce el número del contacto: ")
        if phone.isdigit() and len(phone)>0 and len(phone)<=10:
            agenda[name] = phone
        else:
            print("Introduce un número de teléfono válido de menos de 11 digitos")
    agenda={}

    while True:        #bucle
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion=input("Selecciona una opción:")
        
        match opcion: #opcion de coincidencia
            case "1":
                name=input("Introduce el nombre del contacto: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            
            case "2":
                name=input("Introduce el nombre del contacto: ")
                insert_number()
                               
            case "3":
                name=input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_number()
                    
            case "4":
                name=input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")

            case "5":
                print("Saliendo de la agenda")
                break
            case _:         #ninguna
                print("Opción no válida, Elige una opción del 1 al 5.")


my_agenda()

