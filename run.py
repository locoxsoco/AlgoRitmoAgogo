from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import multiprocessing as mp
import math
import random
import sys
import requests
import time
import json
import numpy
import importlib
import Clases
import Metaheuristico
from datetime import datetime, date, time, timedelta

def main():
    print(sys.argv[1]+ " cargado")
    with open(sys.argv[1]) as json_file:  
        data = json.loads(json_file.read().replace("\'", "\""))
        #print (data)
        #print(len(data))
        #for j in data:
            #print(j['arrival'])

    data_filtered = list(filter(lambda x : x['status'] != 'landed' and x['status'] != 'cancelled', data))
    #print(len(data_filtered))
    #print(data_filtered[47])
    listaVuelos = []
    Clases.Vuelo.nVuelo =0
    i =0
    for flight in data_filtered:
        #print (flight['status'], flight['departure'], flight['arrival'], flight['airline'], flight['flight'])
        #try:
        i +=1
        vuelo = Clases.Vuelo()
        jsonDestino = flight ['arrival']
        anho = int(jsonDestino['scheduledTime'][0:4])
        mes = int(jsonDestino['scheduledTime'][5:7])
        dia = int(jsonDestino['scheduledTime'][8:10])
        hora = int(jsonDestino['scheduledTime'][11:13])
        minuto = int(jsonDestino['scheduledTime'][14:16])
        segundo = int(jsonDestino['scheduledTime'][17:19])
        vuelo.setTiempoEstimado(datetime(year=anho, month=mes, day=dia, \
                                   hour=hora, minute=minuto, second=segundo))
        vuelo.setTiempoLlegada(datetime(year=anho, month=mes, day=dia, \
                                   hour=hora, minute=minuto, second=segundo))
        vuelo.setEstado(flight['status'])
        if (vuelo.estado=="active"):
            try:
                anho = int(jsonDestino['scheduledTime'][0:4])
                mes = int(jsonDestino['scheduledTime'][5:7])
                dia = int(jsonDestino['scheduledTime'][8:10])
                hora = int(jsonDestino['scheduledTime'][11:13])
                minuto = int(jsonDestino['scheduledTime'][14:16])
                segundo = int(jsonDestino['scheduledTime'][17:19])
                vuelo.setTiempoEstimado(datetime(year=anho, month=mes, day=dia, \
                                           hour=hora, minute=minuto, second=segundo))
                vuelo.setTiempoLlegada(datetime(year=anho, month=mes, day=dia, \
                                           hour=hora, minute=minuto, second=segundo))
            except:
                pass
            
        jsonVuelo = flight['flight']
        vuelo.addNumeroVuelo(jsonVuelo['number'])
        vuelo.addIata(jsonVuelo['iataNumber'])

        try:
            vuelo.addIcao(jsonVuelo['icaoNumber'])
        except:
            pass

        jsonAerolinea = flight['airline']
        aerolinea =Clases.TAerolinea()
        aerolinea.addIata(jsonAerolinea['iataCode'])
        try:
            aerolinea.addIcao(jsonAerolinea['icaoCode'])
        except:
            pass
        aerolinea.addNombre(jsonAerolinea['name'])

        avion = Clases.Avion()
        avion.addTAerolinea(aerolinea)
        vuelo.setAvion(avion)

        vuelo.asignarIDVuelo()
        listaVuelos.append(vuelo)
        #print (str(vuelo.tiempoEstimado)+ "  "+ str(vuelo.idVuelo))

    nPuertas = 20
    nZonas = 52
    listaZonas = []
    listaPuertas = []
    for i in range(1,nPuertas+1):
        area2 = Clases.Puerta(2*i,random.random()*79+1, random.random()*59+1,random.random()*499+1,random.random()*499+1,10)
        listaPuertas.append(area2)
        
    for i in range(1,nZonas +1):
        area = Clases.Zona(2*i-1,random.random()*79+1, random.random()*59+1,random.random()*499+1, random.random()*499+1)
        listaZonas.append(area)

    ann = Metaheuristico.Annealer(listaVuelos,listaPuertas,listaZonas)
    x,y = ann.anneal()

    print("Puertas")
    for i in x[0]:
        i.imprimirLista()
    print("Zonas:")
    for i in x[1]:
        i.imprimirLista()
    print("Resultado: " + str(y))

if __name__ == '__main__':
    main()