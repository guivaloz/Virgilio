import csv
import os
from datetime import datetime
from tabulate import tabulate

from idmnm.incidencia import Incidencia


class Incidencias(object):
    """ Incidencias """

    MESES_A_NUMEROS = {
        'Enero': 1,
        'Febrero': 2,
        'Marzo': 3,
        'Abril': 4,
        'Mayo': 5,
        'Junio': 6,
        'Julio': 7,
        'Agosto': 8,
        'Septiembre': 9,
        'Octubre': 10,
        'Noviembre': 11,
        'Diciembre': 12,
        }

    def __init__(self, entidad=None, municipio=None, modalidad=None, tipo=None, subtipo=None, entrada=None, inicio=None, termino=None, salida=None):
        # Parametros
        self.entidad = entidad
        self.municipio = municipio
        self.modalidad = modalidad
        self.tipo = tipo
        self.subtipo = subtipo
        self.entrada = entrada
        # El time stamp de inicio comienza en tiempo 00:00:00
        if inicio != None:
            idt = datetime.strptime(inicio, "%Y-%m-%d")
            self.inicio = datetime(idt.year, idt.month, idt.day, 0, 0, 0)
        else:
            self.inicio = None
        # El time stamp de termino es en tiempo 23:59:59
        if termino != None:
            tdt = datetime.strptime(termino, "%Y-%m-%d")
            self.termino = datetime(tdt.year, tdt.month, tdt.day, 23, 59, 59)
        else:
            self.termino = None
        self.salida = salida
        # Propios
        self.incidencias = None
        self.cantidad = 0
        self.consultado = False

    def encabezados(self):
        return(Incidencia.campos())

    def cargar(self):
        if self.consultado:
            return()
        if not os.path.isfile(self.entrada):
            raise Exception("<Error> Archivo CSV {} no encontrado.".format(self.entrada))
        self.incidencias = list()
        with open(self.entrada, encoding='iso8859') as archivo:
            lector = csv.DictReader(archivo, delimiter=';')
            for renglon in lector:
                # Saltar
                # self.inicio
                # self.termino
                #if self.ano != None and renglon['Año'] != self.ano:
                #    continue
                if self.inicio != None and int(renglon['Año']) < self.inicio.year:
                    continue
                if self.termino != None and int(renglon['Año']) > self.termino.year:
                    continue
                if self.entidad != None and renglon['Entidad'] != self.entidad:
                    continue
                if self.municipio != None and renglon['Municipio'] != self.municipio:
                    continue
                if self.modalidad != None and renglon['Modalidad'] != self.modalidad:
                    continue
                if self.tipo != None and renglon['Tipo de delito'] != self.tipo:
                    continue
                if self.subtipo != None and renglon['Subtipo de delito'] != self.subtipo:
                    continue
                # Acumular
                for mes, mes_numero in self.MESES_A_NUMEROS.items():
                    if renglon[mes] != '':
                        incidencia = Incidencia(
                            ano=renglon['Año'],
                            mes=mes_numero,
                            entidad=renglon['Entidad'],
                            municipio=renglon['Municipio'],
                            modalidad=renglon['Modalidad'],
                            tipo=renglon['Tipo de delito'],
                            subtipo=renglon['Subtipo de delito'],
                            cantidad=renglon[mes],
                            )
                        self.incidencias.append(incidencia)
                        self.cantidad += 1
        self.consultado = True

    def guardar(self):
        if self.consultado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<Error> No hay registros. No se puede guardar.')
        with open(csv_file, 'w', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=self.encabezados())
            escritor.writeheader()
            for incidencia in self.incidencias:
                escritor.writerow(incidencia.renglon_dict())

    def __repr__(self):
        if self.consultado == False:
            self.cargar()
        if self.cantidad == 0:
            return('<Incidencias> La consulta no arrojó registros.')
        #return('<Incidencias {}>.'.format(self.cantidad))
        table = [self.encabezados()]
        for incidencia in self.incidencias:
            table.append(incidencia.renglon_list())
        return(tabulate(table, headers="firstrow"))

