import csv
import os
from datetime import datetime
from tabulate import tabulate

from idmnm.incidencia import Incidencia


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

