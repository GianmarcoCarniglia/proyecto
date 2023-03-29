from datetime import datetime
from constructor import Constructor
from piloto import Piloto
from carrera import Carrera, Circuito, Location, Restaurante, Producto
from cliente import Cliente
from compra import Compra
import matplotlib.pyplot as plt
import numpy as np
import random
from tabulate import tabulate
from collections import Counter
import os
import pickle



def funcion_menu():
    
    menu= int(input('A continuacion se presentara el menu de las opciones\ndisponibles:\nMarque el numero de la funcion que desea ejecutar\n1. Gestión de carreras y equipo \n2. Gestion de venta de entradas \n3. Gestion de asistencia a las carreras \n4. Gestion de restaurantes\n5. Gestion de venta de restaurantes\n6. Indicadores de gestion (estadisticas)\n7. Grafico \n8. Finalizar \n >'))
    if menu==1:
        print('Gestion de carreras y equipo')   
    elif menu==2:
        print('Gestion de venta de entradas')
    elif menu==3:
        print('Gestion de asistencia a las carreras')
    elif menu==4:
        print('Gestion de Restaurantes')
    elif menu==5:
        print('Gestion de venta de Restaurantes')
    elif menu==6:
        print('Indicadores de gestion (estadisticas)')
    elif menu==7:
        print('Ver grafica')
    elif menu==8:
        print('Gracias, ha finalizado')
    else:
        print('Numero invalido')
        funcion_menu()
    return menu

'''Esta funcion va a desplegar las opciones que tiene el cliente'''

def gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location):

    menu=int(input('Marque el numero de la funcion que desee realizar\n 1. Buscar los constructores por país\n 2. Buscar los pilotos por constructor \n 3. Buscar a las carreras por país del circuito \n 4. Buscar todas las carreras que ocurran en un mes \n 5. Finalizar una carrera \n >'))
    if menu==1:
        print('Buscar los constructores por país')
        lista_pais_constructor= []
        for x in lista_constructor:
            print (x.nacionalidad)
        pais= input('Que pais desea buscar, ingrese su nombre exacto:\n>')
        
        
        for x in lista_constructor:
            if x.nacionalidad == pais:
                lista_pais_constructor.append(x)
        if len(lista_pais_constructor)>0:
            print('Los constructores de este pais son:\n')
            for item, y in enumerate(lista_pais_constructor):
                print(item+1)
                y.mostrar_constructor()
        else:
            print('Pais no tiene partidos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)





    elif menu==2:
        print('Buscar los pilotos por constructor')
       
        for x in lista_constructor:
            print (x.nombre_equipo)
        constructor= input('Que pilotos desea buscar, ingrese el nombre del constructor tal y como sale:\n>')
        
        lista=[]
        for j in lista_constructor:
            if constructor == j.nombre_equipo:
                for x in lista_piloto:
                    if j.id_equipo==x.nombre_equipo:
                        lista.append(x)
        if len(lista)> 0:
            for x in lista:
                x.mostrar_piloto()
        else:
            print('Constructor no existente')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
                #revisar los demas ifs
           





    elif menu==3:
        print('Buscar a las carreras por país del circuito')
        
        for i in lista_location:
            print(i.pais)

        pais_circuito= input('Que pais desea buscar, ingrese el nombre del pais exacto:\n')
        print('Las carreras que se van a correr en este pais son:\n')
        lista_2=[]
        for x in lista_location:
            if x.pais == pais_circuito:
                lista_2.append(x)
        if len(lista_2)> 0:
            for x in lista_2:
                x.mostrar_location()
        else:
            print('Pais no tiene circuitos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)


    elif menu==4:
        print('Buscar todas las carreras que ocurran en un mes')
        fecha=input('Ingrese el mes que desea buscar, en el formato 00\n Ejemplo: para escribir enero escribo "01"\n>')
        lista_3=[]
        separacion=[]
        # for i in lista_carrera:
        #     separacion.append(i.fecha_carrera)
        # for i in separacion:
        #     i.split('-')
        #     # ['ano', 'mes','dia']4
        #     if i[1]==fecha:
        #         lista_3.append(x)
        for i in lista_carrera:
            datetime_object = datetime.strptime(i.fecha_carrera, '%Y-%m-%d')
            if datetime_object.month == int(fecha):
                lista_3.append(i)
        if len(lista_3)> 0:
            for i in lista_3:
                i.mostrar_carrera()
        else:
            print('Mes no tiene circuitos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
   
   
    elif menu==5:
        get_podio(lista_piloto, lista_carrera, lista_constructor)
    
    
    else:
        print('Numero invalido')
        gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
    return




def get_podio(pilotos, carreras, constructores):
    puntaje = {1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}
    print('\nCarreras sin finalizar:')
    n_invalidos = []
    for i,carrera in enumerate(carreras):
        if carrera.podio == False:
            print('\t',i+1,carrera.nombre_carrera)
        else:
            n_invalidos.append(i+1)
    if len(n_invalidos) != len(carreras):
        choice = input('\nIngrese el numero correspondiente a la carrera a finalizar:\n>> ')
        while not choice.isnumeric() or int(choice) not in range (1,len(carreras)+1) or int(choice) in n_invalidos:
            choice = input('\nERROR - Opcion invalida\nPor favor ingrese el numero correspondiente a la carrera a finalizar:\n>> ')
        podio = random.sample(pilotos, 10)       
        contador = 1
        for piloto in podio:
            piloto.puntaje += puntaje[contador]
            contador += 1
        for constructor in constructores:
            for pilot in constructor.pilotos:
                if pilot in podio:
                    constructor.puntaje += pilot.puntaje
        carreras[int(choice)-1].podio = podio
        print(f"\nPodio final para la carrera {carreras[int(choice)-1].nombre_carrera}")
        l=[]
        for i, piloto in enumerate(podio):
            pi = piloto.nombre_piloto +' '+ piloto.apellido_piloto
            sc= puntaje[i+1]
            d= [i+1 ,pi, sc]
            l.append(d)
        print(tabulate(l,headers=['Posicion','Piloto','Puntaje']))
        return pilotos, constructores, carreras
    else:
        print('\nYa se han finalizado todas las carreras!')        
        return pilotos, constructores, carreras

'''Funcion para obtener el podio de una carrera'''





def gestion_2(lista_carrera):
    
    '''cliente = []
    entradas_general = []
    entradas_vip = []'''
    nombre = input('Cual es su nombre:\n')
    apellido = input('Cual es su apellido:\n')
    edad = input('Cual es su edad:\n')
    while not edad.isnumeric():
        edad = input('Cual es su edad:\n')
    ci = input('Cual es su cedula:\n')
    while not ci.isnumeric():
        ci = input('Cual es su cedula:\n')
    for i in lista_carrera:
        Carrera.mostrar_carrera(i)
    carrera_ronda = input('Ingrese la ronda de la carrera que quiere ver:\n')
    
    for i in lista_carrera:
        if  carrera_ronda == i.ronda:
            entrada = int(input('Que tipo de entrada desea 0. General= 150$ 1. VIP=340$ y tendras acceso al restaurante\n'))
            id_entrada = ci
            print(' a continuacion se le mostrara el mapa, las D son asientos disponibles y las O son asientos ocupados')

            if entrada == 0:

                asiento = mostrar_asientos (i.mapa['general'][0], i.mapa['general'][1])
                
            else:

                asiento = mostrar_asientos (i.mapa['vip'][0], i.mapa['vip'][1])
                



            
    if entrada==0:
        entrada='General'
        costo=150
        descuento=costo
        if es_ondulado(ci):
            descuento=costo*0.5
            print(f'Tuvo un descuento del 50%, el precio de su entrada ahora es {descuento}')

    elif entrada==1:
        entrada='VIP'
        costo=340
        descuento=costo
        if es_ondulado(ci):
            descuento=costo*0.5
            print(f'Tuvo un descuento del 50%, el precio de su entrada ahora es {descuento}')

    else:

        print('numero invalido')
        gestion_2(lista_carrera)

    confirmacion=int(input('Desea confirmar su compra:\n1. Si\n2. No\n'))
    
    if confirmacion==1:

        



        print(f'{nombre} {apellido}')
        print (f'{entrada} {id_entrada}')
        print(f'Asiento:{asiento}')
        iva=descuento*0.16
        total=descuento*1.16

        print(f'Subtotal: {costo}')
        print(f'Despues del descuento: {descuento}')
        print(f'iva= {iva}')
        print(f'Total: {total}')
        print(f'Gracias por su compra')
        usuario=Cliente(nombre, apellido, edad, ci, entrada, id_entrada, costo, False, total, carrera_ronda)
        '''cliente.append(usuario)
        if usuario.entrada=='General':
            entradas_general.append(usuario)
        elif usuario.entrada=='VIP':
            entradas_vip.append(usuario)'''

        for carrera in lista_carrera:

            if usuario.ronda == carrera.ronda:

                carrera.boletos_vendidos = carrera.boletos_vendidos + 1

    elif confirmacion==2:
        funcion_menu()

    else:
        print('numero invalido')
        gestion_2(lista_carrera)




    return usuario







def mostrar_asientos(filas, columnas):	
    asientos = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("D")
        asientos.append(fila)

    for i in range(filas):
        for j in range(columnas):
            print(asientos[i][j], end=" ")
        print()
    fila = int(input("Seleccione una fila: "))
    columna = int(input("Seleccione una columna: "))
    asiento=[fila, columna]
    if asientos[fila-1][columna-1] == "O":
        print("Este asiento ya está ocupado. Por favor cancele la compra.")
    else:
        asientos[fila-1][columna-1] = "O"
        print("Asiento reservado exitosamente.")
    print("Gracias por usar nuestro sistema de reservas.")
    return asiento



'''con esta funcion mostramos los asientos disponibles y ocupados para cada estadio, le pasamos como atributo
la cantidad de filas (la primera posicion de la lista del api) y la cantidad de columnas (la segunda posicion 
de la lista del api) '''

# '''def ondulados(ci):
#         ondulado = True
#         contador = 0
#         par = list(str(ci))[0]
#         inpar = list(str(ci))[1]
#         if par == inpar:
#             print (f'The number {ci} is not an ondulated number.')
#         else:
#             for x in str(ci):
#                 if (contador+2)%2 == 0:
#                     if x != par:
#                         ondulado = False
#                     contador +=1
#                 elif (contador+2) %2 !=0:
#                     if x != inpar:
#                         ondulado = False
#                     contador += 1
#             if ondulado == True:
#                 return 0
#             else:
#                 return 1'''
            
def es_ondulado(cadena):
    last=""
    for i in cadena:
        if i==last:
            return False
        last=i
    return True
	
'''funcion para determinar un numero ondulado'''



def gestion_3(cliente, lista_carrera):
    ci=input('Ingrese su cedula: ')
    for usuario in cliente:
        if ci==usuario.id_entrada:
            if usuario.acceso==False:
                usuario.acceso=True
                print('El ticket es valido')
                for carrera in lista_carrera:

                    if usuario.ronda == carrera.ronda:

                        carrera.asistencia += 1

            else:
                print ('Ya alguien uso esta entrada')
        else:
            print ('El ticket se ingreso incorrectamente')
            gestion_3(cliente)
    return

'''a cada cliente le convertimos su numero de cedula en numero de ticket y lo guardamos como atributo de ese cliente
para que cada ticket sea un numero unico. en esta funcion le solicitamos su cedula y verificamos que se haya vendido un ticket
con ese numero y luego verificamos que no haya sido usado'''

def gestion_4(listaproducto):
    menu=input('Marque el numero de la funcion que desee realizar\n 1. Buscar productos por nombre\n 2. Buscar productos por tipo \n 3. Buscar productos por rango de precio \n')
    resultado = 0
    if menu=='1':
        print('Buscar productos por nombre')
        nombre=input('Ingrese el nombre del producto: ')
        for x in listaproducto:
            if getattr(x,'nombre') == nombre:
                print('Se encontro el siguiente producto')
                nombreproducto = getattr(x,'nombre')
                precio = getattr(x,'precio')
                tipo = getattr(x,'tipo')
                print(f'\n\n Nombre: {nombreproducto} \n Precio: {precio}\n Tipo: {tipo}')
                resultado = 1
                break
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    if menu=='2':
        print('Buscar productos por tipo: Las opciones son "alimento" o "bebida"')
        tipo=input('Ingrese el tipo del producto: ')
        for x in listaproducto:
            tipo_arr = getattr(x,'tipo') 
            tipo_primero = tipo_arr.split(":")[0]
            tipo_segundo = tipo_arr.split(":")[1]
            if tipo_primero == 'drink':
                t = 'bebida'
            else:
                t = 'alimento'
            if t == tipo:
                nombreproducto = getattr(x,'nombre')
                precio = getattr(x,'precio')
                print(f'\n\n Nombre: {nombreproducto} \n Precio: {precio}\n Subcategoria: {tipo_segundo}')
                resultado = 1
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    if menu=='3':
        print('Buscar productos por rango de precio')
        rangoinferior=input('Ingrese rango inferior: ')
        if rangoinferior.isnumeric() == False:
            print('Rango inferior is not numeric. Try again')
            return
        rangosuperior=input('Ingrese rango superior: ')
        if rangosuperior.isnumeric()== False:
            print('Rango superior is not numeric. Try again')
            return
        for x in listaproducto:
            precio = float(getattr(x,'precio'))
            if (precio >= float(rangoinferior)) & (precio <= float(rangosuperior)):
                nombreproducto = getattr(x,'nombre')
                tipo = getattr(x,'tipo')
                print(f'\n\n Nombre: {nombreproducto} \n Precio: {precio}')
                resultado = 1
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    return

'''en esta funcion le mostraremos al usuarios los productos disponibles por nombre, por tipo o por rango de precio. 
agregamos todos los productos a una lista con una funcion definida en la clase estadio. le solicitamos al usuario 
lo que desea buscar y con un for buscamos en todos los objetos de la lista el atributo a buscar y mostramos todos
los productos que sean = a lo que solicito el cliente '''

def NumeroPerfecto(ci):
	suma = 0
	for i in range(1,int(ci)):
		if (int(ci) % (i) == 0):
			suma += (i)
	if int(ci) == suma:
		return True
	else:
		return False

'''funcion para determinar un numero perfecto'''





def gestion_5(clientes):
    cedulaexiste = False
    total = 0
    subtotal = 0
    esdescuento = False
    descuento = 0
    comidasistema = False
    if not clientes:
        print("No hay clientes registrados \n\n")
        return
    cedula=input('Ingrese su cedula\n')
    for i in clientes:
        if i.ci==cedula:
            cedulaexiste = True
            if i.entrada=='General':
                print ('No puede comprar porque su entrada es general')
            elif i.entrada=='VIP':
                print('Bienvenidos al restaurante')
                perfecto=NumeroPerfecto(i.ci)

                if perfecto == True:
                    print ('Obtendras un 15% de descuento')
                    esdescuento = True
                if int(i.edad)<18:
                    print ('Este cliente no puede consumir bebidas alcoholicas pq es menor de edad')
                print("Lista de productos")
                lista_de_productos_vendidos_interna = []
                while True:
                    for x in lista_producto:
                            precio = float(getattr(x,'precio'))
                            nombreproducto = getattr(x,'nombre')
                            tipo = getattr(x,'tipo')
                            if (int(i.edad)<18) & (tipo.split(":")[1] == "alcoholic"):
                                pass
                            else:
                                print(f'Nombre: {nombreproducto}, Precio: {precio}, Tipo: {tipo}')
                    comidaseleccionada=input('Que comida/bebida deseas comprar:\n')
                    cant=input('Cantidad:\n')
                    for x in lista_producto:
                            if getattr(x,'nombre') == comidaseleccionada:
                                comidasistema = True
                                precio = float(getattr(x,'precio'))
                                nombreproducto = getattr(x,'nombre')
                                lista_de_productos_vendidos_interna.append(x)
                                break
                    if comidasistema == False: 
                        print("La comida escrita no se encuentra en el sistema")
                    continuar=input('Desea culminar la compra o continuar comprando? Seleccione 0 para Salir y 1 para continuar:\n')
                    subtotal = precio*int(cant) + subtotal
                    
                    if int(continuar) == 0:
                        if esdescuento == True:
                            descuento = subtotal*0.15
                        total = subtotal - descuento
                        print('Subtotal:' + str(subtotal))
                        print('Descuento:' + str(descuento))
                        print('Total:' + str(total))
                        continuar=input('Estas de acuerdo con la compra. Presione 1 si estas de acuerdo, 0 si no:\n')
                        if continuar == '1':
                            i.monto= i.monto + total
                            return lista_de_productos_vendidos_interna
                        else:
                            print('Compra cancelada')
                            return

    if cedulaexiste == False: 
        print ('La cedula no existe')
    return 

'''Para comprar productos de restaurantes verificamos que sea cliente vip y le mostramos todos los productos disponibles  con un for 
y el metodo getattr donde obtenemos el value del key solicitado de cada atributo, el usuario elige su producto. buscamos su precio en
el sistema si tiene algun descuento se lo decimos y descontamos y le mostramos la factura '''


def gestion_6(entradas_vip, clientes, lista_carrera, lista_circuito, lista_de_productos_vendidos):
    menu=int(input('Marque el numero de la funcion que desee realizar\n 1. Promedio de gastos de un cliente VIP en una carrera \n 2. Mostrar tabla con la asistencia a las carreras de mejor a peor \n 3. ¿Cuál fue la carrera con mayor asistencia? \n 4. ¿Cuál fue la carrera con mayor boletos vendidos? \n 5. Top 3 productos más vendidos en el restaurante \n 6. Top 3 de clientes \n 7. Grafica \n >'))
    if menu== 1:
        if len(entradas_vip)== 0:
            print('No hay entradas vip vendidas')
        else:
            print("Promedio de gastos de un cliente VIP en una carrera")
            suma=0
            for i in entradas_vip:
                suma += i.monto
            promedio = suma/len(entradas_vip)
            print(f'{promedio}')
    elif menu == 2:
        tabla_asistencia(lista_circuito)
    elif menu == 3:
        mayor_asistencia(lista_carrera)
    elif menu == 4:
        mayor_boletos_vendidos(lista_carrera)
    elif menu == 5:
        top_productos(lista_de_productos_vendidos)
    elif menu == 6:
        top_clientes(clientes)
    elif menu == 7:
        grafica()
    else:
        print('Numero invalido')
        gestion_6()

def grafica():
    print('Bebidas vs Comidas')
    '''base de datos'''
    data = {'Bebidas':20, 'Comidas':15}
    c = list(data.keys())
    valor = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    '''creating the bar plot'''
    plt.bar(c, valor, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Bebidas")
    plt.ylabel("Comidas")
    plt.title("Cantidad de comidas/Bebidas que ofrece el restaurante")
    plt.show()

def tabla_asistencia(lista_circuito):
    aux = sorted(lista_circuito, key=lambda x:x.asistencia, reverse=True)
    l = []
    for i, circuito in enumerate(aux):
        try:
            relacion = circuito.asistencia / circuito.boletos_vendidos
        except:
            relacion = 0
        d=[i+1,circuito.nombre_carrera,circuito.nombre_circuito,circuito.asistencia, circuito.boletos_vendidos, relacion]
        l.append(d)
    print(tabulate(l ,headers=['Posicion','Nombre','Estadio','Asistencia','Boletos','Relacion asistencia/boletos']))



def mayor_asistencia(lista_carrera):
    aux = sorted(lista_carrera, key=lambda x:x.asistencia, reverse=True)
    contador = 0
    for i in lista_carrera:
        if i.asistencia==0:
            contador +=1
    if contador == len(lista_carrera):
        print('Nadie ha asistido a ningun evento')
    else:
        print('La carrera con mayor asistencia fue: ')
        aux[0].mostrar_carrera

def mayor_boletos_vendidos(lista_carrera):

    aux = sorted(lista_carrera, key=lambda x:x.boletos_vendidos, reverse=True)
    contador = 0
    '''for i in lista_carrera:
        if i.boletos_vendidos==0:
            contador +=1
    if contador == len(lista_carrera):
        print('Nadie ha comprado en ningun evento')
    else:'''
    print('La carrera con mayor boletos vendidos fue: ')
    aux[0].mostrar_carrera

def top_productos(lista_de_productos_vendidos):
    if len(lista_de_productos_vendidos)==0:
        print('Nadie ha comprado a ningun producto')
    elif len(lista_de_productos_vendidos)==1:
        lista_de_productos_vendidos[0].mostrar_producto
    elif len(lista_de_productos_vendidos)==2:
        lista_de_productos_vendidos[0].mostrar_producto
        lista_de_productos_vendidos[1].mostrar_producto
    elif len(lista_de_productos_vendidos)==3:
        lista_de_productos_vendidos[0].mostrar_producto
        lista_de_productos_vendidos[1].mostrar_producto
        lista_de_productos_vendidos[2].mostrar_producto
    else:
        counter = Counter(lista_de_productos_vendidos)
        first, second, third, *_, last = counter.most_common()
        first.mostrar_producto
        second.mostrar_producto
        third.mostrar_producto

def top_clientes(clientes):
    
    aux = sorted(clientes, key=lambda x:x.monto, reverse=True)
    if len(aux) == 0:
        print('Aun no se han vendido boletos')
    elif len(aux) == 1:
        print('Top 3 clientes que mas gastaron: ')
        aux[0].mostrar_cliente
    elif len(aux) == 2:
        print('Top 3 clientes que mas gastaron: ')
        aux[0].mostrar_cliente
        aux[1].mostrar_cliente
    elif len(aux) == 2:
        print('Top 3 clientes que mas gastaron: ')
        aux[0].mostrar_cliente
        aux[1].mostrar_cliente
        aux[2].mostrar_cliente




# '''lista_constructor=Constructor.leer_constructor()
# lista_piloto=Piloto.leer_piloto()
# lista_circuito=Circuito.leer_circuito()
# lista_carrera=Carrera.leer_carrera()
# lista_location=Location.leer_location()
# lista_producto = Producto.leer_producto()'''



if os.stat('carreras.txt').st_size == 0:
        

        lista_constructor=Constructor.leer_constructor()
        lista_piloto=Piloto.leer_piloto()
        lista_circuito=Circuito.leer_circuito()
        lista_carrera=Carrera.leer_carrera()
        lista_location=Location.leer_location()
        lista_producto = Producto.leer_producto()
        clientes=[]
        lista_de_productos_vendidos = []
        entradas_general = []
        entradas_vip = []


else:

    with open('carreras.txt', 'rb') as c:
        lista_carrera  = pickle.load(c)
    with open('pilotos.txt', 'rb') as c:
        lista_piloto  = pickle.load(c)
    with open('constructores.txt', 'rb') as c:
        lista_constructor  = pickle.load(c)
    with open('location.txt', 'rb') as c:
        lista_location  = pickle.load(c)
    with open('productos.txt', 'rb') as c:
        lista_producto  = pickle.load(c)
    with open('clientes.txt', 'rb') as c:
        clientes  = pickle.load(c)
    with open('circuitos.txt', 'rb') as c:
        lista_circuito  = pickle.load(c)
    with open('productosvendidos.txt', 'rb') as c:
        lista_de_productos_vendidos  = pickle.load(c)
    with open('entradasgeneral.txt', 'rb') as c:
        entradas_general  = pickle.load(c)
    with open('entradasvip.txt', 'rb') as c:
        entradas_vip  = pickle.load(c)
    













def main():
    print('')
    print('/***************************/')
    print('/* Bienvenidos a Formula 1 */')
    print('/***************************/')
    print('')

    '''clientes=[]
    lista_de_productos_vendidos = []
    entradas_general = []
    entradas_vip = []'''



    while True:
        menu=funcion_menu()

        if menu==1:
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
            
        elif menu==2:

            clientes.append(gestion_2(lista_carrera))
            for usuario in clientes:
                if usuario.entrada=='General':
                    entradas_general.append(usuario)
                elif usuario.entrada=='VIP':
                    entradas_vip.append(usuario)

        elif menu==3:
            if len(clientes) == 0:
                print("Debe introducir primero al menos un cliente en la opcion 2 para tener acceso a esta opcion.")
            else:
                gestion_3(clientes, lista_carrera)
            
        elif menu==4:
            gestion_4(lista_producto)
            
        elif menu==5:
            lista_de_productos_vendidos_interna = gestion_5(clientes)
            for i in lista_de_productos_vendidos_interna:
                lista_de_productos_vendidos.append(i)
            
            
        elif menu==6:
            gestion_6(entradas_vip, clientes, lista_carrera, lista_circuito, lista_de_productos_vendidos)

        elif menu==7:
            grafica()

        elif menu==8:



            with open('carreras.txt', 'wb') as c:  
                pickle.dump(lista_carrera, c) 
            with open('constructores.txt', 'wb') as c:  
                pickle.dump(lista_constructor, c) 
            with open('pilotos.txt', 'wb') as c:  
                pickle.dump(lista_piloto, c) 
            with open('clientes.txt', 'wb') as c:  
                pickle.dump(clientes, c)
            with open('location.txt', 'wb') as c:  
                pickle.dump(lista_location, c) 
            with open('productos.txt', 'wb') as c:  
                pickle.dump(lista_producto, c) 
            with open('circuitos.txt', 'wb') as c:  
                pickle.dump(lista_circuito, c)
            with open('productosvendidos.txt', 'wb') as c:  
                pickle.dump(lista_de_productos_vendidos, c) 
            with open('entradasgeneral.txt', 'wb') as c:  
                pickle.dump(entradas_general, c) 
            with open('entradasvip.txt', 'wb') as c:  
                pickle.dump(entradas_vip, c)




            print(' _________________________')
            print('/\                        \\')
            print('\_|    Gracias y          |')
            print('  |      hasta luego      |')
            print('  |  _____________________|_')
            print('  \_/______________________/')
            break

main()

