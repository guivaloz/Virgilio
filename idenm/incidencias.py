import calendar
import csv
import datetime
import os


class Incidencia(object):
    """ Incidencia """

    def __init__(self):
        pass

    @staticmethod
    def fieldnames():
        pass

    def row_dict(self):
        pass

    def row_list(self):
        pass

    def __repr__(self):
        return('<Incidencia>')


class Incidencias(object):
    """ Incidencias """

    def __init__(self):
        pass

    def encabezados(self):
        return(Incidencia.fieldnames())

    def cargar(self):
        pass

    def guardar(self):
        pass

    def __repr__(self):
        return('<Incidencias>')
