        # -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:37 2019

@author: reinaqu_2
"""

from collections import namedtuple

Pico = namedtuple("Pico", "nombre altitud provincia")



def mostrar_picos1(picos):
    for pico in picos:
        print(pico)



# 2.1 Obtener una lista con los nombres de los picos ordenada alfabéticamente
# Resultado esperado: [‘Alcazaba’, ‘Llambrión’, ‘Mulhacén’, ‘Naranjo’, ‘Peña Santa’, ‘Teide’, ‘Torrecilla’, ‘Torreón’, ‘Veleta’
def nombres_ord_alfabetico(picos):
    return sorted(x.nombre for x in picos)

# 2.2 Obtener una lista con la altitud en kms y el nombre de los picos
# Resultado esperado: [(3.479, ‘Mulhacén’), (1.648, ‘Torreón’), (2.596, ‘Peña Santa’), (2.519, ‘Naranjo’), (3.371, ‘Alcazaba’), (3.396, ‘Veleta’), (1.919, ‘Torrecilla’), (2.647, ‘Llambrión’), (3.718,
# ‘Teide’)]
def altitud_y_nombre(picos):
    return [(x.altitud/1000,x.nombre) for x in picos]

# 2.3 Obtener una lista con los picos que están en la provincia de Granada
# Resultado esperado: [(‘Mulhacén’, 3479, ‘Granada’), (‘Alcazaba’, 3371, ‘Granada’), (‘Veleta’, 3396,
# ‘Granada’)]
def picos_en_provincia(picos, provincia='Granada'):
    # generalizada para cualquier provincia, no solo Granada
    return [x for x in picos if provincia==x.provincia]

# 2.4 Obtener una lista con la altitud y el nombre de los picos que tienen más de 2000
# metros de altitud, ordenada de mayor a menor altitud
# Resultado esperado: [(3718, ‘Teide’), (3479, ‘Mulhacén’), (3396, ‘Veleta’), (3371, ‘Alcazaba’), (2647,
# ‘Llambrión’), (2596, ‘Peña Santa’), (2519, ‘Naranjo’)]
def picos_con_altitud_ord(picos, altitud=2000):
    # generalizada a cualquier altitud mínima
    return sorted([(x.altitud,x.nombre) for x in picos if altitud<x.altitud], key=lambda n: n[0], reverse=True)

# 2.5 Obtener la suma de las altitudes de los picos que están en la provincia de León
# Resultado esperado: 5243
def suma_altitudes_en_provincia(picos, provincia='León'):
    # generalizada a cualquier provincia
    return sum(x.altitud for x in picos if provincia==x.provincia)

# 2.6 Obtener el nombre y la altitud del pico más alto de la lista
# Resultado esperado: (3718, ‘Teide’)
def nombre_y_altitud_mas_alto(picos):
    return max([(x.altitud,x.nombre) for x in picos], key=lambda n: n[0])

# 2.7 Obtener la altitud media de los picos
# Resultado esperado: 2810.3333333333335
from statistics import mean
def altitud_media(picos):
    return mean(x.altitud for x in picos)

# 2.8 Obtener una lista ordenada con las provincias donde hay picos, sin repetir ninguna
# Resultado esperado: [‘Asturias’, ‘Cádiz’, ‘Granada’, ‘León’, ‘Málaga’, ‘Santa Cruz de Tenerife’]
def provincia_con_picos_ord(picos):
    return sorted(set(x.provincia for x in picos))