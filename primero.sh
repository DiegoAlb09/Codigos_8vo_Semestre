#!/bin/bash

echo "Como te llamas?"
read NOM
echo "Saludos $NOM, vamos a sumar dos numeros"

echo "Dame el primer numero: "
read N1
echo "Dame el segundo numero: "
read N2

RES=$(expr $N1 + $N2)
echo "La suma es: $RES"
