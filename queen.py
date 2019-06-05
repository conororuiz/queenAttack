Frango=''
tabla=[]
Rfila=Rcolumna=mov=fil=col=0

def crearTablero(n):
    global tabla
    filas = n
    tabla = [0] * filas
    for i in range(filas):
        tabla[i] = [0] * n

def fueraDeRango(fila,columna):
    global tabla
    global Frango
    if fila>=len(tabla ) or columna>=len(tabla):
        Frango="fuera"
    elif fila<0 or columna<0:
        Frango="fuera"
    else:
        Frango="ok"

def posicionReina(fila,columna):
    global tabla
    global Frango
    global  Rfila
    global  Rcolumna
    fueraDeRango(fila-1,columna -1)
    if Frango=="fuera":
        print("la reina no puede ir fuera del tablero...")
    elif Frango=="ok":
        tabla[fila -1][columna -1]=2
        Rfila=fila-1
        Rcolumna=columna-1

def ocupado(fila,columna):
    global tabla
    if tabla[fila][columna]==0:
        return False
    else:
        return True

def posicionObtaculo(fila,columna):
    global tabla
    global Frango
    fueraDeRango(fila - 1, columna - 1)
    if ocupado(fila-1,columna-1):
        print("un obtaculo no puede ir donde ya hay una ficha")
    else:
        if Frango == "fuera":
            print("un obstaculo no puede ir fuera del tablero...")
        elif Frango == "ok":
            tabla[fila - 1][columna - 1] = 1

def movimientos(fila,columna):
    global Frango
    global tabla
    global mov
    movis=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    #movimientos
    for i in range(0,len(movis)):
        Tfila = fila
        Tcol = columna
        seguir=True
        while seguir==True:
            cont = 0
            Tfila+=movis[i][cont]
            cont+=1
            Tcol+=movis[i][cont]
            fueraDeRango(Tfila, Tcol)
            if Frango == "fuera":
                seguir = False
            else:
                if ocupado(Tfila, Tcol):
                    seguir = False
                else:
                    mov+=1
    print("movimientos que puede hacer la reina:")
    print(mov)

def resolver():
    #se lee el archivo
    try:
     datos=open('tt.txt','r')
    except:
       print("error al intentar abrir el archivo...")
       exit()
    #se pasan los datos a un vector y se oreganizan
    dato=datos.readlines()
    for i in range(0,len(dato)):
     dato[i]=dato[i].split()
    #se opera segun los datos optenidos
    try:
        size=int(dato[0][0])
        numobs = int(dato[0][1])
        Preinafila=int(dato[1][0])
        Preinacol=int(dato[1][1])

    except:
        print("el documento no tiene el formato correcto")
        exit()
    tot=0
    crearTablero(size)
    posicionReina(Preinafila,Preinacol)
    #se verifica que haya obstaculos y se colocan
    if numobs>=1 or numobs==0:
      for i in range(2, len(dato)):
          tot+=1
      if numobs==tot:
            try :
                for i in range(2,len(dato)):
                     cont=0
                     fil=int(dato[i][cont])
                     cont+=1
                     col=int(dato[i][cont])
                     posicionObtaculo(fil,col)
            except:
              print("el documento no tene el formato correcto")
              exit()
            # se verifica cuantos movimientos puede hacer la reina
            movimientos(Rfila, Rcolumna)
      else:
          print("hay menos/mas obstaculos de los estipulados en el documento")
          exit()
resolver()
tabla.reverse()
for i in tabla:
    print(i)