'''
  Universidad del Valle de Guatemala
  Bases de datos 1
  Proyecto 2

  Integrantes:
    - Gabriel Vicente 20498
    - Maria Isabel Solano 20504
    - Christopher García 20541
'''

#librerias
from getpass import getpass
from logging import exception
from sympy import true
from Funciones import *
from ConnectionBD import *

#Funciones que seran añadidas luego al documento Funciones
def obtenerData(entidad, offset):
    #Realizar query
    Conseguir_Data(entidad, offset)
    data = ''#Ingresar lista con toda la informacion
    return data

'''
Genera un codigo Concatendando las primeras 3 letras del nombre
 de la entidad y el numero correspondiente dependiendo de la cantidad de
 datos que se encuentran ingresados en la tabla correspondiente (count)
'''
def GenerarCodigo(entidad):
    #Obtener data de la base de datos
    cant = Gen_code(entidad)
    codigo = str(entidad)[0:3] + str(cant)
    return codigo

'''
Agregar contenido hace cambios en las siguientes entidades
- 
'''
def AgregarContenido():
    #Parte 1, datos generales - Tabla Peliculas
    codigo_pel = GenerarCodigo('Peliculas')
    titulo = input('Titulo: ')
    genero = input("Genero: ")
    duracion= 0
    verificador_num = True
    while (verificador_num):
        try:
            duracion = int(input("Duracion: "))
            verificador_num = False #salir del verificador
        except:
            escritura_lenta('Ingrese un numero valido')
    anio = 0
    verificador_num = True
    while(verificador_num):
        try:
            anio = int(input("Año: "))
            verificador_num = False
        except:
            escritura_lenta('Ingrese un numero valido')
    '''INGRESAR A LA BASE DE DATOS'''
    Upload_Peliculas(codigo_pel, titulo, genero, anio, duracion)

    #Parte 2, directores - Tablas directores y director_pelicula
    permanecer = True
    while (permanecer):
        escritura_lenta('\n¿Desea ingresar un(otro) director? ')
        otro = input('(y/n): ')
        
        if (otro == 'y'):
            verificador_director = True
            while (verificador_director): 
                director = input('Nombre del director: ')
                existencia = Get_Director(director)
                if (existencia):
                    #Ya existe en la base de datos
                    codigo_director = existencia[0]
                    '''
                    Ingresar a la BD director_pelicula el codigo del 
                    director y el codigo de la pelicula
                    '''
                    Upload_DirectoresPeliculas(codigo_pel, codigo_director)
                    print("Director(es) ingresado(s) exitosamente")
                    verificador_director = False
                else:
                    escritura_lenta('El director ingresado no existe, desea ingresarlo nuevamente o crear un usuario')
                    escritura_lenta('1) Añadirlo')
                    escritura_lenta('2) Ingresarlo nuevamente\n')
                    oppp = input('Opcion: ')
                    if (oppp == '1'):
                        #Crear dato en la base de datos
                        codigo_director = GenerarCodigo('directores')
                        '''
                        Ingresar a la tabla directores, nombre y codigo
                        Ingresar a la tabla director_pelicula el codigo del
                        director y el codigo de la pelicula
                        '''
                        Upload_Directores(codigo_director, director)
                        Upload_DirectoresPeliculas(codigo_pel, codigo_director)
                        print("Director(es) ingresado(s) exitosamente")
                        verificador_director = False     

        elif (otro == 'n'):
            #Salir de ingresar directores y continuar
            permanecer = False

        else: 
            #Error
            escritura_lenta('Ingrese una respuesta valida\n')

    #Parte 3. Actores - Tablas Actores y Actores_peliculas
    permanecer = True
    while (permanecer):
        escritura_lenta('\nDesea ingresar el nombre de un actor? ')
        otro = input('(y/n): ')

        if (otro == 'y'):
            verificar_actor = True
            while (verificar_actor):
                actor = input('Nombre del actor: ')
                existencia = Get_Actor(actor)
                if (existencia):
                    #Ya existe en la base de datos
                    codigo_actor = existencia[0]
                    '''
                    Ingresar a la tabla Actor_Pelicula (codigo_pelicula, codigo_actor)
                    '''
                    Upload_ActoresPeliculas(codigo_pel, codigo_actor)
                    print("Actor(es) ingresado(s) exitosamente")
                    verificar_actor = False
                else:
                    escritura_lenta('El actor ingresado no existe, desea ingresarlo nuevamente o crear un usuario')
                    escritura_lenta('1) Añadirlo')
                    escritura_lenta('2) Ingresarlo nuevamente\n')
                    oppp = input('Opcion: ')
                    if (oppp == '1'):
                        #Crear dato en la base de datos
                        codigo_actor = GenerarCodigo('actores')
                        '''
                        Ingresar a la tabla actores (codigo y nombre)
                        '''
                        '''
                        Ingresar a la tabla actores_peliculas (codigo y codigo_pelicula)
                        '''
                        Upload_Actores(codigo_actor, actor)
                        Upload_ActoresPeliculas(codigo_pel, codigo_actor)
                        print("Actor(es) ingresado(s) exitosamente")
                        verificar_actor = False
                        
        elif (otro == 'n'):
            #Salir de ingresar actores y continuar
            permanecer = False
        else :
            #Error
            escritura_lenta('Ingrese una respuesta valida\n')

    #Parte 4, Premiaciones - Tabla premiaciones
    permanecer = True
    while (permanecer):
        escritura_lenta('\nLa pelicula ha recibido algun(os) premio(s)? ')
        otro = input('(y/n): ')
        if (otro == 'y'):
            premiacion = input('Premiacion: ')
            reconocimiento = input('Reconocimiento: ')
            verificador_fecha = True
            fecha = ''
            while (verificador_fecha):
                fecha = input("Fecha (YYYY-MM-DD): ")
                if (Check_Date(fecha)):
                    #se puede continuar
                    verificador_fecha = False
                else: 
                    escritura_lenta('Ingrese una fecha valida')

            '''
            Ingresar a la BD, a la tabla premiaciones codigo_pelicula, 
             premiacion, reconocimiento y fecha
            '''
            Upload_Premiaciones(codigo_pel, premiacion, reconocimiento, fecha)
            print("Premiacion ingresada exitosamente")
            permanecer = False
        elif (otro == 'n'):
            #Salir de ingresar premios y continuar
            permanecer = False
        else:
            #Error
            escritura_lenta('Ingrese una respuesta valida \n')

'''
Permite hacer cambios en el contenido
'''
def ModContenido_pelicula():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar')
            print()
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Peliculas', offset)
                        escritura_lenta('Pagina: '+ str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_pel = input('Codigo pelicula: ')
                    if (Get_Movie(cod_pel)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Titulo')
                                escritura_lenta('2) Genero')
                                escritura_lenta('3) Año')
                                escritura_lenta('4) Duracion')
                                escritura_lenta('5) Cancelar')
                                print()
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                print()
                                
                                if(dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        cambiarlo en la base de datos 
                                    '''
                                    Modificar_Pelicula('titulo', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 2):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        cambiarlo en la base de datos
                                    '''
                                    Modificar_Pelicula('genero', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 3):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input("Nuevo año: "))
                                            verificador_num = False
                                        except:
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Obtener nuevo dato del usuario y
                                        cambiarlo en la base de datos
                                    '''
                                    Modificar_Pelicula('YearP', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 4):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input("Nueva duracion: "))
                                            verificador_num = False
                                        except:
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Obtener nuevo dato del usuario y
                                        cambiarlo dato en la base de datos
                                    '''
                                    Modificar_Pelicula('Duracion', nuevoDato, cod_pel)
                                
                                elif(dato_mod == 5):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False
                                
                                else:
                                    escritura_lenta('La opcion ingresada no es valida')
                                      
                            except Exception as ex:
                                #print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('La pelicula ingresada no existe')
                        escritura_lenta('Desea volver a escribir el codigo? ')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except Exception as ex:
            print(ex)
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Permite elimiar peliculas
'''
def Eliminar_pelicula():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar')
            print()
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Peliculas', offset)
                        escritura_lenta('Pagina: '+str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_pel = input('Codigo pelicula: ')
                    if (Get_Movie(cod_pel)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            escritura_lenta('¿Seguro que desea eliminar la pelicula? ')
                            confirm = input('(y/n): ')
                            if (confirm == 'y'):
                                '''
                                Ejecutar query para eliminar contenido con ese nombre!
                                '''
                                Delete_Pelicula(cod_pel)
                                print("Pelicula eliminada exitosamente")
                                permanecer3 = False
                                permanecer2 = False
                                
                            elif (confirm == 'n'):
                                #cancelar la eliminacion de la pelicula escrita
                                permanecer3 = False
                                permanecer2 = False
                            else: 
                                #Error
                                print("La opcion ingresada no existe")
                    else:
                        #no existe
                        escritura_lenta('La pelicula ingresada no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
                
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Agrega Anunciantes a la tabla Anunciantes
'''
def Agregar_Anunciantes():
    codigo_anunciante = GenerarCodigo('anunciantes')
    nombre = input('Nombre anunciante: ')
    '''
    Agregar Anuncainte a la tabla anunciantes
    '''
    Upload_Anunciantes(codigo_anunciante, nombre)
    print("Anunciante agregado con exito")

def ModAnunciantes():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anunciantes')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anunciantes', offset)
                        escritura_lenta('Pagina: '+str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo Anunciante: ')
                    if (Get_Anunciante(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) Nombre')
                                escritura_lenta('2) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_Anunciantes('nombre', nuevoDato, cod_an)
                                    print("Anunciante modificado exitosamente")
                                    permanecer3 = False
                                    permanecer2 = False
                                    
                                elif(dato_mod == 2):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El anunciante ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

def EliminarAnunciantes():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anunciantes')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver anuncios
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anunciantes', offset)
                        escritura_lenta('Pagina: '+str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Eliminar con codigo
                Codigo_anunciante = input('Ingrese el codigo del anunciante: ')
                Delete_Anunciante(Codigo_anunciante)
                print("Anunciante eliminado exitosamente")

            elif (op == 3):
                #salir
                permanecer = False
        except Exception as ex:
            print(ex)
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Agrega Anuncions a la tabla Anuncios
'''
def Agregar_Anuncios():
    permanecer = True
    while (permanecer):
        cod_anuncio = GenerarCodigo('anuncios')
        anunciante = input('Codigo del anunciante: ')
        existencia = Get_Anunciante(anunciante)
        if (existencia):
            #existe
            cod_anunciante = existencia[0]
            contenido = input('Contenido de anuncio: ')
            duracion = 0
            verificador_num = True
            while (verificador_num):
                try:
                    duracion = int(input('Duracion: '))
                    verificador_num = False
                except:
                    escritura_lenta('Ingrese una respuesta valida\n')
            Link = input('Link del contenido: ')
            #salir de la funcion
            Upload_Anuncios(cod_anuncio, cod_anunciante, duracion, contenido, Link)
            print("Anuncio agregado exitosamente")
            permanecer = False
        else:
            escritura_lenta('El anunciante no existe')
            escritura_lenta('Desea escribir nuevamente el nombre del anunciante? \n')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

def ModAnuncios():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver anuncios')
            escritura_lenta('2) Modificar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver contenido
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anuncios', offset)
                        escritura_lenta('Pagina: '+str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Modificar con codigo
                permanecer2 = True
                while (permanecer2):
                    cod_an = input('Codigo Anuncio: ')
                    if (Get_Anuncio(cod_an)):
                        #existe
                        permanecer3 = True
                        while (permanecer3):
                            try:
                                escritura_lenta('\nQue dato desea modificar?: ')
                                escritura_lenta('1) ContenidoPromocional')
                                escritura_lenta('2) Link')
                                escritura_lenta('3) Duracion')
                                escritura_lenta('4) Cancelar\n')
                                nuevoDato =''
                                dato_mod = int(input('Dato: '))
                                
                                if (dato_mod == 1):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos 
                                    '''
                                    Mod_Anuncios('contenidopromocional', nuevoDato, cod_an)
                                    print("Anuncio modificado exitosamente")
                                    permanecer3 = False
                                    permanecer2 = False
                                elif (dato_mod == 2):
                                    nuevoDato = input('Nuevo: ')
                                    '''
                                        Cambiar en la base de datos
                                    '''
                                    Mod_Anuncios('Link', nuevoDato, cod_an)
                                    print("Anuncio modificado exitosamente")
                                    permanecer3 = False
                                    permanecer2 = False
                                elif(dato_mod == 3):
                                    verificador_num = True
                                    while (verificador_num):
                                        try:
                                            nuevoDato = int(input("Nueva duracion: "))
                                            verificador_num = False
                                        except Exception as ex:
                                            print(ex)
                                            escritura_lenta('Ingrese un dato valido')
                                    '''
                                        Cambiar en la base de datos
                                    '''
                                    Mod_Anuncios('duracion', nuevoDato, cod_an)
                                    print("Anuncio modificado exitosamente")
                                    permanecer3 = False
                                    permanecer2 = False
                                elif(dato_mod == 4):
                                    escritura_lenta('[Cancelando...]\n')
                                    permanecer3 = False
                                    permanecer2 = False

                                else:
                                    escritura_lenta('La opcion ingresada no es valida')  
                            except Exception as ex:
                                print(ex)
                                escritura_lenta('Ingrese una opcion valida')
                    else:
                        #no existe
                        escritura_lenta('El anunciante ingresado no existe')
                        escritura_lenta('Desea volver a escribir el codigo? (y/n)')
                        op = input('(y/n): ')
                        if (op == 'n'):
                            permanecer2 = False

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Eliminar anunciantes
'''
def EliminarAnuncios():
    permanecer = True
    while (permanecer):
        try:
            escritura_lenta('\n¿Que desea hacer primero?: ')
            escritura_lenta('1) Ver contenido')
            escritura_lenta('2) Eliminar utilizando codigo')
            escritura_lenta('3) Cancelar\n')
            op = int(input("Opcion: "))
            if (op == 1):
                #Ver anuncios
                permanecer2 = True
                offset = 0
                pag = 1
                while(permanecer2):
                    if(offset >= 0):
                        obtenerData('Anuncios', offset)
                        escritura_lenta('Pagina: '+str(pag))
                        escritura_lenta('Avanzar(a)/Retroceder(d)/salir(l): ')
                        siguiente = input('(a/d/l): ')
                        if (siguiente == 'a'):
                            offset += 10
                            pag += 1
                        elif (siguiente == 'd'):
                            offset -= 10
                            pag -= 1
                        elif (siguiente == 'l'):
                            permanecer2 = False
                        else:
                            escritura_lenta('La opcion ingresada no es valida')
                    else:
                        #Corregir el offset y evitar que este se convierta en 0
                        offset = 0
                        pag = 1

            elif (op == 2):
                #Eliminar con codigo
                Codigo_anuncio = input('Ingrese el codigo del anuncio: ')
                Delete_Anuncio(Codigo_anuncio)
                print("Anuncio eliminado exitosamente")

            elif (op == 3):
                #salir
                permanecer = False
        except:
            escritura_lenta('Ingrese una respuesta valida\n')

'''
Modificar Usuarios
'''
def Modifi_Usuarios():
    permanecer = True
    while (permanecer):
        escritura_lenta("Ingrese el correo de la cuenta que desea modificar\n")
        correo = input('Correo: ')
        if (Correo_Validacion(correo)):
            #El correo es valido
            escritura_lenta('La suscripcion actual de '+correo+ ' es ' + Get_Sub(correo))
            permanecer2 = True
            while (permanecer2):
                escritura_lenta('A que suscripcion desea cambiarlo? (1, 2, 3)\n')
                nuevaSus = input('Nueva suscripcion: ')
                if (nuevaSus == '1'):
                    #gratis
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Gratis', correo)
                    print("Cambio de suscripcion exitoso")
                    permanecer2 = False
                    permanecer = False
                elif (nuevaSus == '2'):
                    #estandar
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Estandar', correo)
                    print("Cambio de suscripcion exitoso")
                    cant = Get_Perfiles(correo)
                    if (cant == 4):
                        ActPerfil(correo)
                    permanecer2 = False
                    permanecer = False
                elif (nuevaSus == '3'):
                    #premium
                    '''
                    Query que cambia la suscripcion
                    '''
                    Mod_Usuarios('Avanzada', correo)
                    print("Cambio de suscripcion exitoso")
                    cant = Get_Perfiles(correo)
                    if (cant == 8):
                        ActPerfil(correo)
                    permanecer2 = False
                    permanecer = False
                else:
                    #Error
                    escritura_lenta('La opcion ingresada no es valida')
                    escritura_lenta('¿Desea continuar? ')
                    oppp = input('(y/n)')
                    if (oppp == 'n'):
                        permanecer2 = False
                        permanecer = False
                
        else:
            #el correo no es valido
            escritura_lenta('Desea ingresar el correo nuevamente? ')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

'''
Desactivar usuarios
'''
def desactivar_Usuarios():
    permanecer = True
    while (permanecer):
        escritura_lenta("Ingrese el correo de la cuenta que desea desactivar\n")
        correo = input('Correo: ')
        if (Correo_Validacion(correo)):
            #El correo es valido
            if Get_Estado(correo):
                escritura_lenta('El estado actual de '+correo+ ' es cuenta activada')
            else:
                escritura_lenta('El estado actual de '+correo+ ' es cuenta desactivada')
            permanecer2 = True
            while (permanecer2):
                escritura_lenta('Seguro que desea toggle con el estado de la cuenta? ')
                opp = input('(y/n): ')
                if (opp == 'y'):
                    nuevoEstado = not Get_Estado(correo)
                    '''
                    Query para acer UPDATE en el dato
                    '''
                    if Get_Estado(correo):
                        Desactivar_Usuarios(nuevoEstado, correo)
                        print("Desactivacion exitosa")
                    else:
                        Desactivar_Usuarios(nuevoEstado, correo)
                        print("Activacion exitosa")
                    permanecer2 = False
                    permanecer = False
                elif (opp == 'n'):
                    permanecer2 = False
                    permanecer = False
                else:
                    #Error
                    escritura_lenta('La opcion ingresada no es valida')
                
        else:
            #el correo no es valido
            escritura_lenta('Desea ingresar el correo nuevamente? (y/n)')
            op = input('(y/n): ')
            if (op == 'n'):
                permanecer = False

def reporte_1():
    escritura_lenta("Ingreso de los rangos de fecha")
    escritura_lenta("Fecha A\n")
    year_A =    SolicitudNum3("Ingresa el valor de Year: ")
    month_A =   SolicitudNum3("Ingresa el valor de Month: ")
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3("Ingresa el valor de Day: ")
    if day_A < 1 or day_A > 31:
        day_A = 1
    escritura_lenta("Fecha B\n")
    year_B =    SolicitudNum3("Ingresa el valor de Year: ")
    month_B =   SolicitudNum3("Ingresa el valor de Month: ")
    if month_B < 1 or month_B > 12:
        month_B = 1
    day_B =     SolicitudNum3("Ingresa el valor de  Day: ")
    if day_B < 1 or day_B > 31:
        day_B = 1

    fechaA= str(year_A)+"-"+str(month_A)+"-"+str(day_A)

    fechaB= str(year_B)+"-"+str(month_B)+"-"+str(day_B)
    query_reporte_1(fechaA, fechaB, fechaA, fechaB)

    return 2

def reporte_2():
    escritura_lenta("Ingreso de los rangos de fecha\n")
    escritura_lenta("Fecha A\n")
    year_A =    SolicitudNum3("Ingresa el valor de Year: ")
    month_A =   SolicitudNum3("Ingresa el valor de Month: ")
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3("Ingresa el valor de Day: ")
    if day_A < 1 or day_A > 31:
        day_A = 1
    escritura_lenta("Fecha B\n")
    year_B =    SolicitudNum3("Ingresa el valor de Year: ")
    month_B =   SolicitudNum3("Ingresa el valor de Month: ")
    if month_B < 1 or month_B > 12:
        month_B = 1
    day_B =     SolicitudNum3("Ingresa el valor de  Day: ")
    if day_B < 1 or day_B > 31:
        day_B = 1

    fechaA= str(year_A)+"-"+str(month_A)+"-"+str(day_A)
    fechaB= str(year_B)+"-"+str(month_B)+"-"+str(day_B)
    
    GetCantReprGratis(fechaA, fechaB)
    GetCantReprEst(fechaA, fechaB)
    GetCantReprAva(fechaA, fechaB)

def reporte_3():
    TopAct()
    print()
    TopDir()

def reporte_5():
    escritura_lenta("Ingreso de la fecha\n")

    year_A =    SolicitudNum3("Ingresa el valor de Year: ")
    month_A =   SolicitudNum3("Ingresa el valor de Month: ")
    if month_A < 1 or month_A > 12:
        month_A = 1
    day_A =     SolicitudNum3("Ingresa el valor de Day: ")
    if day_A < 1 or day_A > 31:
        day_A = 1

    fechaA= str(year_A)+"-"+str(month_A)+"-"+str(day_A)

    query_reporte_5(fechaA)

    return 2