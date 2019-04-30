from datetime import datetime
from random import random

class Avion :
    def __init__ (self,idAvion,reg_number,icao,tipoAvion,tAerolinea):
        self.idAvion= idAvion
        self.regNumber = reg_number
        self.icao = icao
        self.tipoAvion = tipoAvion
        self.tAerolinea = tAerolinea

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
    def __init__ (self,llegada,avion,horaEstimada,fechaEstimada, \
        horaProgramada,fechaProgramada, horaLlegada, fechaLlegada,  icao, iata, \
        numeroVuelo,estaEnTierra,latitud,longitud, \
        altura, direccion, velocidadHorizontal, velocidadVertical):
        self.horaEstimada = horaEstimada
        self.fechaEstimada = fechaEstimada
        self.horaProgramada = horaProgramada
        self.fechaProgramada = fechaProgramada
        self.horaLlegada = horaLlegada
        self.fechaLlegada = fechaLlegada
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
        self.asignado = False
        self.area= None
        self.avion = avion

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
