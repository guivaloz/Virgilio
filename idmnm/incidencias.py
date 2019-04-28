import calendar
import csv
import datetime
import os


meses_a_numeros = {
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


class Incidencia(object):
    """ Incidencia """

    def __init__(self, ano, mes, entidad, municipio, modalidad, tipo, subtipo, cantidad):
        # La fecha es el ultimo dia del mes
        ano = int(ano)
        mes = int(mes)
        self.fecha = datetime.date(ano, mes, calendar.monthrange(ano, mes)[-1]).isoformat()
        # Propios
        self.entidad = entidad
        self.municipio = municipio
        self.modalidad = modalidad
        self.tipo = tipo
        self.subtipo = subtipo
        self.cantidad = cantidad

    @staticmethod
    def fieldnames():
        return([
            'fecha',
            'entidad',
            'municipio',
            'modalidad',
            'tipo',
            'subtipo',
            'cantidad',
            ])

    def row_dict(self):
        return({
            'fecha': self.fecha,
            'entidad': self.entidad,
            'municipio': self.municipio,
            'modalidad': self.modalidad,
            'tipo': self.tipo,
            'subtipo': self.subtipo,
            'cantidad': self.cantidad,
            })

    def row_list(self):
        return([
            self.fecha,
            self.entidad,
            self.municipio,
            self.modalidad,
            self.tipo,
            self.subtipo,
            self.cantidad,
            ])

    def __repr__(self):
        return('<Incidencia {0}>'.format(self.cantidad))


class Incidencias(object):
    """ Incidencias """

    def __init__(self, entidad, municipio, modalidad, tipo, subtipo, inicio, termino):
        # Parametros
        self.entidad = entidad
        self.municipio = municipio
        self.modalidad = modalidad
        self.tipo = tipo
        self.subtipo = subtipo
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
        # Propios
        self.incidencias = None
        self.cantidad = 0
        self.consultado = False

    def encabezados(self):
        return(Incidencia.fieldnames())

    def cargar(self):
        if self.consultado:
            return()
        if not os.path.isfile(self.entrada):
            raise Exception("<Error> Archivo CSV {} no encontrado.".format(self.entrada))
        self.incidencias = list()
        with open(self.entrada) as archivo:
            lector = csv.DictReader(archivo)
            for renglon in lector:
                # Saltar
                #if self.ano != None and renglon['Año'] != self.ano:
                #    continue
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
                for mes, mes_numero in meses_a_numeros.items():
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
            escritor = csv.DictWriter(archivo, fieldnames=self.headers())
            escritor.writeheader()
            for incidencia in self.incidencias:
                escritor.writerow(incidencia.row_dict())

    def __repr__(self):
        return('<Incidencias>')

"""
        table = [incidencias.headers()]
        for incidencia in incidencias.load():
            table.append(incidencia.row_list())
        click.echo(tabulate(table, headers="firstrow"))
        click.echo('There are {0} incidencias.'.format(incidencias.count))
"""
