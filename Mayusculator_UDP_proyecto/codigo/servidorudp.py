from socket import *

serviPuerto = 12000

socketServidor = socket(AF_INET, SOCK_DGRAM)
socketServidor.bind(('', serviPuerto))

print("Soy Mayusculator UDP y espero cadenas en minuscula")

while True:
    mensaje, clienteDir = socketServidor.recvfrom(1024)

    mensaje = mensaje.decode("utf-8")

    print("Mensaje recibido:", mensaje)

    mensajeMay = mensaje.upper()

    socketServidor.sendto(mensajeMay.encode("utf-8"), clienteDir)
