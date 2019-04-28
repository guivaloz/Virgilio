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
        self.salida = salida
        # El time stamp de inicio
        if isinstance(inicio, datetime):
            self.inicio = inicio
        elif isinstance(inicio, str):
            idt = datetime.strptime(inicio, "%Y-%m-%d")
            self.inicio = datetime(idt.year, idt.month, idt.day, 0, 0, 0)
        else:
            self.inicio = None
        # El time stamp de termino
        if isinstance(termino, datetime):
            self.termino = termino
        elif isinstance(termino, str):
            tdt = datetime.strptime(termino, "%Y-%m-%d")
            self.termino = datetime(tdt.year, tdt.month, tdt.day, 23, 59, 59)
        else:
            self.termino = None
        # Propios
        self.incidencias = None
        self.cantidad = 0
        self.total = 0
        self.consultado = False

    def encabezados(self):
        return(Incidencia.campos())

    def cargar(self):
        if self.consultado:
            return()
        if not os.path.isfile(self.entrada):
            raise Exception("<Error> Archivo CSV {} no encontrado.".format(self.entrada))
        self.incidencias = list()
        with open(self.entrada, encoding='utf8') as archivo:
            lector = csv.DictReader(archivo, delimiter=';')
            for renglon in lector:
                ano = int(renglon['Año'])
                # Saltar
                if self.inicio != None and ano < self.inicio.year:
                    continue
                if self.termino != None and ano > self.termino.year:
                    continue
                if self.entidad != None and renglon['Entidad'] != self.entidad:
                    continue
                if self.municipio != None:
                    if isinstance(self.municipio, str) and renglon['Municipio'] != self.municipio:
                        continue
                    if isinstance(self.municipio, list) and renglon['Municipio'] not in self.municipio:
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
                        if self.inicio != None and ano == self.inicio.year:
                            if mes_numero < self.inicio.month:
                                continue
                        if self.termino != None and ano == self.termino.year:
                            if mes_numero > self.termino.month:
                                continue
                        incidencia = Incidencia(
                            ano=int(renglon['Año']),
                            mes=mes_numero,
                            entidad=renglon['Entidad'],
                            municipio=renglon['Municipio'],
                            modalidad=renglon['Modalidad'],
                            tipo=renglon['Tipo de delito'],
                            subtipo=renglon['Subtipo de delito'],
                            cantidad=int(renglon[mes]),
                            )
                        self.incidencias.append(incidencia)
                        self.cantidad += 1
                        self.total += incidencia.cantidad
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
        table = [self.encabezados()]
        for incidencia in self.incidencias:
            table.append(incidencia.renglon_list())
        return("\n".join([
            tabulate(table, headers="firstrow"),
            "<Incidencias: {}>".format(self.total),
            ]))

