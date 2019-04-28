from datetime import datetime
from tabulate import tabulate

from idmnm.incidencia import Incidencia
from idmnm.incidencias import Incidencias


class Reportes(object):
    """ Reportes """

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
        self.total_ultimo = 0
        self.total_ano_pasado = 0
        self.total_ano_antepasado = 0

    def cantidad_de_meses(self):
        return((self.termino.year - self.inicio.year) * 12 + self.termino.month - self.inicio.month + 1)

    def rango_de_fechas_ano_pasado(self):
        inicio = datetime(self.inicio.year - 1, self.inicio.month, self.inicio.day, 0, 0, 0)
        termino = datetime(self.termino.year - 1, self.termino.month, self.termino.day, 23, 59, 59)
        return(inicio, termino)

    def rango_de_fechas_ano_antepasado(self):
        inicio = datetime(self.inicio.year - 2, self.inicio.month, self.inicio.day, 0, 0, 0)
        termino = datetime(self.termino.year - 2, self.termino.month, self.termino.day, 23, 59, 59)
        return(inicio, termino)

    def crear_ultimo(self):
        incidencias = Incidencias(
            entidad=self.entidad,
            municipio=self.municipio,
            modalidad=self.modalidad,
            tipo=self.tipo,
            subtipo=self.subtipo,
            entrada=self.entrada,
            inicio=self.inicio,
            termino=self.termino,
            )
        incidencias.cargar()
        self.total_ultimo += incidencias.total
        return(incidencias)

    def crear_ano_pasado(self):
        inicio, termino = self.rango_de_fechas_ano_pasado()
        incidencias = Incidencias(
            entidad=self.entidad,
            municipio=self.municipio,
            modalidad=self.modalidad,
            tipo=self.tipo,
            subtipo=self.subtipo,
            entrada=self.entrada,
            inicio=inicio,
            termino=termino,
            )
        incidencias.cargar()
        self.total_ano_pasado += incidencias.total
        return(incidencias)

    def crear_ano_antepasado(self):
        inicio, termino = self.rango_de_fechas_ano_antepasado()
        incidencias = Incidencias(
            entidad=self.entidad,
            municipio=self.municipio,
            modalidad=self.modalidad,
            tipo=self.tipo,
            subtipo=self.subtipo,
            entrada=self.entrada,
            inicio=inicio,
            termino=termino,
            )
        incidencias.cargar()
        self.total_ano_antepasado += incidencias.total
        return(incidencias)

    def __repr__(self):
        if self.cantidad_de_meses() > 6:
            raise Exception('<Aviso> No deben elaborarse reportes mayores a 6 meses.')
        ano_pasado_inicio, ano_pasado_termino = self.rango_de_fechas_ano_pasado()
        ano_antepasado_inicio, ano_antepasado_termino = self.rango_de_fechas_ano_antepasado()
        return("\n".join([
            '<Reportes>',
            "- Meses de diferencia: {}".format(self.cantidad_de_meses()),
            "- De {} a {} son {}".format(self.inicio.isoformat(), self.termino.isoformat(), self.total_ultimo),
            "- De {} a {} son {}".format(ano_pasado_inicio.isoformat(), ano_pasado_termino.isoformat(), self.total_ano_pasado),
            "- De {} a {} son {}".format(ano_antepasado_inicio.isoformat(), ano_antepasado_termino.isoformat(), self.total_ano_antepasado),
            ]))
