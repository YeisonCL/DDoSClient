DDoSClient
===========
## Descripción
Programa que realizar un ataque DDos a un sitio especificado utililizando el cliente en Python y el cliente en C que se puede encontrar en este mismo sitio.

##Running
Interpretar usando python y ejecutar con la opciones disponibles.

```
python3 stressCMD.py
```

##Options

###-n
Cantidad de threads que serán utilizados para realizar las peticiones.

```
python3 stressCMD.py -n 50
```

###-c
Nombre del cliente que será usado para realizar el ataque, "httpclient.c" o "httpclient.py".

```
python3 stressCMD.py -n 50 -c httpclient.py
```

###-u
Dirección a la cual se realizará el ataque.

```
python3 stressCMD.py -n 50 -c httpclient.py -u http://algunadireccion.com
```

###-h
Brinda información sobre las opciones mencionadas anteriormente.

```
python3 stressCMD.py -h
```
