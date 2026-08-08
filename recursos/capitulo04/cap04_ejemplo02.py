# cap04_ejemplo02.py
## Este ejemplo asume que usa Python algo antiguo.
 
## Definición de variables
pieza_peso = 0.0
mensaje = ''
 
## Input
pieza_peso = float(input('Indique el peso de la pieza: '))
 
## Process
if pieza_peso >= 500:
    mensaje = 'Aprobada'
else:
    mensaje = 'Rechazada'
 
## Output
print('La pieza fue ' + mensaje)