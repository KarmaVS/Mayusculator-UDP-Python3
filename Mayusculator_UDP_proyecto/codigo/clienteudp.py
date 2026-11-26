from socket import *

serviNombre = '192.168.3.3'
serviPuerto = 12000

socketCliente = socket(AF_INET, SOCK_DGRAM)

mensaje = input('Mete una linea en minusculas: ')

socketCliente.sendto(mensaje.encode("utf-8"),
                     (serviNombre, serviPuerto))

mensajeMayu, servidorDir = socketCliente.recvfrom(1024)

print(mensajeMayu.decode("utf-8"))

socketCliente.close()
