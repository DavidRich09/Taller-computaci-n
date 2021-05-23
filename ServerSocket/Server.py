import socket

def iniciarServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    salida = bytes("cerrar", 'utf-8')
    server.bind(("localhost", 5000))
    server.listen(1)
    print("Esperando conexión....")
    conexion, dir = server.accept()
    while True:
        conexion.send(bytes(input(""),'utf-8'))
        entrante = conexion.recv(1024)
        if (entrante == salida):
            conexion.send(salida)
            break
        mensaje = entrante.decode('utf-8')
        print("->"+mensaje)

iniciarServer()