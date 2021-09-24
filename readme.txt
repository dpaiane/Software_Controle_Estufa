comunicacao arduino - tinker
********************************************************************
para iniciar o vnc server
x11vnc
*********************************************************************
os.system("python myOtherScript.py arg1 arg2 arg3")

**********************************************************************
Comando para tornar o script.py em um executavel do sistema
	chmod +x seuscript.py


***********************************************************************
arquivos do sistema plantario
	aplic_script.service
	app_script.service


diretorio do servico
	/lib/systemd/system


starta o servico
	sudo systemctl start app_script


lista os servicos com falha
     systemctl --failed

*********************************************************************
comando para agendar o reset do sistema

	sudo shutdown -r HH:MM

********************************************************************
https://culturannabis.com/br/calculo-de-iluminacao/