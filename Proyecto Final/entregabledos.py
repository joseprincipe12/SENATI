from tkinter import *
from datetime import datetime
venta= []

inventario=[
    {"codigo": "111", "marca": "ADIDAS", "modelo": "CHOMPA", "precio": 90.0, "cantidad": 20},
    {"codigo": "112", "marca": "NIKE", "modelo": "POLO", "precio": 40.0, "cantidad": 20},
    {"codigo": "113", "marca": "PUMA", "modelo": "POLERA", "precio": 85.0, "cantidad": 20},
    {"codigo": "114", "marca": "XIOMI", "modelo": "CAMISA", "precio": 70.0, "cantidad": 20},
    {"codigo": "115", "marca": "NEW YORK", "modelo": "BERMUDA", "precio": 60.0, "cantidad": 20},
    {"codigo": "116", "marca": "HAWK", "modelo": "JEAN", "precio": 95.0, "cantidad": 20},
    {"codigo": "117", "marca": "MAUI", "modelo": "JOGGER", "precio": 79.0, "cantidad": 20},
    {"codigo": "118", "marca": "PUMA", "modelo": "CASACA", "precio": 99.0, "cantidad": 20},
    {"codigo": "119", "marca": "ZARA", "modelo": "BUZO", "precio": 70.0, "cantidad": 20},
    {"codigo": "120", "marca": "REEBOOK", "modelo": "LEGGING", "precio": 70.0, "cantidad": 20},
    {"codigo": "121", "marca": "HAWK", "modelo": "CAPA", "precio": 100.0, "cantidad": 20},
    {"codigo": "122", "marca": "ADIDAS", "modelo": "TOP", "precio": 40.0, "cantidad": 20},
    {"codigo": "123", "marca": "XIOMI", "modelo": "PIJAMA", "precio": 89.0, "cantidad": 20},
    {"codigo": "124", "marca": "HAWK", "modelo": "CHALECO", "precio": 55.0, "cantidad": 20},
    {"codigo": "125", "marca": "ADIDAS", "modelo": "CALCETINES", "precio": 30.0, "cantidad": 20},
    {"codigo": "126", "marca": "NIKE", "modelo": "FALDA", "precio": 45.0, "cantidad": 20},
    {"codigo": "127", "marca": "TOPITOP", "modelo": "CALZONCILLO", "precio": 20.0, "cantidad": 20},
    {"codigo": "128", "marca": "CALVINK", "modelo": "BOXER", "precio": 30.0, "cantidad": 20},
    {"codigo": "129", "marca": "ADIDAS", "modelo": "CALZON", "precio": 30.0, "cantidad": 20},
    {"codigo": "130", "marca": "ADIDAS", "modelo": "VESTIDO", "precio": 89.0, "cantidad": 20},
    {"codigo": "131", "marca": "ADIDAS", "modelo": "CHOMPA", "precio": 89.0, "cantidad": 20},
    {"codigo": "132", "marca": "ADIDAS", "modelo": "PANTALON", "precio": 62.0, "cantidad": 20},
    {"codigo": "133", "marca": "ADIDAS", "modelo": "SHORT", "precio": 46.0, "cantidad": 20},
    {"codigo": "134", "marca": "ADIDAS", "modelo": "LICRA", "precio": 99.0, "cantidad": 20},
    {"codigo": "135", "marca": "ADIDAS", "modelo": "POLO", "precio": 47.0, "cantidad": 20},
]

def crear_boleta_electronica():
    root = Tk()
    root.title("Boleta Electrónica")
    #Parte 1 boleta
    #Importamos la Fecha y hora para imprimirla
    fecha_actual = datetime.now().strftime("%d/%m/%Y %I:%M %p")
    texto_uno = f"""
                    TOPITOP
      Av. Alfredo Mendiola 1400 Int. 106 A
                (CC. Megaplaza)
               Independencia Lima
                RUC:20100047056
        DOM. FISCAL: JR. HUALLAGA NRO.278 
                   LIMA-LIMA
------------------------------------------------
          BOLETA DE VENTA ELECTRONICA                        
------------------------------------------------
FECHA: {fecha_actual}
"""
    boleta_text_uno = Text(root, height=12.5, width=48,font=("Courier", 8))
    boleta_text_uno.insert(END, texto_uno)
    boleta_text_uno.pack()
#Parte 2 de la boleta
    texto_dos = """   
  Producto              Precio  Cant.  Subtotal
------------------------------------------------"""
    boleta_text_dos = Text(root, height=3, width=48,font=("Courier", 8))
    boleta_text_dos.insert(END, texto_dos)
    boleta_text_dos.pack()
    #Parte 3 de la boleta
    tamaño = len(venta)+(len(venta)*0.3)
    producto_texto_tres = Text(root, height=tamaño, width=48,font=("Courier", 8))
    producto_texto_tres.pack()
    total = 0
    # Agregar detalles de productos a producto_textouno
    for producto in venta:
        
        marca_producto = producto["marca"]
        modelo_producto = producto["modelo"]
        precio_producto = producto["precio"]
        cantidad_llevada = producto["cantllevada"]
        topro = cantidad_llevada * precio_producto
        total += topro
        detalle_producto = f"{modelo_producto:<7} {marca_producto:<10} {precio_producto:>10.2f} {cantidad_llevada:>5} {topro:>10.2f}\n"
        producto_texto_tres.insert(END, detalle_producto)

    #Parte 4 de la boleta
    text_cuatro = f"""
-----------------------------------------------
    Total:                     {"S/":<2}  {(total / 1.18):.2f}
    IGV (18%):                 {"S/":<2}   {(total / 1.18) * 0.18:.2f}
    Total a Pagar:             {"S/":<2}  {total:.2f}
-----------------------------------------------"""

    # Cuadro de texto para el modelo de boleta
    boleta_text_cuatro = Text(root, height=7, width=48,font=("Courier", 8))
    boleta_text_cuatro.insert(END, text_cuatro)
    boleta_text_cuatro.pack()
    #parte 5 boleta qr de topitop
    imagen = PhotoImage(file="qrtopitop.png")  # Reemplaza con la ruta correcta
    imagen = imagen.subsample(4,4)
    imagen_label = Label(root, image=imagen)
    imagen_label.pack()
    #parte 6 boleta
    texto_cinco = """
-----------------------------------------------
          GRACIAS POR SU PREFERENCIA 
          
            Como agradecimiento, 
    ¡has ganado un cupón de descuento del 
         10% para tu próxima compra!
    """
    boleta_text_cinco = Text(root, height=9, width=48,font=("Courier", 8))
    boleta_text_cinco.insert(END, texto_cinco)
    boleta_text_cinco.pack()
    
    # DISABLED
    boleta_text_uno.config(state=DISABLED)
    boleta_text_dos.config(state=DISABLED)
    producto_texto_tres.config(state=DISABLED)
    boleta_text_cuatro.config(state=DISABLED)
    boleta_text_cinco.config(state=DISABLED)
    
    
    
    root.mainloop()

def boleta():
    
    print("+----------------------------------------------+")
    print("|              **** TOPITOP ****               |")
    print("|                 ** BOLETA **                 |")
    print("+----------------------------------------------+")
    producto_encontrado = None
    topro=0 #TOTAL DEL PRODUCTO
    total=0 #TOTAL
    igv=0.18
    for producto in venta:
        producto_encontrado = producto

        if producto_encontrado:
            marca_producto = producto_encontrado["marca"]
            modelo_producto = producto_encontrado["modelo"]
            precio_producto = producto_encontrado["precio"]
            cantidad_llevada = producto_encontrado["cantllevada"]
            topro=cantidad_llevada*precio_producto
            total= total+topro
         
            print(f"| {marca_producto}      {modelo_producto}                         {cantidad_llevada} |")
            print(f"| Precio        X                            {cantidad_llevada} |")  
            print(f"| Precio U:                               {precio_producto} |")
           
           
    print(f"| TOTAL:                                  {total-(total*igv)} |")
    print(f"| IGV:                                    {total*igv} |")  
    print(f"| TOTALIGV                                {total} |")
    print("|       **** GRACIAS POR SU COMPRA ****        |")
    print("+----------------------------------------------+")
    crear_boleta_electronica()
def productosventa(codigo,marca,modelo,precio,cantidad,cantllevada):
    proventa = {
        "codigo": codigo,
        "marca":  marca,
        "modelo": modelo,
        "precio": precio,
        "cantidad": cantidad,
        "cantllevada": cantllevada
    }
    venta.append(proventa)
   
def nuevopoducto():
    # Solicitar al usuario que ingrese los detalles del nuevo producto
    codigo_nuevo = input("Ingrese el codigo del nuevo producto: ")
    marca_nuevo = input("Ingrese la marca del nuevo producto: ")
    modelo_nuevo = input("ingrese el modelo del producto: ")
    precio_nuevo = float(input("Ingrese el precio del nuevo producto: "))
    cantidad_nueva = int(input("Ingrese la cantidad del nuevo producto: "))

    # Crear un diccionario con la informaciÃ³n del nuevo producto
    nuevo_producto = {
        "codigo": codigo_nuevo,
        "marca":  marca_nuevo,
        "modelo": modelo_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    }

    # Agregar el nuevo producto a la lista de inventario
    inventario.append(nuevo_producto)

    # Mostrar mensaje de confirmaciÃ³n
    print("Nuevo producto agregado al inventario:")
   

def buscar():  
   
    cantprod= int(input("Cuantos productos ingresara: "))
    c = 0
    while c < cantprod:
        c = c + 1
        codigo_buscar = input("Ingrese el codigo del producto: ")
        cantllevada = int(input("Ingrese la cantidad del producto a llevar: "))

        producto_encontrado = None

        for producto in inventario:
            if producto["codigo"] == codigo_buscar:
                producto_encontrado = producto
                break

        if producto_encontrado:
            marca_producto = producto_encontrado["marca"]
            modelo_producto = producto_encontrado["modelo"]
            precio_producto = producto_encontrado["precio"]
            cantidad_producto = producto_encontrado["cantidad"]
           
            productosventa(codigo_buscar,marca_producto,modelo_producto,precio_producto,cantidad_producto,cantllevada)
       
        else:
            print("+-----------------------------------------+")
            print("| El codigo que ingreso es incorreto      |")
            print("|A|   Desea volver al menu principal      |")
            print("|B|   Desea ingresar los productos nuevame|")
            print("+-----------------------------------------+")
            print()
            opciond=["A","B"]
           
            op=input("Ingrese su opcion : ").upper()
            for e in opciond:
                if e == op:
                    break
                else:
                    continue
           
            if op=="A":
                bienvenido()
            elif op=="B":
                buscar()
       
        if c == cantprod:
            boleta()

def bienvenido():
    print("+----------------------------------------------+")
    print("| BIENVENIDOS AL SISTEMA DE VENTAS DE TOPITOP  |")
    print("|      👔 👕 👖 🩳 🧦 👟 👠 👢 👜 👗 👚 🥼     |")
    print("+----------------------------------------------+")
    print("|A|   Desea agregar un producto nuevo          |")
    print("|B|   Realizar una venta                       |")
    print("|C|   Cerrar el sistema                        |")
    print("+----------------------------------------------+")
    print()
   
    opcion=["A","B","C"]
   
    op=input("Ingrese su opcion : ").upper()
    for e in opcion:
        if e == op:
            break
        else:
            continue
   
    if op=="A":
       nuevopoducto()
       bienvenido()
    elif op=="B":
        buscar()
    elif op=="C":
        exit

bienvenido()


