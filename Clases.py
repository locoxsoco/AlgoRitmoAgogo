from datetime import datetime, date,time, timedelta
class Avion :
    def __init__ (self,reg_number=None,icao=None,tipoAvion=None,tAerolinea=None):
        pass
    
    def addRegNumber (self,reg_number):
        self.regNumber = reg_number

    def addIata(self, iata):
        self.iata = iata

    def addIcao(self, icao):
        self.icao = icao

    def addTipoAvion(self, tipoAvion):
        self.tipoAvion = tipoAvion

    def addTAerolinea(self, tAerolinea):
        self.tAerolinea = tAerolinea

class Aeropuerto:
    def __init__ (self, iata=None, icao=None):
        pass

    def addIata(self, iata):
        self.iata = iata

    def addIcao(self, icao):
        self.icao = icao

class TAerolinea:
    def __init__ (self,idAerolinea=None, iata=None,icao=None):
        pass

    def addIdAerolinea(self, idAerolinea):
        self.idAerolinea = idAerolinea

    def addIata(self, iata):
        self.iata = iata

    def addIcao(self, icao):
        self.icao = icao

    def addNombre(self,nombre):
        self.nombre = nombre

class TipoAvion:
    def __init__(self,regNumber = None,capacidad = None,largo = None,ancho = None): 
        pass

    def addRegNumber (self,reg_number):
        self.regNumber = reg_number

    def addCapacidad(self,capacidad):
        self.capacidad = capacidad

    def addLargo(self,largo):
        self.largo = largo

    def addAncho(self,ancho):
        self.ancho=ancho

class Vuelo:        
    def __init__ (self, estado = None, avion =None,tiempoEstimado =None,tiempoProgramado=None, \
        tiempoLlegada=None,  icao=None, iata=None, \
        numeroVuelo=None,estaEnTierra=None,latitud=None,longitud=None, \
        altura=None, direccion=None, velocidadHorizontal=None, velocidadVertical=None,
        aeropuertoOrigen = None):
        self.asignado = False
        self.area=None
        self.estado=estado
        self.avion=avion
        self.tiempoEstimado=tiempoEstimado
        self.tiempoProgramado=tiempoProgramado
        self.tiempoLlegada=tiempoLlegada
        self.iata=iata
        self.icao=icao
        self.numeroVuelo=numeroVuelo
        self.estaEnTierra=estaEnTierra
        self.latitud=latitud
        self.longitud=longitud
        self.altura=altura
        self.direccion = direccion
        self.velocidadHorizontal = velocidadHorizontal
        self.velocidadVertical = velocidadVertical
        self.aeropuertoOrigen = aeropuertoOrigen

    def addEstado(self,estado):
        self.estado = estado

    def addAvion (self,avion):
        self.avion=avion

    def addTiempoEstimado (self,tiempoEstimado):
        self.tiempoEstimado = tiempoEstimado

    def addTiempoProgramado (self,tiempoProgramado):
        self.tiempoProgramado=tiempoProgramado

    def addTiempoLlegada (self, tiempoLlegada):
        self.tiempoLlegada = tiempoLlegada

    def addIata(self, iata):
        self.iata = iata

    def addIcao(self, icao):
        self.icao = icao

    def addNumeroVuelo(self,numeroVuelo):
        self.numeroVuelo=numeroVuelo

    def addEstaEnTierra(self,estaEnTierra):
        self.estaEnTierra = estaEnTierra

    def addLatitud(self,latitud):
        self.latitud =latitud

    def addLongitud(self,longitud):
        self.longitud=longitud

    def addAltura(self,altura):
        self.altura=altura

    def addDireccion(self,direccion):
        self.direccion=direccion
        
    def addVelocidadHorizontal(self,velocidadHorizontal):
        self.velocidadHorizontal = velocidadHorizontal

    def addVelocidadVertical(self,velocidadVertical):
        self.velocidadVertical = velocidadVertical 

    def addAeropuertoOrigen(self,aeropuertoOrigen):
        self.aeropuertoOrigen = aeropuertoOrigen 

    def addAvion(self,avion):
        self.avion = avion #class

    def asignarPuerta (self, flagArea, area): 
        self.flagArea = flagArea # 1: zona, 0: puerta
        self.area = area # puntero a puerta o zona
        self.asignado=True

    def printData(self):
        print("Numero de vuelo: " + str(self.numeroVuelo))
        if (self.area is not None):
            print("Puerta: " + str(self.area.idArea))
        print ("------------------------")

class BloqueVuelo:
    def __init__(self):
        self.vuelo = None
        self.ocupado=None
        self.tiempoInicio = None
        self.tiempoFin = None
        self.sig = None

    def addVuelo(self,vuelo):
        self.vuelo = vuelo
        self.ocupado = True
        if(vuelo.estado =="scheduled"):
            t = vuelo.tiempoProgramado
        else:
            t=vuelo.tiempoEstimado

        self.tiempoInicio = t-timedelta(hours =1)
        self.tiempoFin = t + timedelta(hours=2)


    def definirEspacioVacio(self, tiempoInicio, tiempoFin):
        self.tiempoInicio = tiempoInicio
        self.tiempoFin=tiempoFin
        self.ocupado=False

class ListaVuelos:
    def __init__ (self):
        self.inicio = BloqueVuelo()

        dia = datetime.now()
        self.tiempoInicio= datetime(year=dia.year,month =dia.month,day=dia.day,\
            hour=dia.hour,minute=0,second=0)-timedelta(days=1)
        self.tiempoFin= datetime(year=dia.year,month =dia.month,day=dia.day,\
            hour=dia.hour,minute=59,second=59)+timedelta(days=2)

        self.inicio.definirEspacioVacio(self.tiempoInicio,self.tiempoFin)
        self.fin = self.inicio
        self.cantidad=0
        self.cantBloques=1
        self.tiempoLibre = self.tiempoFin - self.tiempoInicio
    
    def insertarBloque (self, bloque,pos=0):
        p = self.inicio
        ant = None
        ubicado = False
        while(p is not None):
            if (not p.ocupado and p.tiempoInicio<= bloque.tiempoInicio and \
                p.tiempoFin >= bloque.tiempoFin):

                self.tiempoLibre = self.tiempoLibre - (bloque.tiempoFin - bloque.tiempoInicio)
                bloqueAnt = ant    
                bloqueSig = p.sig
                if (p.tiempoInicio != bloque.tiempoInicio):
                    bloqueAnt = BloqueVuelo()
                    bloqueAnt.definirEspacioVacio(p.tiempoInicio,bloque.tiempoInicio)
                    if(ant is None):
                        self.inicio = bloqueAnt
                    else:
                        ant.sig = bloqueAnt 
                    self.cantBloques += 1
                if (p.tiempoFin != bloque.tiempoFin):
                    bloqueSig = BloqueVuelo()
                    bloqueSig.definirEspacioVacio(bloque.tiempoFin,p.tiempoFin)
                    bloqueSig.sig = p.sig
                    self.cantBloques +=1

                if(bloqueAnt is None):
                    self.inicio = bloque
                else:
                    bloqueAnt.sig = bloque
                bloque.sig = bloqueSig
                self.cantidad +=1

                #print("vuelo "+str(bloque.vuelo.numeroVuelo) )
                #print (self.cantidad,self.cantBloques)
                #print(bloqueSig.tiempoInicio, bloqueSig.tiempoFin)
                #print(bloqueAnt.tiempoInicio, bloqueAnt.tiempoFin)
                ubicado = True
                break
            ant = p
            p = p.sig
        if (ubicado): 
            return self.tiempoLibre
        else: 
            return -1

class Area:
    def __init__ (self, idArea=0, largo=0.0, ancho=0.0, coordenadaXCentro=0.0, \
        coordenadaYCentro=0.0):
        self.idArea = idArea
        self.largo = largo
        self.ancho = ancho
        self.vuelos = ListaVuelos()
        self.tiempoLibre = self.vuelos.tiempoLibre


    def imprimirLista(self):
        p=self.vuelos.inicio
        print("ID: "+str(self.idArea))
        while(p is not None):
            print("Libre: "+ str(p.ocupado)+" | tiempoInicio: "+str(p.tiempoInicio)+ " | tiempoFin: "+str(p.tiempoFin))
            p=p.sig
        print("----------------------")
        
class Zona(Area):
    def __init__ (self, idArea=0, largo=0.0, ancho=0.0, coordenadaXCentro=0.0, \
        coordenadaYCentro=0):
        Area.__init__(self, idArea, largo,ancho,coordenadaXCentro, coordenadaYCentro)

    def insertarVuelo(self, vuelo):
        bloque = BloqueVuelo()
        bloque.addVuelo(vuelo)
        insercion = self.vuelos.insertarBloque(bloque)
        if (insercion != -1 ):
            bloque.vuelo.asignarPuerta (1, self)
            self.tiempoLibre = insercion
            return 1
        else:
            #print ("Area: " + str(self.idArea) + "t: " + str(insercion))
            return -1

class Puerta(Area):
    def __init__ (self, idArea=0, largo=0.0, ancho=0.0, coordenadaXCentro=0.0, \
        coordenadaYCentro=0.0, velocidadDesembarco = 0.0):
        Area.__init__(self, idArea, largo,ancho, coordenadaXCentro, coordenadaYCentro)
        self.velocidadDesembarco = velocidadDesembarco

    def insertarVuelo(self, vuelo):
        bloque = BloqueVuelo()
        bloque.addVuelo(vuelo)
        insercion = self.vuelos.insertarBloque(bloque)
        if (insercion != -1 ):
            bloque.vuelo.asignarPuerta (0, self)
            self.tiempoLibre = insercion
            return 1
        else:
            #print ("Area: " + str(self.idArea) + "t: " + str(insercion))
            return -1

class Manga: 
    def __init__(self):
        pass

    def asignarPuerta(self, puerta):
        self.puerta=puerta