
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

Pruebe consultando la ayuda...

    (Virgilio) $ virgilio --help

### Notas sobre el archivo CSV

No es un archivo con caracteres UTF-8, ni separados por comas,
por lo que estas líneas lo arreglan a ISO 8859 y separados por punto y coma...

    with open(self.entrada, encoding='iso8859') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')

### Ejemplos de usos

Mostrar los Robos a casa habitación, sin violencia
en el municipio de Lerdo, Durango,
de julio 2017 a junio 2018...

    $ virgilio --entrada IDM_NM.csv \
        --inicio 2017-07-01 --termino 2018-06-30 idmnm \
        --entidad Durango --municipio Lerdo \
        --tipo Robo --subtipo 'Robo a casa habitación' \
        --modalidad 'Sin violencia'

