import json

base_datos = {}
final_programa = False

def registro(bd):
    usuario = input('Ingrese nombre de usuario: ')
    contrasenia = input('Ingrese contraseña: ')
    bd[usuario] = contrasenia

def login(bd):
    usuario = input('Ingrese nombre de usuario: ')
    if len(bd) == 0:
        print('No hay usuarios registrados')
    else:
        for usu in bd:
            if usu == usuario:
                contrasenia = input('Ingrese contraseña: ')
                if bd[usu] == contrasenia:
                    print('Login correcto!')
                    print(f'Bienvenido {usuario}!')
                else:
                    print('Contraseña incorrecta')
            else:
                print('Usuario incorrecto')

def lectura(bd):
    if len(bd) == 0:
        print('No hay usuarios registrados')
    else:
        print('Usuarios:')
        for usuario in bd:
            print(usuario, ' ', bd[usuario])

def exportar(bd):
    with open('base_de_datos.txt', 'w') as file:
        json.dump(bd, file, indent=4)
    print('Datos exportados correctamente!')

def importar(bd):
    with open('base_de_datos.txt', 'r') as file:
        datos = json.load(file)
    for usu in datos:
        bd[usu] = datos[usu]
    print('Datos importados correctamente!')

while not final_programa:
    opcion = input("""
        Presione el número correspondiente para ingresar a la opción:
        1.- Registro de usuario
        2.- Login
        3.- Lectura de Base de Datos
        4.- Importar datos del .txt (Sobreescribe la bd local)
        5.- Exportar datos al .txt (Sobreescribe el .txt)
        6.- Salir
    """)
    
    if opcion == '1':
        registro(base_datos)
    elif opcion == '2':
        login(base_datos)
    elif opcion == '3':
        lectura(base_datos)
    elif opcion == '4':
        importar(base_datos)
    elif opcion == '5':
        exportar(base_datos)
    elif opcion == '6':
        final_programa = True
    else:
        print('Debe ingresar una opción correcta')