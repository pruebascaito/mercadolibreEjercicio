#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import requests

i = 1
#itero para verificar que tiene mas de un parametro
if (sys.argv[i] > i):
	
	y = 0
	#itero el parametro pasado por linea de comando
	for x in range(len(sys.argv[i])):
		print("----------------------------------")		
		#envio un request con seller_id enviado por linea de comando
		files_response = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id='+ sys.argv[i])
		#Lo convierto en json
		file_json = files_response.json()
		
		try:

			#limito que me devuelva 40 item
			while(y < 40):
				# recorro para obtener
				id = file_json['results'][y]['id']
				title = file_json['results'][y]['title']
				cateId = file_json['results'][y]['category_id']
				#vuelvo  a enviar un request para obtener el nombre de la categoria del producto
				response = requests.get('https://api.mercadolibre.com/categories/'+ cateId)
				#lo transforo en json
				rJson = response.json()
				
				name = rJson['name']
				#imprimo el resultado
				print(id, title, cateId, name)
				y = y + 1
				
				
				
				
		except ValueError:
			print("Lo que escribiste NO es un entero") 
	
		
						
			
	i = i + 1	
else:
	print("No se ingreso parametros...")	