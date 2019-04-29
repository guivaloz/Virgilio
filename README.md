
# Virgilio

Scripts en Python para generar reportes de los Datos Abiertos de Incidencia Delictiva.

Se llama _Virgilio_ porque en la obra de **Dante Alighieri,** _La Divina Comedia,_ es el guía de _Dante_ a través del Infierno y del Purgatorio.

### Instalación

Cree un entorno virtual de Python 3...

    $ cd ~/Documentos/VirtualEnv
    $ virtualenv -p python3 Virgilio
    $ cd Virgilio
    $ . bin/activate

Clone este repositorio de GitHub...

    (Virgilio) $ git clone https://github.com/guivaloz/Virgilio.git
    (Virgilio) $ cd Virgilio

Instale...

    (Virgilio) $ pip install -r requirements.txt
    (Virgilio) $ pip install --editable .

Consulte la ayuda...

    (Virgilio) $ virgilio --help
    (Virgilio) $ virgilio idmnm --help
    (Virgilio) $ virgilio idmnm-reportes --help
    (Virgilio) $ virgilio idmnm-reportes-coahuila --help

### Secretariado Ejecutivo

En la siguiente página podrá encontrar los archivos de datos abiertos...

    https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published

Descargue los archivos IDEFC_NM (estatal) y IDM_NM (municipal).

### Notas sobre el archivo CSV

Si no es un archivo con caracteres UTF-8, ni separados por comas,
debe cambiar estas líneas...

    with open(self.entrada, encoding='utf8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')

Por ejemplo, a ISO 8859...

    with open(self.entrada, encoding='iso8859') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')

### Acelere el script creando un archivo para su estado

Por ejemplo, para extraer 'Coahuila de Zaragoza' a un nuevo archivo IDM_NM_05.csv, ejecute...

    $ head -n1 IDM_NM.csv > IDM_NM_05.csv
    $ grep -a 'Coahuila de Zaragoza' IDM_NM.csv >> IDM_NM_05.csv

### Ejemplos de usos

Mostrar los Robos a casa habitación, sin violencia
en el municipio de Lerdo, Durango,
de julio 2017 a junio 2018...

    $ virgilio --entrada IDM_NM.csv \
        --inicio 2017-07-01 --termino 2018-06-30 idmnm \
        --entidad Durango --municipio Lerdo \
        --tipo Robo --subtipo 'Robo a casa habitación' \
        --modalidad 'Sin violencia'

Mostrar un reporte trimestral de la Región Laguna,
de Robo a casa habitación, del presente año y los dos anteriores...

    $ virgilio --entrada IDM_NM_mar19_05.csv \
        --inicio 2019-01-01 --termino 2019-03-31 idmnm-reportes-coahuila-laguna \
        --tipo Robo --subtipo 'Robo a casa habitación'
