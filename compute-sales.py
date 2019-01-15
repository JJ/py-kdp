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
                asin = 'ASIN/ISBN'
            else:
                asin = 'ASIN'
            fecha = record['Fecha de las regalías']
            if not fecha in unit_sales :
                 unit_sales[fecha] = {}
            unit_sales[fecha][record[asin]]=record['Unidades netas vendidas']
            title[record[asin]] = record['Título']


asin_sales={}
for fecha in unit_sales:
    for asin in unit_sales[fecha]:
        if asin in asin_sales:
            asin_sales[asin] = asin_sales[asin]+unit_sales[fecha][asin]
        else:
            asin_sales[asin] = unit_sales[fecha][asin]

print("Title, Units")
for asin in asin_sales:
    print(title[asin], ", ", asin_sales[asin])
    
