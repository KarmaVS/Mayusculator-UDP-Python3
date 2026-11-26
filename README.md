# Mayusculator UDP - Python 3

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![UDP](https://img.shields.io/badge/Protocolo-UDP-green)
![Debian](https://img.shields.io/badge/Servidor-Debian-red?logo=debian)
![Ubuntu](https://img.shields.io/badge/Cliente-Ubuntu-orange?logo=ubuntu)
![SRI](https://img.shields.io/badge/Asignatura-SRI-lightgrey)

## Descripción

Aplicación cliente-servidor que envía un texto mediante UDP y devuelve el mismo texto en mayúsculas. Práctica de Sistemas de Redes e Internet (SRI).

## Entorno de trabajo

| Característica | Configuración prevista |
|---|---|
| Servidor | Debian |
| Cliente | Ubuntu |
| IP del servidor | 192.168.3.3/24 |
| Puerto | 12000/UDP |
| Lenguaje | Python 3 |

## Código fuente

- [Servidor UDP](codigo/servidorudp.py)
- [Cliente UDP](codigo/clienteudp.py)

## Funcionamiento

El servidor utiliza `SOCK_DGRAM`, recibe datagramas con `recvfrom()`, transforma el mensaje mediante `upper()` y responde con `sendto()`. El cliente envía una cadena codificada en UTF-8 y espera la respuesta. UDP no garantiza entrega ni orden.

## Ejecución

No se necesitan librerías externas. Desde la raíz del repositorio, en Debian:

```bash
python3 codigo/servidorudp.py
```

En Ubuntu:

```bash
python3 codigo/clienteudp.py
```

Ejemplo esperado: `hola mundo` → `HOLA MUNDO`.

Para comprobar el puerto en Debian:

```bash
sudo ss -ulnp | grep ':12000'
```

## Capturas de la práctica

Añadir las imágenes reales en `codigo/imagenes/` con los nombres indicados. Hasta entonces los enlaces no mostrarán las imágenes.

### 1. Dirección IP del servidor

![IP Debian](codigo/imagenes/01_ip_debian.png)

### 2. Conectividad desde Ubuntu

![Conectividad](codigo/imagenes/02_conectividad.png)

### 3. Inicio del servidor UDP

![Servidor esperando](codigo/imagenes/03_servidor_esperando.png)

### 4. Puerto UDP

![Puerto UDP](codigo/imagenes/04_puerto_udp.png)

### 5. Envío y respuesta en el cliente

![Cliente Ubuntu](codigo/imagenes/05_cliente_ubuntu.png)

### 6. Recepción en el servidor

![Servidor recibiendo](codigo/imagenes/06_servidor_recibiendo.png)

## Documentación

La memoria definitiva se podrá consultar en la carpeta `documentacion/` una vez completada y subida al repositorio.

## Referencias

- [Documentación de sockets de Python](https://docs.python.org/es/3/library/socket.html)
- [RFC 768 - UDP](https://www.rfc-editor.org/rfc/rfc768)

## Autores

- KarmaVS
- pedro-hg07

---
Proyecto académico - Sistemas de Redes e Internet (SRI)

