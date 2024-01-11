# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:48 2019

@author: reinaqu_2
"""
from picos import *

if __name__=='__main__':
    PICOS = [Pico("Mulhacén", 3479, "Granada"), 
             Pico("Torreón", 1648, "Cádiz"),
             Pico("Peña Santa", 2596, "León"), 
             Pico("Naranjo", 2519, "Asturias"),
             Pico("Alcazaba", 3371, "Granada"), 
             Pico("Veleta", 3396, "Granada"),
             Pico("Torrecilla", 1919, "Málaga"), 
             Pico("Llambrión", 2647, "León"),
             Pico("Teide", 3718, "Santa Cruz de Tenerife")]
             
    mostrar_picos1(PICOS)
    exercise_functions_list =  [nombres_ord_alfabetico(PICOS),
                                altitud_y_nombre(PICOS),
                                picos_en_provincia(PICOS),
                                picos_con_altitud_ord(PICOS),
                                suma_altitudes_en_provincia(PICOS),
                                nombre_y_altitud_mas_alto(PICOS),
                                altitud_media(PICOS),
                                provincia_con_picos_ord(PICOS)]

    for i,function in enumerate(exercise_functions_list, 1):
        print(f'Exercise 2.{i}:\n\t{function}')