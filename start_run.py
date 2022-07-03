#!/usr/bin/env python
#encoding: utf-8
#####################################################################################
########								#############
########    Projeto plantario - Diego paiani cardoso			#############
########    Faculdade de engenharia de computacao - FTEC		#############
########    Versao: 1.122						#############
########								#############
#####################################################################################

import serial					# carrega as bibliotecas necessarias
import re					# carrega as bibliotecas necessarias
import urllib3					# carrega as bibliotecas necessarias
import time					# carrega as bibliotecas necessarias
import os					# carrega os modulos para  o projeto

from datetime import datetime			# importa a biblioteca

chave = 'HUU99AP7J6VEFNNV'												# chave para acesso a api
url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}'	# envia dados para a api

arduino = serial.Serial("/dev/ttyUSB0", 9600)										# configura comunicacao com arduino
arquivo = open("/home/linaro/Desktop/Plantario/log_aplic.txt", "w")							# abre o arquivo como escrita

while(1):														# laco de repeticao
	data_texto = datetime.now()
	data_hora = data_texto.strftime("%d/%m/%Y %H:%M")								# foemata a forma da hora e data
	valor_recebido = arduino.readline()
	print(valor_recebido)
	
	arquivo.write(valor_recebido + data_hora)									# gera os logs da aplicacao

	lista_sensores = valor_recebido.split(" ")									# tira por espaco
	dia = lista_sensores[1]												# separa a variavel dia
	ciclo = lista_sensores[3]											# define variavel dia
	umidade_ar = lista_sensores[5]											# define variavel umidade do ar
	temperatura = lista_sensores[7]											# define variavel temperatura
	umidade_solo1 = re.sub('[^0-9]', '', lista_sensores[9])								# salva somente algarismos de 0 a 9
	umidade_solo2 = re.sub('[^0-9]', '', lista_sensores[11])							# salva somente algarismos de 0 a 9
	umidade_solo3 = re.sub('[^0-9]', '', lista_sensores[9])								# salva somente algarismos de 0 a 9
	umidade_solo4 = re.sub('[^0-9]', '', lista_sensores[11])							# salva somente algarismos de 0 a 9
	# print(lista_sensores)												# imprimi a variavel recebida

	print("\n")													# separa o texto
	print data_hora													# indica que os dados estao prontos
	print "dias:", dia												# imprimi na tela

	if(ciclo == 20):												# define o ciclo como noite ou dia
		print("ciclo: Noite")											# condicao
	else:														# caso contrario
		print("ciclo: Dia")											# condicao

															# indica que os dados estao prontos
	urllib3.PoolManager().request("GET", url.format(chave, temperatura, umidade_ar, umidade_solo1, umidade_solo2, umidade_solo3, umidade_solo4))
	time.sleep(30)													# tempo de execucao para api
