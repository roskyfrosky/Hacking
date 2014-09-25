'''
    ____             __         ____                __        
   / __ \____  _____/ /____  __/ __/________  _____/ /____  __
  / /_/ / __ \/ ___/ //_/ / / / /_/ ___/ __ \/ ___/ //_/ / / /
 / _, _/ /_/ (__  ) ,< / /_/ / __/ /  / /_/ (__  ) ,< / /_/ / 
/_/ |_|\____/____/_/|_|\__, /_/ /_/   \____/____/_/|_|\__, /  
                      /____/                         /____/   

'''
# Echo server program
import socket

HOST = ''              
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET ->  es una constante que define la familia del protocolo, en este caso IPv4
#SOCK_STREAM -> representa el tipo de socket en este caso TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Mas adelante vamos a ligar nuestra ip a un puerto determinado, con la linea anterior le indicamos
#al socket que desligue esta union lo antes posible para evitarnos errores como 
# socket.error: [Errno 98] Address already in use
#Si no le indicamos esto al socket y ejecutaramos el script muchas veces seguidas, no dariamos
#tiempo al S.O de desligar la union socket-puerto
s.bind((HOST, PORT))
#Con bind indicamos al socket que tiene que ligar al socket que acabamos de crear
#la direccion IP (127.0.0.1) y el puerto especificado
#El resultado es que nuestro socket se quedara escuchando en el puerto PORT por la interfaz que 
#contenga la ip HOST
s.listen(1)
#Con listen definimos el numero maximo de clientes, si se supera las siguientes conexiones de otros
#clientes seran denegadas
conn, addr = s.accept()
#Accept es bloqueante, y se quedara bloqueada hasta recibir una conexion
#Cuando reciba una conexion devuelve
#conn -> el socket del cliente
#addr -> la direccion y puerto del cliente
print 'Connected by', addr
#En este bucle recibimos 1024 bytes del cliente y le enviamos el mismo mensaje  (servidor echo)
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
#Cerramos la conexion con el cliente
conn.close()
