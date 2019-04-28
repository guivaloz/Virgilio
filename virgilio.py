import click
from tabulate import tabulate

import idenm.incidencias as idenm
import idmnm.incidencias as idmnm


class Config(object):

    def __init__(self):
        self.salvar = False
        self.entrada = ''
        self.inicio = ''
        self.termino = ''
        self.salida = ''


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--salvar', is_flag=True, help='Habilita el modo de salvar')
@click.option('--entrada', default='direcciones-ip.csv', type=str, help='Archivo CSV con insumos')
@click.option('--inicio', default=None, type=str, help='Fecha de incio YYYY-MM-DD')
@click.option('--termino', default=None, type=str, help='Fecha de término YYYY-MM-DD')
@click.option('--salida', default='', type=str, help='Nombre del archivo a escribir')
@pass_config
def cli(config, salvar, entrada, inicio, termino, salida):
    if salvar:
        config.salvar = True
        click.echo('<Aviso> En modo de salvar.')
    else:
        click.echo('<Aviso> En modo de probar.')
    config.entrada = entrada
    config.inicio = inicio
    config.termino = termino
    config.salida = salida


@cli.command()
@pass_config
def idenm(config):
    """
    Incidencia Delictiva Estatal, Nueva Metodología
    """
    incidencias = idenm.Incidencias()
    try:
        if config.salvar:
            click.echo(incidencias.guardar())
        else:
            click.echo(incidencias)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def idmnm(config):
    """
    Incidencia Delictiva Municipal, Nueva Metodología
    """
    incidencias = idmnm.Incidencias()
    try:
        if config.salvar:
            click.echo(incidencias.guardar())
        else:
            click.echo(incidencias)
    except Exception as e:
        click.echo(e)

