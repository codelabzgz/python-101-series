"""
Solución al problema de calentamiento del Calendario de Adviento de CodeLab 2024.
Este script calcula los siguientes dos números de la secuencia de Fibonacci, 
dada una pareja inicial de números proporcionados como argumentos en la línea de comandos.

Author: CodeLabZGZ
Date:   2024-11-29
Event:  Calendario de Adviento 2024
"""

import sys

def fibonacci(a, b):
  fibo = [a, b]
  for _ in range(3):
    next_number = fibo[-1] + fibo[-2]
    fibo.append(next_number)
  return fibo[2:]

if __name__ == "__main__":
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  next_fib_numbers = fibonacci(a, b)
  print(", ".join(map(str, next_fib_numbers)), end="")