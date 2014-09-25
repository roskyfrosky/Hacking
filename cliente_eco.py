'''
    ____             __         ____                __        
   / __ \____  _____/ /____  __/ __/________  _____/ /____  __
  / /_/ / __ \/ ___/ //_/ / / / /_/ ___/ __ \/ ___/ //_/ / / /
 / _, _/ /_/ (__  ) ,< / /_/ / __/ /  / /_/ (__  ) ,< / /_/ / 
/_/ |_|\____/____/_/|_|\__, /_/ /_/   \____/____/_/|_|\__, /  
                      /____/                         /____/   

'''

import socket

HOST = '127.0.0.1'
PORT = 50007
#Definimos que nos vamos a conectar utilizando IPv4 (AF_INET)
#utilizando el protocolo tcp (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Nos conectamos a HOST por el puerto PORT
s.connect((HOST, PORT))
#Le enviamos una cadena de texto
s.sendall('Hello, world')
#Esperamos su contestacion
data = s.recv(1024)
#Cerramos el socket
s.close()
#Mostramos los datos recibidos
print 'Received', repr(data)
