from datetime import datetime
from random import random

class Avion :
    def __init__ (self,idAvion,reg_number,icao,tipoAvion,tAerolinea):
        self.idAvion= idAvion
        self.regNumber = reg_number
        self.icao = icao
        self.tipoAvion = tipoAvion
        self.tAerolinea = tAerolinea
        
class Aeropuerto:
    def __init__ (self, idAeropuerto, iata, icao):
        self.idAeropuerto = idAeropuerto 
        self.iata = iata
        self.icao = icao

class TAerolinea:
    def __init__ (self, idAerolinea, iata,icao):
        self.idAerolinea = idAerolinea
        self.iata = iata
        self.icao = icao

class TipoAvion:
    def __init__(self, idTipoAvion,regNumber,capacidad,largo,ancho): 
        self.idTipoAvion = idTipoAvion
        self.regNumber = regNumber
        self.capacidad=capacidad
        self.largo=largo
        self.ancho=ancho

class Vuelo:
    def __init__ (self, status, aeropuertoPartida, aeropuertoDestino, aerolinea, vuelo):
        self.aeropuertoOrigen = Aeropuerto (aeropuertoPartida.idAeropuerto, aeropuertoPartida.iataCode, aeropuertoPartida.icaoCode)
        if (status == "scheduled"):
            anho = aeropuertoDestino.scheduledTime[0:4]
            print(anho)  
            
    def __init__ (self,llegada,avion,horaEstimada,fechaEstimada, \
        horaProgramada,fechaProgramada, horaLlegada, fechaLlegada,  icao, iata, \
        numeroVuelo,estaEnTierra,latitud,longitud, \
        altura, direccion, velocidadHorizontal, velocidadVertical, aeropuertoOrigen):
        
        self.tiempoEstimado = horaEstimada
        self.tiempoProgramado = horaProgramada
        self.tiempoLlegada = horaLlegada
        self.icao = icao
        self.iata = iata
        self.numeroVuelo = numeroVuelo
        self.estaEnTierra = estaEnTierra
        self.latitud = latitud
        self.longitud = longitud
        self.altura = altura
        self.direccion = direccion
        self.velocidadHorizontal = velocidadHorizontal
        self.velocidadVertical = velocidadVertical 
        self.aeropuertoOrigen = aeropuertoOrigen #class
        self.asignado = False
        self.area= None
        self.avion = avion #class
             
        
    def asignarPuerta (self, flagArea, area): 
        self.flagArea = flagArea # 1: zona, 0: puerta
        self.Area = area # puntero a puerta o zona
        
class BloqueVuelo:
    def __init__(self):
        self.vuelo = None
        self.ocupado = None
        self.sig = None
        self.ant = None

    def addVuelo(self,vuelo):
        self.vuelo = vuelo
        self.ocupado = True

class ListaVuelos:
    def __init__ (self):
        self.inicio = None
        self.fin = None
        self.cantidad=0
    
    def insertarBloque (self, bloque, pos=0):
        if(self.inicio  is None):
            self.inicio = bloque
            self.fin = bloque
        else:
            self.inicio.sig.ant=bloque
            self.inicio.sig = bloque
            
        self.cantidad += 1

class Area:
    def __init__ (self, idArea,  largo,ancho, coordenadaXCentro, coordenadaYCentro):
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
    def __init__(self, puerta, longitud):
        self.puerta = puerta

#def main():
#    listaPuertas = []
#    for i  in range(10):
#        listaPuertas.append(Puerta(i,int(round((random()+1)*400)),(random()+1)*10,(random()+1)*10))
#    print (listaPuertas[2].capacidad)
    #print(str(p.ancho)+" / "+str(p.capacidad) +" / " + str(p.tiempoDisponible))

#if __name__ == "__main__":
#    main()
'''
class Salida:
    def _init_ (self, iataCod, icaoCod, terminal, puerta, horaProgramada, horaEstimada, horaReal, pistaEstimada, pistaReal):
        self.iataCod = iataCod
        self.icaoCod = icaoCod
        self.terminal = terminal
        self.puerta = puerta
        self.horaProgramada = horaProgramada
        self.horaEstimada = horaEstimada
        self.horaReal = horaReal
        self.pistaEstimada = pistaEstimada
        self.pistaReal = pistaReal

class Llegada:
    def _init_ (self, iataCod, icaoCod, horaProgramada, horaEstimada, horaReal, pistaEstimada, pistaReal):
        self.iataCod = iataCod
        self.icaoCod = icaoCod
        self.horaProgramada = horaProgramada
        self.horaEstimada = horaEstimada
        self.horaReal = horaReal
        self.pistaEstimada = pistaEstimada
        self.pistaReal = pistaReal

class Aerolinea:
    def _init_ (self, nombre, iataCod, icaoCod)
        self.nombre = nombre
        self.iataCod = iataCod
        self.icaoCod = icaoCod
'''