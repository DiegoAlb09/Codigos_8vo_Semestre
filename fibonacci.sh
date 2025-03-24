#!/bin/bash

# Script para generar la serie de Fibonacci

# Program for Fibonacci
# Series
echo "Dame hasta que posición de Fibonacci generar: "  
# Static input for N
read N1
 
# First Number of the
# Fibonacci Series
a=0
 
# Second Number of the
# Fibonacci Series
b=1 
  
echo "The Fibonacci series is : "
  
for (( i=0; i<$N1; i++ ))
do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done
# End of for loop

