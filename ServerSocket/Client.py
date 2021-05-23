import socket

def iniciarCliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    salida = bytes("cerrar",'utf-8')

    print("conectado")
    cliente.connect(("localhost", 5000))
    while True:
        entrante = cliente.recv(1024)
        if (entrante == salida):
            cliente.send(salida)
            break
        mensaje = entrante.decode('utf-8')
        print("->"+mensaje)

        cliente.send(bytes(input(""),'utf-8'))

iniciarCliente()