import click

from idenm.incidencias import Incidencias as IncidenciasEstatales
from idmnm.incidencias import Incidencias as IncidenciasMunicipales
from idmnm.reportes import Reportes as ReportesMunicipales


class Config(object):

    def __init__(self):
        self.salvar = False
        self.entrada = ''
        self.inicio = None
        self.termino = None
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
    incidencias = idenm()
    try:
        if config.salvar:
            click.echo(incidencias.guardar())
        else:
            click.echo(incidencias)
    except Exception as e:
        click.echo(e)


@cli.command()
@click.option('--entidad', default=None, type=str, help='Entidad.')
@click.option('--municipio', default=None, type=str, help='Municipio.')
@click.option('--modalidad', default=None, type=str, help='Modalidad.')
@click.option('--tipo', default=None, type=str, help='Tipo.')
@click.option('--subtipo', default=None, type=str, help='Subtipo.')
@pass_config
def idmnm(config, entidad, municipio, modalidad, tipo, subtipo):
    """
    Incidencia Delictiva Municipal, Nueva Metodología
    """
    incidencias = IncidenciasMunicipales(
        entidad=entidad,
        municipio=municipio,
        modalidad=modalidad,
        tipo=tipo,
        subtipo=subtipo,
        entrada=config.entrada,
        inicio=config.inicio,
        termino=config.termino,
        salida=config.salida,
        )
    try:
        if config.salvar:
            click.echo(incidencias.guardar())
        else:
            click.echo(incidencias)
    except Exception as e:
        click.echo(e)


@cli.command()
@click.option('--entidad', default=None, type=str, help='Entidad.')
@click.option('--municipio', default=None, type=str, help='Municipio.')
@click.option('--modalidad', default=None, type=str, help='Modalidad.')
@click.option('--tipo', default=None, type=str, help='Tipo.')
@click.option('--subtipo', default=None, type=str, help='Subtipo.')
@pass_config
def idmnm_reportes(config, entidad, municipio, modalidad, tipo, subtipo):
    """
    Reportes de Incidencia Delictiva Municipal, Nueva Metodología
    """
    reportes = ReportesMunicipales(
        entidad=entidad,
        municipio=municipio,
        modalidad=modalidad,
        tipo=tipo,
        subtipo=subtipo,
        entrada=config.entrada,
        inicio=config.inicio,
        termino=config.termino,
        salida=config.salida,
        )
    try:
        if config.salvar:
            click.echo(reportes.guardar())
        else:
            click.echo(reportes.crear_ultimo())
            click.echo(reportes.crear_ano_pasado())
            click.echo(reportes.crear_ano_antepasado())
            click.echo(reportes)
    except Exception as e:
        click.echo(e)


@cli.command()
@click.option('--modalidad', default=None, type=str, help='Modalidad.')
@click.option('--tipo', default=None, type=str, help='Tipo.')
@click.option('--subtipo', default=None, type=str, help='Subtipo.')
@pass_config
def idmnm_reportes_coahuila_laguna(config, modalidad, tipo, subtipo):
    """
    Reportes de Incidencia Delictiva Municipal, Nueva Metodología
    """
    entidad = 'Coahuila de Zaragoza'
    municipios = ['Matamoros', 'San Pedro', 'Torreón', 'Viezca']
    reportes = ReportesMunicipales(
        entidad=entidad,
        municipio=municipios,
        modalidad=modalidad,
        tipo=tipo,
        subtipo=subtipo,
        entrada=config.entrada,
        inicio=config.inicio,
        termino=config.termino,
        salida=config.salida,
        )
    try:
        if config.salvar:
            click.echo(reportes.guardar())
        else:
            click.echo(reportes.crear_ultimo())
            click.echo(reportes.crear_ano_pasado())
            click.echo(reportes.crear_ano_antepasado())
            click.echo(reportes)
    except Exception as e:
        click.echo(e)

