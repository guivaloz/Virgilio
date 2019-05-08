#!/bin/bash

# Ejecutar configuracion local
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# VirtualEnv
. bin/activate
cd Virgilio/

echo "+-----------------------+"
echo "|  VirtualEnv Virgilio  |"
echo "+-----------------------+"
echo
virgilio --help
echo

# Instrucciones
echo "Pruebe con su archivo CSV..."
echo "  $ cd /mnt/cascarrabias/DB/SecretariadoEjecutivo/2019-03/"
echo "  $ ls IDM_NM_mar19_05.csv"
echo "  $ virgilio --entrada IDM_NM_mar19_05.csv \\"
echo "      --inicio 2019-01-01 --termino 2019-03-31 \\"
echo "      idmnm-reportes-coahuila --region Laguna \\"
echo "      --tipo Robo --subtipo 'Robo a casa habitación'"
echo
