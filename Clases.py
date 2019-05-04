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
        altura=None, direccion=None, velocidadHorizontal=None, velocidadVertical=None):
        self.asignado = False
        self.area=None

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
        self.latitud

    def addLongitud(self,longitud):
        self.longitud

    def addAltura(self,altura):
        self.altura

    def addDireccion(self,direccion):
        self.direccion
        
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
        self.Area = area # puntero a puerta o zona
        self.asignado=True

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

    def definirEspacioVacio(self, tiempoInicio, tiempoFin):
        self.tiempoInicio = tiempoInicio
        self.tiempoFin=tiempoFin
        self.ocupado=False

class ListaVuelos:
    def __init__ (self):
        self.inicio = None
        self.fin = None
        self.cantidad=0
        self.cantBloques=0
    
    def insertarBloqueVuelo (self, bloque,pos=0):
        if(self.inicio  is None):
            self.inicio = bloque
            self.fin = BloqueVuelo()
            if (bloque.vuelo.estado == "scheduled"):
                self.fin.definirEspacioVacio(bloque.vuelo.tiempoProgramado, datetime())
            self.inicio.sig = self.fin
            self.cantBloques += 2
        else:
            p = self.inicio
            while(p is not None):
                if (not p.ocupado and bloque.vuelo.estado):
                    pass
                    #insert

                p = p.sig
                pass
            self.inicio.sig = bloque
            self.cantBloques += 1

            
        self.cantidad += 1

class Area:
    def __init__ (self, idArea=None, largo=None, ancho=None, coordenadaXCentro=None, \
        coordenadaYCentro=None):
        self.idPuerta = idArea
        self.largo = largo
        self.ancho = ancho
        self.tiempoDisponible = 24*60*60
        self.vuelos = ListaVuelos()
        
class Zona(Area):
    def __init__ (self, idArea, largo,ancho,coordenadaXCentro, coordenadaYCentro):
        Area.__init__(self, idArea, largo,ancho,coordenadaXCentro, coordenadaYCentro)

class Puerta(Area):
    def __init__ (self, idArea, largo,ancho,coordenadaXCentro, coordenadaYCentro, velocidadDesembarco):
        Area.__init__(self, idArea, largo,ancho, coordenadaXCentro, coordenadaYCentro)
        self.velocidadDesembarco = velocidadDesembarco

class Manga: 
    def __init__(self):
        pass

    def asignarPuerta(self, puerta):
        self.puerta=puerta