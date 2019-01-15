#!/usr/bin/env python

import pyexcel as p
import os
import sys

dir = "."
if len(sys.argv) == 2:
    dir = sys.argv[1]

unit_sales={}
title = {}
for filename in os.listdir(dir):
    if filename.startswith("KDP ") or filename.startswith("Sales "):
        records = p.get_records(file_name=dir+filename)
        for record in records:
            if (record['Unidades netas vendidas'] == '' ):
                continue
            if 'ASIN/ISBN' in record:
                asin_name = 'ASIN/ISBN'
            else:
                asin_name = 'ASIN'
            fecha = record['Fecha de las regalías']
            mercado = record['Mercado']
            asin=record[asin_name]
            if not fecha in unit_sales :
                unit_sales[fecha] = {}
            if not asin in unit_sales[fecha]:
                unit_sales[fecha][asin] = {}
            if not mercado in unit_sales[fecha][asin]:
                unit_sales[fecha][asin][mercado] = record['Unidades netas vendidas']
            title[asin] = record['Título']


asin_sales={}
for fecha in unit_sales:
    for asin in unit_sales[fecha]:
        for mercado in unit_sales[fecha][asin]:
            if asin in asin_sales:
                asin_sales[asin] = asin_sales[asin]+unit_sales[fecha][asin][mercado]
            else:
                asin_sales[asin] = unit_sales[fecha][asin][mercado]

print("Title, Units")
for asin in asin_sales:
    if asin in title:
        print(f"\"{title[asin]}\", {asin_sales[asin]}")
    else:
        print(f"\"{asin}\", {asin_sales[asin]}")
    
