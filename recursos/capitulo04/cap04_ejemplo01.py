# cap04_ejemplo01.py
## Este ejemplo asume que usa Python 3.10 o superior que utiliza typing.
 
## Definición de variables
pieza_peso:float = 0.0
mensaje:str = ''
 
## Input
pieza_peso = float(input('Indique el peso de la pieza: '))
 
## Process
if pieza_peso >= 500:
    mensaje = 'Aprobada'
else:
    mensaje = 'Rechazada'
 
## Output
print('La pieza fue ' + mensaje)