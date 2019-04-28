import calendar
import datetime


class Incidencia(object):
    """ Incidencia """

    def __init__(self, ano=None, mes=None, entidad=None, municipio=None, modalidad=None, tipo=None, subtipo=None, cantidad=None):
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
    def campos():
        return([
            'fecha',
            'entidad',
            'municipio',
            'modalidad',
            'tipo',
            'subtipo',
            'cantidad',
            ])

    def renglon_dict(self):
        return({
            'fecha': self.fecha,
            'entidad': self.entidad,
            'municipio': self.municipio,
            'modalidad': self.modalidad,
            'tipo': self.tipo,
            'subtipo': self.subtipo,
            'cantidad': self.cantidad,
            })

    def renglon_list(self):
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

