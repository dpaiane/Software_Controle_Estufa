#########################################################################################
########								    #############
########    Projeto plantario - Diego paiani cardoso			    #############
########    Faculdade de engenharia de computacao - FTEC		    #############
########    Versao: 1.122						    #############
########								    #############
#########################################################################################

#encoding: utf-8

from datetime import datetime

import sys
import os
import serial
import re
import time
#import urllib3
import tkinter as tk

chave = 'HUU99AP7J6VEFNNV'
url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}'
#arduino = serial.Serial("/dev/ttyUSB0", 9600)
iniciar_set = False

class myApp(object):

    def __init__(self, **kw):

        self.root = tk.Tk()
        self.root.title("aplicação plantario")
        self.root.geometry("700x450")
        self.create_canvas_area()
        self.create_status_bar()

    def create_status_bar(self):
        self.status = tk.Label(self.root, text="Bem vindo a Interface Plantario - Eng Diego Paiani Cardoso", bd=1, relief=tk.SUNKEN)
        self.status.pack(side= tk.BOTTOM, fill = tk.X) 

    def create_canvas_area(self):
        self.lbl1 = tk.Label(self.root, text="Interface Plantario",fg= "blue", font= ("Arial" ,"28", "bold"))
        self.text1 = tk.Text(self.root, height=15, width=60, bg="black", fg="white")
        
        self.text1.insert(tk.END, "INSIRA O INTERVALO DE LUZ:\n\n")
        self.text1.insert(tk.END, " 0 - Usa os dados salvos.\n")
        self.text1.insert(tk.END, " 1 - Usar intervalo de 11 horas.\n")
        self.text1.insert(tk.END, " 2 - Usar intervalo de 12 horas.\n")
        self.text1.insert(tk.END, " 3 - Usar intervalo de 13 horas.\n")
        self.text1.insert(tk.END, " 4 - Usar intervalo de 14 horas.\n")
        self.text1.insert(tk.END, " 5 - Usar intervalo de 15 horas.\n")
        self.text1.insert(tk.END, " 6 - Usar intervalo de 16 horas.\n")
        self.text1.insert(tk.END, " 7 - Usar intervalo de 17 horas.\n")
        self.text1.insert(tk.END, " 8 - Usar intervalo de 18 horas.\n")
        self.text1.insert(tk.END, " 9 - Apagar os dados salvos.\n")
        
        self.frame1 = tk.Frame(self.root)
        
        self.btniniciar= tk.Button(self.frame1, text = " iniciar ",command=self.iniciar)
        self.btncamera= tk.Button(self.frame1, text = " Camera ",command=self.camera)
        self.btnTemp= tk.Button(self.frame1, text = " Sensores ",command=self.sensores)
        self.btnIntervalo= tk.Button(self.frame1, text =" Intervalo:",command=self.intervalo)
        
        self.entry1= tk.Entry(self.frame1,width=10 )
        self.entry1.insert( 0,"12") 

        self.btniniciar.pack(side = tk.LEFT, padx= 15, pady= 18)
        self.btncamera.pack(side = tk.LEFT, padx= 15, pady= 18)
        self.btnTemp.pack(side = tk.LEFT,  padx= 15, pady= 18)
        
        self.btnIntervalo.pack(side = tk.LEFT, padx= 15, pady= 18)
        
        self.entry1.pack(side = tk.LEFT,padx= 15, pady= 18)

        data_texto = datetime.now()
        data_atual = 28 #data_texto.strftime("%d/%m/%Y")

        self.data1 = tk.StringVar()
        self.data1.set(data_atual)
        
        
        self.lbl2 = tk.Label(self.root, text="Dias cultivando: ", fg= "green", font= ("Arial" ,"12"))
        self.lbl3 = tk.Label(self.root, textvariable=self.data1, fg= "green", font= ("Arial" ,"12", "bold"))
        
        self.lbl1.pack()
        self.text1.pack()
        self.frame1.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        
    def finaliza_software(self):
        self.root.destroy()        
      
    def execute(self):
        self.root.mainloop()

    def camera(self):
        self.text1.delete("1.0", "end")
        data_texto = datetime.now()
        data_hora = data_texto.strftime("%d/%m/%Y %H:%M\n")
        self.text1.insert(tk.END, data_hora)
        self.text1.insert(tk.END, "\n Camera iniciada com sucesso...\n")
          
    def iniciar(self):
        global iniciar_set

        if(iniciar_set == True):
            self.text1.delete("1.0", "end")                                  
            self.text1.insert(tk.END, "INSIRA O INTERVALO DE LUZ:\n\n")
            self.text1.insert(tk.END, " 0 - Usar dados salvos.\n")
            self.text1.insert(tk.END, " 1 - Usar intervalo de 10 horas.\n")
            self.text1.insert(tk.END, " 2 - Usar intervalo de 11 horas.\n")
            self.text1.insert(tk.END, " 3 - Usar intervalo de 12 horas.\n")
            self.text1.insert(tk.END, " 4 - Usar intervalo de 13 horas.\n")
            self.text1.insert(tk.END, " 5 - Usar intervalo de 14 horas.\n")
            self.text1.insert(tk.END, " 6 - Usar intervalo de 15 horas.\n")
            self.text1.insert(tk.END, " 7 - Usar intervalo de 16 horas.\n")
            self.text1.insert(tk.END, " 8 - Usar intervalo de 18 horas.\n")
            self.text1.insert(tk.END, " 9 - Apagar os dados salvos.\n")
            iniciar_set = False
            
        else:
            self.text1.delete("1.0", "end")
            data_texto = datetime.now()
            data_hora = data_texto.strftime("%d/%m/%Y %H:%M\n")
            data_plantio = data_hora                                   
            self.text1.insert(tk.END, data_hora)
            self.text1.insert(tk.END, "\n Iniciando servico...\n")
            self.text1.insert(tk.END, "\n Servico iniciado com sucesso...\n")
            iniciar_set = True 
        
    def sensores(self):	
        self.text1.delete("1.0", "end")							                        
        data_texto = datetime.now()
        data_hora = data_texto.strftime("%d/%m/%Y %H:%M\n")			                        
        self.text1.insert(tk.END, data_hora)
        self.text1.insert(tk.END, "\nLendo os sensores...\n")
        self.text1.insert(tk.END, "\nProcessando os dados...\n")				                              															
		
    def intervalo(self):
        self.text1.delete("1.0", "end")
        data_texto = datetime.now()
        data_hora = data_texto.strftime("%d/%m/%Y %H:%M\n")                                 
        self.text1.insert(tk.END, data_hora)
        self.text1.insert(tk.END, "\nIntervalo inserido com sucesso\n")
        self.text1.insert(tk.END, self.entry1.get())
        self.text1.insert(tk.END, "\nDados salvos\n")
   
def main(args):
    app_proc = myApp()
    app_proc.execute()    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
